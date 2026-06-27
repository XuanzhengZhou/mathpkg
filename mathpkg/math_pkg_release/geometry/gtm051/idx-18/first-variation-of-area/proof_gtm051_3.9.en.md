---
role: proof
locale: en
of_concept: first-variation-of-area
source_book: gtm051
source_chapter: "3"
source_section: "3.9.6"
---

Consider a family $f^\epsilon(u) = f(u) + \epsilon a(u)n(u)$ of surfaces neighboring $f$. Here $\epsilon$ lies in an interval containing $0$ and $a: U \to \mathbb{R}$ is a smooth function. For sufficiently small $\epsilon$, $f^\epsilon$ is a regular surface and we may define its first fundamental form.

Compute the derivative $f_i^\epsilon = f_i + \epsilon a_i n + \epsilon a n_i$. Then
$$g_{ik}^\epsilon = f_i^\epsilon \cdot f_k^\epsilon = (f_i + \epsilon a_i n + \epsilon a n_i) \cdot (f_k + \epsilon a_k n + \epsilon a n_k).$$

Using $f_i \cdot n = 0$, $n \cdot n = 1$, and $f_i \cdot n_k = -h_{ik}$ (from the Weingarten equations), we obtain up to first order in $\epsilon$:
$$g_{ik}^\epsilon = g_{ik} - 2\epsilon a h_{ik}.$$

For the determinant, using the expansion $\det(I + \epsilon A) = 1 + \epsilon \operatorname{tr}(A) + O(\epsilon^2)$, we have
$$g^\epsilon = \det(g_{ik}^\epsilon) = \det(g_{ik}) \det(\delta_{ik} - 2\epsilon a g^{il} h_{lk}) = g(1 - 2\epsilon a \sum_{i,l} g^{il} h_{li}).$$

Since $\sum_{i,l} g^{il} h_{li} = \operatorname{tr}(g^{-1}h) = 2H$ (the mean curvature), we get
$$g^\epsilon = g(1 - \epsilon \cdot 4aH).$$

Therefore
$$\sqrt{g^\epsilon} = \sqrt{g} \sqrt{1 - 4\epsilon aH} = \sqrt{g}(1 - 2\epsilon aH + O(\epsilon^2)),$$
and
$$\left. \frac{\partial \sqrt{g^\epsilon}}{\partial \epsilon} \right|_{\epsilon=0} = -2aH\sqrt{g}.$$

For the area functional $A(\epsilon) = \int_U \sqrt{g^\epsilon} \, du^1 du^2$, we have
$$A'(0) = \int_U \left. \frac{\partial \sqrt{g^\epsilon}}{\partial \epsilon} \right|_{\epsilon=0} du^1 du^2 = -2 \int_U aH \sqrt{g} \, du^1 du^2.$$

Thus $A'(0) = 0$ for all smooth functions $a$ with compact support if and only if $H \equiv 0$.
