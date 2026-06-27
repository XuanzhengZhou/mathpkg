---
role: proof
locale: en
of_concept: tychonoff-space-embedding-theorem
source_book: gtm027
source_chapter: "5"
source_section: "Products of Compact Spaces"
---

# Proof of Tychonoff Space Embedding Theorem

**Theorem.** A topological space is a Tychonoff space if and only if it is homeomorphic to a subspace of a compact Hausdorff space.

*Proof.* ($\Rightarrow$) By Theorem 4.6, each Tychonoff space is homeomorphic to a subset of a cube (a product of closed unit intervals). The closed unit interval $[0, 1]$ is compact, and by Tychonoff's theorem the product of compact spaces is compact. Moreover, a product of Hausdorff spaces is Hausdorff. Hence the cube is a compact Hausdorff space. Therefore each Tychonoff space is homeomorphic to a subspace of a compact Hausdorff space.

($\Leftarrow$) Every compact Hausdorff space is normal (compactness implies every closed subset is compact, and in a Hausdorff space disjoint compact sets can be separated by disjoint open sets). Consequently, by Urysohn's lemma (Theorem 4.4), every compact Hausdorff space is completely regular and $T_1$, that is, a Tychonoff space. Each subspace of a Tychonoff space is a Tychonoff space (the separation axioms are hereditary). Therefore any space homeomorphic to a subspace of a compact Hausdorff space is a Tychonoff space. $\square$
