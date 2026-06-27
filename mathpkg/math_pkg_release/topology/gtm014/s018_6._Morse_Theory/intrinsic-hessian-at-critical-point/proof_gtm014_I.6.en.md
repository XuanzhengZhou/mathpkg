---
role: proof
locale: en
of_concept: intrinsic-hessian-at-critical-point
source_book: gtm014
source_chapter: "I"
source_section: "§6. Morse Theory"
---

Let $U$ be a nbhd of $p$ in $X$ and $\phi: U \to \mathbf{R}^n$ a chart centered at $p$. Let $U' = \phi(U)$ and $g = f \circ \phi^{-1}$. By Lemma (B) above, $0$ is a critical point of $g$ and $(d^2 f)_p = (d^2 \phi^* g)_p = \phi^* (d^2 g)_0$. By Lemma (A), $(d^2 g)_0$ is symmetric. Hence $(d^2 f)_p$ is symmetric.

By Proposition 6.4, $0$ is a nondegenerate critical point of $g$ iff $(d^2 g)_0$ is a nondegenerate bilinear form iff $(d^2 f)_p$ is a nondegenerate bilinear form, since $(d\phi)_p: T_p X \to T_0 \mathbf{R}^n$ is an isomorphism.

Finally the diagram

$$
J^1(U, \mathbf{R}) \xrightarrow{(\phi^*)^{-1}} J^1(U', \mathbf{R})
$$

commutes and $\phi^*(S_1) = S_1$, establishing the invariance of the Hessian and its nondegeneracy under coordinate changes.
