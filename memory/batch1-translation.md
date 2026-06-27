---
name: batch1-translation-record
description: "49-concept Lean 4 translation: strategy evolution from monolithic to phased to resilient, costs, pass rates"
metadata: 
  node_type: memory
  type: project
  originSessionId: 32b0208b-f009-4db0-9b54-c8a7af2b3275
---

# Batch 1: 49-Concept Lean 4 Translation Record

> 2026-06-23 · 1 day · ~¥50 API cost

## Evolution of Strategy

### Attempt 1: Monolithic (Phase 0)
Each agent does EVERYTHING in one call: gap-fill → grep Mathlib4 → write .lean → compile → self-heal.

| Metric | Value |
|---|---|
| Concepts | 50 |
| Files created | 32 |
| Compile PASS | 9 (28%) |
| StructuredOutput failures | 39/50 |

**Why it failed**: Prompt too long (~1500 words, 6 steps), DeepSeek thinking exhausted before reaching compile step. Agents wrote files but never compiled them. API disconnections mid-task left no recovery mechanism.

### Attempt 2: Phased (Phase 1 + Phase 2)
Split into Phase 1 (gap-fill only, ~200 words) and Phase 2 (translate+compile+self-heal, ~300 words).

| Phase | Input | Output |
|---|---|---|
| Phase 1 gap-fill | 21 theorems | 21 expanded proofs (16 PASS + 5 near-pass QC) |
| Phase 2 translate | 49 concepts (21 gap-filled + 28 defs) | 40 files, 19 PASS (48%) |

**Improvement**: 28% → 48% pass rate. Shorter prompts reduced thinking exhaustion. Phase 1 QC caught low-quality gap-fills before they poisoned Phase 2.

**Remaining problem**: 31/49 agents still failed StructuredOutput due to API errors during compile+self-heal loop.

### Attempt 3: Resilient (v3-v4)
Added retry loop with `try-catch` around `agent()`, disk-based `.done`/`.fail` markers, and external Checker script.

Key discoveries:
- `agent()` **throws** on API error, doesn't return null → must catch
- Separate Checker (local Python compile) + Fixer (Pro Agent repair) pattern
- Disk files are the only reliable completion proof
- Checker script must be external file, not inline Python `-c` (escaping bugs)

## Cost Breakdown

| Phase | Model | Cost |
|---|---|---|
| Phase 0 monolithic (50 concepts) | Pro | ~¥15 |
| Phase 1 gap-fill (21 + 14 redo) | Pro | ~¥3 |
| Phase 2 translate (49 concepts) | Pro | ~¥15 |
| Resilient fix attempts (v2-v4, ~60 agent calls) | Pro | ~¥12 |
| Checker calls (~200+ calls, 500 chars each) | Pro | ~¥2 |
| **Total** | | **~¥50** |

## Final Batch 1 Status (as of v4 running)

- ✅ 12 concepts: compile PASS
- 🔄 11 concepts: undergoing resilient fix (Checker+Fixer)
- 📁 52 .lean files on disk

## Key Lessons

1. **Phased beats monolithic.** Short focused prompts > one mega-prompt.
2. **Compile offload is essential.** Agents should write code, not compile it. Use `lake env lean` locally (parallel, free).
3. **API errors are the norm, not the exception.** Every workflow MUST have try-catch + retry + disk markers.
4. **StructuredOutput is unreliable with DeepSeek.** Use disk files as completion proof instead.
5. **Multi-workflow = real concurrency.** Single workflow caps at ~16. Launch 2-3 simultaneously.
6. **Checker should be a standalone Python script.** Never embed multi-line Python in JS prompts.
7. **5-minute network drops are survivable.** Checker is fast (~5s), Fixer retries naturally.

## Related
- [[resilient-workflow]] — the v4 pattern that finally worked
- [[subagent-workflow]] — original approach before network issues
- [[deepseek-api]] — API configuration
