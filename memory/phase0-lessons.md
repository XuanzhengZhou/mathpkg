---
name: phase0-lessons-learned
description: "What worked, what didn't, and key decisions from Phase 0"
metadata: 
  node_type: memory
  type: project
  originSessionId: bfc46d42-3656-4af8-b6a8-57278284f040
---

# Phase 0 — Lessons Learned

## What Worked

### 1. Hand-curated YAML (21 group theory concepts)
Writing 21 concepts by hand established the data model and proved the pipeline. Quality was excellent (100% descriptive names, 100% with deps, 100% with Lean mappings).

### 2. Copying apt's Architecture
Directly modeling sources.list, pkgCache, DepCache, and dpkg status saved weeks of design time. The mapping is nearly 1:1.

### 3. SQLite Cache
Simple, fast, zero-dependency. rebuild_from_dir() walks concept directories and populates the cache. 21 concepts in <1s.

### 4. LearningPathResolver (Kahn's Algorithm)
Topological sort with policy-based recommended/suggested insertion. Produces correct ordered learning paths. 0 cycles detected in the group theory graph.

### 5. fitz.get_text("text") for PDF Extraction
Discovered that pymupdf4llm fails on scanned+OCR PDFs (80% of our books). Switching to fitz.get_text("text") unlocked the hidden OCR layer. 409 books extracted in 8 minutes.

### 6. Per-Chapter Concept Extraction with Pro+Thinking
Splitting books into chapters, then extracting 8-15 chunks per chapter with Pro+thinking, yielded 611 concepts from GTM073 with 99% descriptive names and 77% with dependency info.

### 7. Multi-Strategy Mathlib4 Grep
Trying name variants (exact, underscores, PascalCase, camelCase, alphanumeric) found 734 matches vs 53 with exact-only grep.

### 8. Claude Subagent Workflow for Lean Translation
Agents that can read Mathlib4 source, understand Lean errors, and iteratively fix code were vastly superior to Python API pipelines. The Sylow theorems compiled after 3 manual API-name fixes.

## What Didn't Work

### 1. pymupdf4llm.to_markdown()
Returned empty image placeholders for scanned books. Only works on truly digital (vector) PDFs (~56% of collection).

### 2. Python self_heal.py with DeepSeek API
DeepSeek API doesn't understand Lean errors well enough to fix them. The self-heal loop ran 5-10 rounds without success. Claude subagents are the solution.

### 3. Whole-Book Concept Extraction (Flash, cheap)
Tried Flash model on whole books — got 1332 concepts but 0% had descriptive names (all "Theorem 2.3"). Pro+thinking per-chapter is necessary.

### 4. Serial Processing
The initial batch_translate.py processed concepts ONE AT A TIME within each batch. Each concept took 3-10 minutes. Switching to ThreadPoolExecutor fixed this.

### 5. Restrictive max_tokens
Setting max_tokens=4096 or 16384 caused thinking to consume all output tokens, leaving content empty. Fix: max_tokens=393216 (384K, essentially unlimited).

### 6. `lean` standalone command
Running `lean file.lean` recompiles ALL of Mathlib from scratch (hours). Always use `lake build` which reuses 8175 cached .olean files.

## Key Decisions

1. **Two-layer pipeline**: Gap-fill in natural language BEFORE Lean translation (solves the "obvious" gap problem)
2. **Mathlib4-first**: grep existing theorems, only write new ones when necessary
3. **Distance-based priority**: Concepts with all deps in Mathlib4 (distance=1) first, then cascade upward
4. **Phase 0 scope**: 21 concepts hand-curated, 20 books automated — enough to validate the full pipeline
5. **Claude subagents for Lean**: Superior to Python API pipelines because agents understand Lean errors

## Cost Summary (Phase 0)

| Task | Model | Cost |
|---|---|---|
| Quality classification (414 books) | Flash | ¥2 |
| Concept extraction (20 books) | Pro+Thinking | ¥40 |
| Cross-book dedup | Flash | ¥0.50 |
| Lean translation test (3 concepts) | Subagents | ¥0 (Claude tokens) |
| **Total** | | **~¥43** |
