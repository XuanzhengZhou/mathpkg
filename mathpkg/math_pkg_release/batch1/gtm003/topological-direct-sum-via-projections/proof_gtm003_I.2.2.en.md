---
role: proof
locale: en
of_concept: topological-direct-sum-via-projections
source_book: gtm003
source_chapter: "I. Topological Vector Spaces"
source_section: "2.2"
---

**Proof.** By definition of the product topology, the mapping $\psi^{-1}: x \mapsto (u_1 x, \ldots, u_n x)$ of $L$ onto $\prod_i M_i$ is continuous if and only if each $u_i$ is continuous. The algebraic direct sum isomorphism $\psi: \prod_i M_i \to L$, $(x_1, \ldots, x_n) \mapsto x_1 + \cdots + x_n$ is always continuous (by continuity of addition). Thus $L = M_1 \oplus \cdots \oplus M_n$ (meaning $\psi$ is a homeomorphism) if and only if $\psi^{-1}$ is continuous, i.e., each $u_i$ is continuous.
