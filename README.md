# mathpkg — Mathematical Knowledge Graph & Formal Verification Engine

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.12+-green.svg)](https://python.org)
[![Lean](https://img.shields.io/badge/Lean-4.31.0-orange.svg)](https://lean-lang.org/)

A dependency-aware mathematical knowledge graph with automated theorem extraction and Lean 4 formal verification via Mathlib4. Inspired by apt package management: mathematical concepts are packages, dependencies are edges, and topological sort generates learning paths.

## ✨ Key Features

- **Structured Concept Extraction** — LLM-powered extraction of theorems, definitions, and lemmas into machine-readable YAML + pure LaTeX + natural language triples
- **4-Tier Structural Analysis** — regex → heuristic detection → semantic analysis → adaptive chunking. Discovered consistent page-to-section ratio across diverse materials (94% automated)
- **Mathlib4 Semantic Matching** — Index of 204,000 theorems/definitions. 3-tier inverted index achieves **71.6% automatic match rate** via keyword + type-signature + domain filtering
- **Resilient Batch Processing** — Adaptive batch sizing with stepwise degradation, checkpoint-based recovery, and automated health monitoring

## 🏗 Architecture

```
Source materials
  ↓ [Structural analysis: regex → heuristics → LLM semantics → adaptive]
Structured chunks (~optimal size for downstream processing)
  ↓ [LLM agent, per-chunk parallel]
Concept triples: concept.yaml + theorem.tex + introduce.en.md
  ↓ [Dedup + dependency resolution]
Knowledge graph (graph.db, apt-inspired pkgCache)
  ↓ [Mathlib4 inverted index matching, 71.6% hit rate]
Lean 4 formal verification code
```

## 📊 v1 Release (2026-06-27)

| Metric | Count |
|---|---|
| **Books processed** | 62 |
| **Concepts extracted** | 27,855 |
| **Proofs extracted** | 13,494 |
| **Exercises extracted** | 6,500+ |
| **Total size** | 538 MB |
| **Format** | 5 files/concept: concept.yaml + theorem.tex + introduce.en.md + proof + exercise |

### By Domain

| Domain | Books | Concepts | Proofs |
|---|---|---|---|
| Algebra | 15 | 6,582 | 2,930 |
| Analysis | 13 | 6,695 | 3,329 |
| Topology | 8 | 3,344 | 1,611 |
| Geometry | 5 | 2,219 | 987 |
| Number Theory | 6 | 2,188 | 1,140 |
| Probability | 6 | 1,861 | 1,114 |
| Logic | 3 | 1,697 | 758 |
| Foundations | 2 | 1,305 | 764 |
| Applied Math | 2 | 1,078 | 484 |
| Combinatorics | 1 | 886 | 377 |

## 🚀 Quick Start

```bash
pip install -r requirements.txt

# Structural analysis
python3 pipeline_output/stitch_by_section.py

# Concept extraction (requires DeepSeek API key)
export DEEPSEEK_API_KEY="sk-..."
# Launch per-section workflow: workflows/v7_book_extract_v3.js

# Mathlib4 matching
python3 pipeline_output/grep_mathlib4.py

# Health monitoring
python3 pipeline_output/ocr_healthcheck.py
```

## 📁 Repo Structure

| Directory | Content |
|---|---|
| `mathpkg/` | Core library: graph DB, dependency resolver, source management |
| `mathpkg/math_pkg_release/` | 🔥 **v1 Release**: 27,855 concepts by domain (algebra, analysis, topology, etc.) |
| `cmd/` | CLI tool |
| `workflows/` | Agent workflow scripts for parallel concept extraction |
| `tests/` | Unit tests |
| `concepts/` | Hand-curated reference concepts |
| `lean/MathPkg/` | Lean 4 project with verified theorems |
| `BATCH_TRACE.yaml` | Batch provenance for every concept |

## 🔬 Key Findings

1. **Optimal chunk size is predictable** — structural units follow a consistent size ratio across diverse materials
2. **Semantic chunking beats coarse splitting** — fine-grained structural units avoid LLM output truncation
3. **Inverted index outperforms exact matching** — name-based matching hits only 1%; keyword + type-signature matching reaches 69%
4. **Adaptive fallback is essential** — stepwise resource degradation maintains near-maximum utilization under varying load

## 📝 License

MIT
