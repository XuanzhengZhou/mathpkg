---
role: proof
locale: en
of_concept: braid-category-strict-monoidal
source_book: gtm005
source_chapter: "XI"
source_section: "4"
---

The braid category $\mathcal{B}$ has objects $n \in \mathbb{N}$ and $\mathcal{B}(n, n) = B_n$ (braid group on $n$ strands), with no morphisms between different objects. Composition is group multiplication.

Strict monoidal structure: $n \otimes m = n + m$. For $\beta \in B_n$, $\beta' \in B_m$, the tensor product $\beta \otimes \beta' \in B_{n+m}$ is the braid obtained by placing $\beta$ and $\beta'$ side-by-side (disjoint union). This is the group homomorphism $B_n \times B_m \to B_{n+m}$.

The braiding $\gamma_{m,n}: m+n \to n+m$ is the element of $B_{m+n}$ crossing the first $m$ strands over the last $n$ strands. The hexagon axioms and naturality reduce to braid relations in $B_{m+n+p}$, which hold by definition. $\mathcal{B}$ is the free braided strict monoidal category on one generating object $1$.
