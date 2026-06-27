---
role: proof
locale: en
of_concept: hessian-symmetric-bilinear-nondegenerate
source_book: gtm014
source_chapter: "6"
source_section: "6. Morse Theory"
---

Let $U$ be a neighborhood of $p$ in $X$ and $\phi: U \to \mathbb{R}^n$ a chart centered at $p$. Let $U' = \phi(U)$ and $g = f \circ \phi^{-1}$. By Lemma (B), $0$ is a critical point of $g$ and
$$(d^2 f)_p = (d^2(\phi^* g))_p = \phi^*(d^2 g)_0.$$
By Lemma (A), $(d^2 g)_0$ is symmetric. Hence $(d^2 f)_p$ is symmetric.

By Proposition 6.4, $0$ is a nondegenerate critical point of $g$ iff $(d^2 g)_0$ is a nondegenerate bilinear form. Since $(d\phi)_p: T_p X \to T_0 \mathbb{R}^n$ is an isomorphism, $(d^2 f)_p$ is nondegenerate iff $(d^2 g)_0$ is nondegenerate iff $p$ is a nondegenerate critical point of $f$.
