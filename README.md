# mathpkg — Mathematical Knowledge Graph & Formal Verification Pipeline

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.12+-green.svg)](https://python.org)
[![Lean](https://img.shields.io/badge/Lean-4.31.0-orange.svg)](https://lean-lang.org/)

Automated extraction of theorems, definitions, and lemmas from 1,565 Springer math textbooks (GTM, UTM, UTX, SMM), organized into a dependency-aware knowledge graph with Lean 4 formal verification via Mathlib4.

## ✨ Key Features

- **Mass-Scale Concept Extraction** — 6,374 concepts from 10 test books (avg ¥8/book), each with structured YAML metadata + pure LaTeX statements + natural language introductions
- **4-Tier Section Splitting** — regex → chapter detection → Flash semantic analysis → size fallback. Discovered **~10 pages/section** natural law across all textbooks (94% automated)
- **Mathlib4 Matching** — Built index of 204,000 theorems/definitions. 3-tier inverted index achieves **71.6% automatic match rate** (keyword + signature + domain filtering)
- **Local GPU OCR** — GLM-OCR on RTX 5060Ti with adaptive batch sizing (16→1 fallback), checkpointing, and health monitoring

## 🏗 Architecture

```
Springer PDFs (1,565 books)
  ↓ [GLM-OCR, local GPU, batch=16 adaptive]
Per-page OCR JSON → Section .md files (~10pp each)
  ↓ [DeepSeek Pro Agent, per-section parallel]
Concept files (concept.yaml + theorem.tex + introduce.en.md)
  ↓ [Dedup + dependency resolution]
Knowledge graph (graph.db, apt-inspired pkgCache)
  ↓ [Mathlib4 inverted index matching, 71.6% hit]
Lean 4 verification code
```

## 📊 Current Progress

| Milestone | Status |
|---|---|
| OCR (GTM series) | 303/305 books done |
| OCR (UTM series) | 5/219 books, ~4/hr |
| Section splitting | 131 books, 4,482 chunks |
| Concept extraction test | 10 books, 6,374 concepts |
| Mathlib4 index | 204K entries, 50.9MB |
| Lean translation | Pending |

## 🚀 Quick Start

```bash
pip install -r requirements.txt

# Section splitting
python3 pipeline_output/stitch_by_section.py --book "GTM"
python3 pipeline_output/stitch_chapters_v2.py       # chapter fallback

# Concept extraction (requires DeepSeek API key)
export DEEPSEEK_API_KEY="sk-..."
# Launch workflow per book: workflows/v7_book_extract_v3.js

# Mathlib4 matching
python3 pipeline_output/grep_mathlib4.py

# OCR health check
python3 pipeline_output/ocr_healthcheck.py
```

## 📁 Repo Structure

| Directory | Content |
|---|---|
| `mathpkg/` | Core: graph DB, resolver, source management, pipeline |
| `cmd/` | CLI tool (`math source/update/show/install/mark`) |
| `pipeline_output/` | Python tools + concept extraction results |
| `workflows/` | Agent workflow scripts (Claude Code Workflow) |
| `tests/` | 28 unit tests |
| `docs/` | V7 specification (file format, agent prompts) |
| `concepts/` | Hand-curated group theory concepts (Phase 0) |
| `lean/MathPkg/` | Lean 4 project with skeletons and verified theorems |

## 🔬 Key Findings

1. **Pages per section ≈ 10** — remarkably stable across 131 textbooks, regardless of length
2. **Section > Chapter** — ~10-page chunks optimal for LLM processing; chapters (30-60pp) cause output truncation
3. **Inverted index beats exact grep** — name-based matching only 1%; keyword + signature matching achieves 69%
4. **OOM requires adaptive fallback** — batch=16→1 stepwise degradation keeps GPU near 100%

## 📝 License

MIT
