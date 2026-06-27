# CLAUDE.md — mathpkg Project Instructions

## Project: mathpkg — Mathematical Knowledge Package Manager

Builds a machine-verifiable knowledge graph from 489 Springer math textbooks (GTM + UTM).
Models math knowledge management after apt (Debian package manager).

## Key Directories

- `mathpkg/` — Python package (graph, source, resolver, status, pipeline)
- `cmd/math` — CLI (8 commands)
- `concepts/` — Hand-curated knowledge (Phase 0, 21 group theory concepts)
- `lean/MathPkg/` — Lean 4 project depending on mathlib v4.31.0
- `pipeline_output/` — All automated pipeline outputs
  - `books/` — 414 extracted Markdown files
  - `concepts_v2/` — 20-book concept extraction
  - `dedup/` — Cross-book deduplication + Mathlib4 distance
  - `done_markers/` — .done/.fail files from Checker+Fixer
  - `checker.py` — Local compile checker (free, fast)
  - `phase2_input_49.json` — Batch 1 full input with gapfills
- `workflows/` — Claude Code Workflow scripts
  - `resilient_v4.js` — Stable Checker+Fixer pattern (use this for new batches)
  - `phase1_gapfill.js` — Gap-fill only (Phase 1)
- `tests/` — 28 unit tests

## Current State (2026-06-23)

- ✅ PDF: 409/489 extracted (298 MB)
- ✅ Concepts: 5,527 canonical (240 distance=1 ready to translate)
- ✅ Batch 1 Lean: 52 .lean files, ~60%+ compile pass (Checker+Fixer self-healing in progress)
- ✅ Resilient Workflow v4: Checker (local compile) + Fixer (Pro agent) with API retry
- ✅ 28/28 Python tests passing
- 🔜 Batch 2-5: 191 remaining distance=1 concepts
- 🔜 80 pure-scan books need local OCR (5060Ti)

## Critical Rules

### Lean 4
1. **Use `lake env lean`, NEVER bare `lean` or `lake build`** — `lake env lean` reuses 8175 cached .olean files
2. **`#check` doesn't work in compiled modules** — use `example` instead
3. **Parallel compile**: `ls *.lean | xargs -P 16 -I {} bash -c 'cd ../../ && lake env lean MathPkg/Pipeline/{} 2>&1'`
4. **Mathlib4 at**: `~/lean-demo/.lake/packages/mathlib/`
5. **Lean project**: `cd ~/文档/mathpkg/lean/MathPkg`

### DeepSeek API
1. **`max_tokens=393216` always** — thinking shares token budget, never limit
2. **Pro + thinking for math**, Flash for cheap tasks (classification, dedup)
3. **Network drops ~5s every ~5min** — every Workflow must handle API errors

### Workflow (Resilient v4 Pattern)
1. **Checker + Fixer, not monolithic** — local compile check (free) → Pro agent fix (only on failure)
2. **`agent()` throws on API error** — must `try-catch` inside retry loops
3. **Disk files are completion proof** — `.done`/`.fail` markers, never trust `agent()` return value
4. **Split into multiple Workflows for concurrency** — single cap ~16, 2-3 simultaneous = 30-48 real concurrent
5. **Never inline multi-line Python in JS prompts** — use external scripts (see `checker.py`)
6. **Don't use StructuredOutput** — DeepSeek agents fail to call it ~60% of the time

### Gap-fill + Translate Pipeline
1. **Phase 1 (gap-fill)**: Short prompt (~200 words), only expand proofs. QC after.
2. **Phase 2 (translate+compile+heal)**: Checker+Fixer pattern. Agent writes code, Checker compiles locally.
3. **Definitions skip Phase 1** — they just need correct `def`/`class`/`structure` in Phase 2

## API & Tools

- **DeepSeek V4**: Flash (¥1/¥2 per M) for cheap, Pro (¥3/¥6 per M) with thinking for math
- **Lean 4**: v4.31.0 at ~/.elan/bin
- **API Key**: sk-f9820c6cd6ff448d9f7f0d54a1411d28
- **Proxy**: http://127.0.0.1:7897 (clash-verge)

## Memory Files

See `/home/a123/.claude/projects/-home-a123----Springer-Math-Textbooks/memory/` for detailed records of:
- Architecture decisions (`architecture.md`)
- PDF extraction strategy (`pdf-extraction.md`)
- DeepSeek API best practices (`deepseek-api.md`)
- Lean 4 integration lessons (`lean-integration.md`)
- Claude subagent workflow patterns (`subagent-workflow.md`)
- Phase 0 lessons (`phase0-lessons.md`)
- **Resilient Workflow v4 pattern** (`resilient-workflow.md`) ← READ THIS FIRST
- **Batch 1 translation record** (`batch1-translation.md`) ← full strategy evolution

## Handover Doc

Full project status and next steps: `HANDOVER.md`
Technical documentation: `TECHNICAL.md`
