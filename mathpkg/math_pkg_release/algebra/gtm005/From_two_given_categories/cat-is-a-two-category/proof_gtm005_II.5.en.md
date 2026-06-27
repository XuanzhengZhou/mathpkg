---
role: proof
locale: en
of_concept: cat-is-a-two-category
source_book: gtm005
source_chapter: "II"
source_section: "5"
---

$\mathbf{Cat}$ is a 2-category with:
- 0-cells = small categories
- 1-cells = functors
- 2-cells = natural transformations

Horizontal composition: Given $\sigma: F \Rightarrow F': A \to B$ and $\tau: G \Rightarrow G': B \to C$, the horizontal composite $\tau \sigma: G \circ F \Rightarrow G' \circ F'$ has components $(\tau \sigma)_a = \tau_{F'(a)} \circ G(\sigma_a) = G'(\sigma_a) \circ \tau_{F(a)}$ (equal by naturality of $\tau$).

Vertical composition is componentwise. The interchange law $(\tau' \cdot \tau) \circ (\sigma' \cdot \sigma) = (\tau' \circ \sigma') \cdot (\tau \circ \sigma)$ follows from naturality, making $\mathbf{Cat}$ a strict 2-category.
