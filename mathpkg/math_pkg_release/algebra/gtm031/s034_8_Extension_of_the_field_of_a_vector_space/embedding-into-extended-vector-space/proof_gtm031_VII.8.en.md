---
role: proof
locale: en
of_concept: embedding-into-extended-vector-space
source_book: gtm031
source_chapter: "VII"
source_section: "8"
---

For each $x \in \mathfrak{R}$, define $\bar{x} = 1 \times x \in \mathfrak{R}_P = P \times \mathfrak{R}$. We verify that the map $\varphi: \mathfrak{R} \to \mathfrak{R}_P$ given by $\varphi(x) = \bar{x}$ is an injective $\Phi$-linear map, hence an equivalence (isomorphism) onto its image.

**$\Phi$-linearity**: For $x, y \in \mathfrak{R}$ and $\alpha \in \Phi$,
$$\varphi(x + y) = 1 \times (x + y) = 1 \times x + 1 \times y = \varphi(x) + \varphi(y),$$
$$\varphi(\alpha x) = 1 \times (\alpha x) = \alpha(1 \times x) = \alpha \varphi(x),$$
where we used the bilinearity of the Kronecker product and the fact that $\alpha \in \Phi \subseteq P$ acts as scalar multiplication in the $P$-component.

**Injectivity**: If $\bar{x} = 1 \times x = 0$ in $\mathfrak{R}_P$, then $x = 0$ in $\mathfrak{R}$ because the Kronecker product with the unit $1 \in P$ is non-degenerate.

Thus $\varphi$ is a $\Phi$-linear isomorphism between $\mathfrak{R}$ and its image $\bar{\mathfrak{R}} = \{\bar{x} : x \in \mathfrak{R}\}$, which is a subspace of $\mathfrak{R}_P$ over $\Phi$.
