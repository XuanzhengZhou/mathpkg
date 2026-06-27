---
role: proof
locale: en
of_concept: indiscrete-topology-right-adjoint
source_book: gtm005
source_chapter: "IV. Adjoints"
source_section: "9. Adjoints in Topology"
---

The adjunction $G \dashv D'$ is established by the natural bijection

$$\mathbf{Set}(GX, S) \cong \mathbf{Top}(X, D'S).$$

Given a set $S$, any set function $f: GX \to S$ lifts uniquely to a continuous map $\tilde{f}: X \to D'S$ because every function into an indiscrete space is continuous — the only open sets in $D'S$ are $\emptyset$ and $D'S$, whose preimages under any function are $\emptyset$ and $X$, both open in $X$. Thus $G$ is left adjoint to $D'$. As a left adjoint, $G$ preserves all colimits (dual of Theorem 1, Section 3).
