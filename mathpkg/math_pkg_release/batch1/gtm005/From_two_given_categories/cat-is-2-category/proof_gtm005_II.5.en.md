---
role: proof
locale: en
of_concept: cat-is-2-category
source_book: gtm005
source_chapter: "II"
source_section: "5"
---

The 2-categorical structure of $\mathbf{Cat}$ is verified by checking that $\mathbf{Cat}(A, B) = B^A$ is a category (functors as objects, natural transformations as morphisms, vertical composition), and horizontal composition is a bifunctor:
$$\circ: \mathbf{Cat}(B, C) \times \mathbf{Cat}(A, B) \to \mathbf{Cat}(A, C).$$

For natural transformations $\sigma: F \Rightarrow F': A \to B$ and $\tau: G \Rightarrow G': B \to C$, define $\tau \circ \sigma: G \circ F \Rightarrow G' \circ F'$ by $(\tau \circ \sigma)_a = G'(\sigma_a) \circ \tau_{F(a)}$. This is natural and satisfies the bifunctor axioms: $1_G \circ 1_F = 1_{G \circ F}$, and horizontal composition is associative and respects vertical composition (interchange law).
