---
role: proof
locale: en
of_concept: gauss-map-implies-riemannian-metric
source_book: gtm020
source_chapter: "9"
source_section: "9.5"
---

Let $g: E(\xi) \to F^\infty$ be a Gauss map for the vector bundle $\xi$. Recall that $g$ is a continuous map that is a linear monomorphism when restricted to each fibre of $\xi$.

Define $\beta: E(\xi \oplus \xi) \to F$ by the relation
$$\beta(x, x') = (g(x) \mid g(x'))$$
where $(\cdot \mid \cdot)$ denotes the standard Euclidean inner product on $F^\infty$.

Since $g$ is a monomorphism on each fibre, the restriction of $\beta$ to each fibre is an inner product. Specifically, for points $x, x'$ in the same fibre:
- Linearity in the first argument follows from the linearity of $g$ on each fibre and the bilinearity of the Euclidean inner product.
- Conjugate-linearity in the second argument follows similarly.
- Continuity follows from the continuity of $g$ and the continuity of the Euclidean inner product.

Thus $\beta$ is a riemannian metric when $F = \mathbf{R}$ and a hermitian metric when $F = \mathbf{C}$.
