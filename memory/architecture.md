---
name: project-architecture
description: mathpkg project design — apt-inspired math knowledge package manager
metadata: 
  node_type: memory
  type: project
  originSessionId: bfc46d42-3656-4af8-b6a8-57278284f040
---

# mathpkg Architecture

## Core Insight

Math knowledge management is isomorphic to software package management. We copy apt's architecture directly.

## apt → mathpkg Mapping

| apt component | mathpkg equivalent | Status |
|---|---|---|
| sources.list | sources.yaml (per-source concept index) | ✅ Phase 0 |
| Packages.gz | index.yaml (per-topic concept listing) | ✅ Phase 0 |
| pkgCache (mmap binary) | SQLite (concepts + dependencies + versions) | ✅ Phase 0 |
| DepCache | UserState (mastered/learning/stuck) | ✅ Phase 0 |
| SAT Solver | LearningPathResolver (Kahn topological sort) | ✅ Phase 0 |
| dpkg status | ~/.mathpkg/status.yaml | ✅ Phase 0 |
| apt-get install | math install <concept> → learning path | ✅ Phase 0 |
| Transport Methods | GitAdapter, ArxivAdapter, LocalAdapter | 🔜 Phase 1 |

## Project Structure

```
mathpkg/
├── cmd/math                    # CLI (source, update, show, install, mark, status, verify, lean)
├── mathpkg/
│   ├── graph/                  # Knowledge graph (concept.py, cache.py)
│   ├── source/                 # Source management (source_list.py, index.py)
│   ├── resolver/               # Dependency resolution (solver.py, policy.py)
│   ├── status/                 # User state (user_state.py)
│   └── pipeline/               # Automated pipeline
│       ├── deepseek_client.py  # DeepSeek V4 API (Flash + Pro, thinking mode)
│       ├── gap_fill.py         # Layer 1: expand proof sketches
│       ├── lean_translate.py   # Layer 2: proof → Lean 4
│       ├── self_heal.py        # Layer 3-4: compile + fix with lake build
│       └── orchestrator.py     # Full pipeline coordinator
├── concepts/                   # Hand-curated knowledge (Phase 0)
│   └── algebra/group_theory/
│       ├── index.yaml          # 21 concepts
│       └── nodes/*.yaml
├── lean/MathPkg/               # Lean 4 project
│   ├── lakefile.toml           # depends on mathlib v4.31.0
│   └── MathPkg/Algebra/Group/
│       └── Pipeline.lean       # Compilable Lean theorems
├── pipeline_output/            # Automated pipeline outputs
│   ├── books/                  # 414 MD files extracted from PDFs
│   │   ├── _extractable.json   # 409 books with text layers
│   │   ├── _no_text.json       # 80 books needing OCR
│   │   └── _full_quality.json  # 414-book quality classification
│   ├── concepts_v2/            # 20-book concept extraction (5779 concepts)
│   │   └── book_*.json
│   ├── dedup/                  # Cross-book deduplication
│   │   ├── canonical_concepts.json     # 5527 canonical concepts
│   │   ├── canonical_with_distance.json  # with Mathlib4 distance
│   │   └── mathlib4_coverage.json       # grep results
│   ├── graph/
│   │   └── dependency_graph.json  # Layered dependency graph
│   └── translations/           # Lean translation results
│       └── _checkpoint.json
├── tests/                      # 28 unit tests, all passing
├── sources.yaml                # Default source config
└── PHASE1.md                   # Phase 1 design (two-layer pipeline)
```

## Key Design Decisions

1. **Copy apt, don't invent**: sources.list pattern, dependency resolution, transaction support all directly modeled
2. **Python stdlib + SQLite**: No frameworks, minimal dependencies
3. **YAML concept format**: Human-readable, LLM-friendly, version-controllable
4. **Two-layer pipeline**: Gap-fill in natural language BEFORE Lean translation
5. **Mathlib4-first**: grep existing theorems before writing new ones
