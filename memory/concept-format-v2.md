---
name: concept-format-v2
description: "Final concept format: three files per concept — markdown, lean, yaml. apt-inspired."
metadata: 
  node_type: memory
  type: project
  originSessionId: 32b0208b-f009-4db0-9b54-c8a7af2b3275
---

# Concept Format v2 (2026-06-23)

Each concept is a directory with exactly three files:

```
concepts/algebra/group_theory/lagrange/
├── lagrange.md     ← Natural language proof, cross-book comparison, discussion
├── lagrange.lean   ← Lean 4 formal verification, lake build compilable
└── concept.yaml    ← Dependencies, source books, versions (apt control file)
```

## Rationale

- **markdown** is for humans — the proof, the comparison across textbooks, the pedagogical discussion
- **lean** is for the compiler — verification that the markdown proof is correct
- **yaml** is for the package manager — dependency resolution, source tracking, versioning

Nothing else is needed. All other files are auto-generated: `index.yaml` (Packages.gz), `graph.db` (pkgCache), `~/.mathpkg/status.yaml` (dpkg status).

## concept.yaml (apt control file)

```yaml
id: lagrange_theorem
name: {en: "Lagrange's Theorem", zh: "拉格朗日定理"}
type: theorem

depends:
  required: [subgroup, coset]
  recommended: [group_action]

versions:
  - source: GTM073, author: Hungerford, chapter: I.4, pages: 38-42
  - source: GTM080, author: Robinson, chapter: 1.3, pages: 15-17
  - source: GTM148, author: Rotman, chapter: 2.4, pages: 34-36

lean:
  mathlib4_path: Mathlib.GroupTheory.Coset.Card
  mathlib4_theorem: Subgroup.card_subgroup_dvd_card
  status: complete  # none | partial | complete
```

## lagrange.md

Natural language. Cross-reference multiple textbooks' approaches. Every proof step links to a Lean block.
Readable by a mathematician without any Lean knowledge.

## lagrange.lean

Compilable Lean 4 code. Imports Mathlib. Uses `lake build`.
The code is embedded in the markdown but also standalone for verification.

## Automatic Generation

Use DeepSeek Flash to generate markdown pages from concept JSON + textbook extracts.
Use DeepSeek Pro for Lean proof blocks.
Total cost for 5,527 concepts: ~¥22 (Flash markdown) + ~¥2,000 (Pro Lean proofs).
