---
role: proof
locale: en
of_concept: braid-group-relations
source_book: gtm005
source_chapter: "XI"
source_section: "4"
---

The Artin braid group $B_n$ is presented by generators $\sigma_1, \ldots, \sigma_{n-1}$ and relations:

1. $\sigma_i \sigma_j = \sigma_j \sigma_i$ for $|i-j| > 1$ (far commutativity).
2. $\sigma_i \sigma_{i+1} \sigma_i = \sigma_{i+1} \sigma_i \sigma_{i+1}$ for $1 \leq i \leq n-2$ (braid relation).

Proof of sufficiency: Geometrically, $\sigma_i$ represents the elementary crossing of strand $i$ over strand $i+1$. Any braid decomposes as a sequence of such crossings. Relation (1) reflects that crossings of disjoint pairs of strands can be done independently. Relation (2) reflects the type-III Reidemeister move in knot theory: sliding one strand over a crossing of two others.

These relations exactly match the coherence conditions of a braided monoidal category: naturality of the braiding gives far commutativity, and the hexagon axioms give the braid relation.
