---
name: concept-format-v3
description: "V3 concept folder: multi-file with manifest.yaml. Each aspect its own .md. Multi-book support."
metadata: 
  node_type: memory
  type: project
  originSessionId: 32b0208b-f009-4db0-9b54-c8a7af2b3275
---

# Concept Format V3 — Portfolio Design (2026-06-24)

## Core Idea

A concept is a **folder**, not a file. Every aspect of the concept gets its own `.md` file.
A `manifest.yaml` config file organizes them all.

## Folder Structure

```
concepts/algebra/group_theory/lagrange/
├── manifest.yaml              ← config: primary file, optional files, deps, Lean
├── gtm0073_introduce.md       ← Hungerford's introduction to the concept
├── gtm0073_proof.md           ← Hungerford's proof
├── gtm0073_exercise.md        ← exercises from Hungerford
├── gtm0080_introduce.md       ← Robinson's introduction
├── gtm0080_proof.md           ← Robinson's proof (different approach)
├── gtm0148_introduce.md       ← Rotman's introduction
├── gtm0148_exercise.md        ← exercises from Rotman
├── lagrange_theorem.lean      ← Lean 4 formal verification
├── dependency_graph.md        ← auto-generated dependency DAG
└── _compiled/                 ← auto-generated: merged encyclopedia page
    └── lagrange_theorem.md    ← the full page stitched from all sources
```

## manifest.yaml

```yaml
id: lagrange_theorem
name: {en: "Lagrange's Theorem", zh: "拉格朗日定理"}
type: theorem
topic: group-theory

# Primary source (first book to introduce this concept)
primary: gtm0073_introduce.md

# All source files in priority order
sources:
  - gtm0073_introduce.md
  - gtm0073_proof.md
  - gtm0073_exercise.md
  - gtm0080_introduce.md
  - gtm0080_proof.md
  - gtm0148_introduce.md
  - gtm0148_exercise.md

# Auto-generated merged output
compiled: _compiled/lagrange_theorem.md

# Dependencies
depends:
  required: [subgroup, coset]
  recommended: [group_action]

# Lean formalization
lean:
  file: lagrange_theorem.lean
  mathlib4_path: Mathlib.GroupTheory.Coset.Card
  status: complete
```

## Why This Design

| Before (v2) | After (v3) |
|---|---|
| One .md per concept, all sources embedded | One .md per source, clean separation |
| Adding new book = editing large .md | Adding new book = adding a file |
| Merge conflicts when two agents add versions | Each source is a separate file — no conflicts |
| Hard to reference "just Robinson's proof" | Direct file link: `gtm0080_proof.md` |

## Auto-compilation

Python script reads `manifest.yaml` → finds all source files → compiles `_compiled/lagrange_theorem.md` with all sections merged.

This is deterministic and free — no API call needed.

## Related
- [[concept-format-v2]] — previous three-file format (superseded)
- [[file-spec.md]] — naming conventions
