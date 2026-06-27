---
name: claude-subagent-workflow
description: Using Claude Code Workflow + subagents for parallel Lean translation
metadata: 
  node_type: memory
  type: project
  originSessionId: bfc46d42-3656-4af8-b6a8-57278284f040
---

# Claude Subagent Workflow for Lean Translation

## Why Subagents Beat Python API Calls

| Dimension | Python Pipeline | Claude Subagents |
|---|---|---|
| Error understanding | Pattern matching on text | Reads and understands Lean errors |
| Mathlib4 lookup | Grep with fixed patterns | Grep with context + understands results |
| Code fixing | Sends error to DeepSeek API | Reads file, edits, recompiles |
| Iteration | Fixed 10-round loop | Adaptive — stops when fixed |
| Parallelism | ThreadPoolExecutor | Workflow `parallel()` |
| Token cost | DeepSeek API ($) | Claude tokens (included) |

## Best Workflow Pattern

```javascript
// Phase 1: Gap-fill all concepts in parallel
const gaps = await parallel(concepts.map(c => () =>
  agent(`Expand this proof: ${c.statement} ...`, {phase: 'Gap-fill'})
))

// Phase 2: Lean translate all in parallel
const leanCode = await parallel(concepts.map((c, i) => () =>
  agent(`Translate to Lean 4: ${gaps[i]} ...`, {phase: 'Lean translate'})
))

// Phase 3: Compile + fix all in parallel
const compiled = await parallel(concepts.map((c, i) => () =>
  agent(`Write to Pipeline.lean, lake build, fix errors...`, {phase: 'Compile'})
))
```

## Key Lessons from First Test

1. **Agents produce WORKING code structure** — correct imports, proper theorem/def syntax, good use of Mathlib4
2. **API names are often wrong** — agent will use `Sylow.card_sylow_modEq_one` when the actual name is `card_sylow_modEq_one` (top-level, not namespaced)
3. **Agents need 2-3 compilation attempts** — first draft has 1-3 API name errors, but the logic is correct
4. **Manual fix of 1-3 lines is acceptable** for final compilation

## Batch 1 Production Lessons (2026-06-23)

After processing 49 concepts at scale, the original "one call per concept" approach was proven wrong:

1. **Phased beats monolithic.** Gap-fill + translate + compile + self-heal in ONE agent call failed at scale (28% pass rate). Splitting into Phase 1 (gap-fill) and Phase 2 (translate+compile+heal) doubled pass rate to 48%.

2. **API errors dominate failures, not math difficulty.** The 2.4G WiFi drops ~5s every ~5min. DeepSeek `agent()` throws on API error, breaking retry loops. Solution: `try-catch` + disk-based `.done`/`.fail` markers.

3. **StructuredOutput is unreliable with DeepSeek.** ~60% of agents fail to call it. Use disk files as completion proof instead.

4. **Checker + Fixer pattern (v4).** Separate local compilation checking (Python script, ~5s, no model needed) from code fixing (DeepSeek Pro agent, minutes). Checker writes `.done` or `.fail` to disk. Fixer only triggered on `.fail`.

5. **Compile locally, not in agents.** `lake env lean` with `xargs -P 16` is parallel, free, and doesn't consume API tokens. Agents should focus on writing code, not running compilation loops.

6. **Multi-workflow for real concurrency.** Single Workflow caps at ~16 concurrent agents. Launch 2-3 simultaneously for 30-48 real concurrent agents.

7. **`agent()` throws on API error, returns null on StructuredOutput failure.** Must `try-catch` the former; must not depend on return value for the latter.

## Current Best Pattern (resilient_v4)

See [[resilient-workflow]] for the complete pattern.

```javascript
// Phase 1: Gap-fill only, short prompt, QC after
// Phase 2: Checker (local compile) + Fixer (Pro agent) with retry
for (var attempt = 0; attempt < MAX_RETRIES; attempt++) {
  try { await agent('python3 checker.py ' + idx) } catch(e) {}
  // Check .done/.fail on disk → retry or fix
}
```
