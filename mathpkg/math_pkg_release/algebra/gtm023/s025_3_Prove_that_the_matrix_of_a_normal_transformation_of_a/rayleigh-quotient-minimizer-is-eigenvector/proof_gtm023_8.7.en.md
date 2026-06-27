---
role: proof
locale: en
of_concept: rayleigh-quotient-minimizer-is-eigenvector
source_book: gtm023
source_chapter: "VIII"
source_section: "8.7"
---

Let $e_1$ be a unit vector minimizing $F$ on the unit sphere. For an arbitrary vector $y$, define
$$f(t) = F(e_1 + ty) = \frac{(e_1 + ty, \varphi e_1 + t\varphi y)}{(e_1 + ty, e_1 + ty)}.$$
Since $f$ attains a minimum at $t = 0$, we have $f'(0) = 0$. Differentiating the quotient:
$$f'(t) = \frac{(y, \varphi e_1 + t\varphi y) + (e_1 + ty, \varphi y)}{(e_1 + ty, e_1 + ty)} - \frac{(e_1 + ty, \varphi e_1 + t\varphi y) \cdot 2(e_1 + ty, y)}{(e_1 + ty, e_1 + ty)^2}.$$
At $t = 0$, using $(e_1, e_1) = 1$:
$$f'(0) = (y, \varphi e_1) + (e_1, \varphi y) - 2(e_1, \varphi e_1)(e_1, y).$$
Since $\varphi$ is selfadjoint, $(e_1, \varphi y) = (\varphi e_1, y) = (y, \varphi e_1)$, hence:
$$f'(0) = 2(\varphi e_1, y) - 2(e_1, \varphi e_1)(e_1, y) = 2(\varphi e_1 - (e_1, \varphi e_1)e_1, \; y).$$
Setting $f'(0) = 0$ for every $y \in E$ yields $\varphi e_1 - (e_1, \varphi e_1)e_1 = 0$, i.e. $\varphi e_1 = (e_1, \varphi e_1)e_1$. Thus $e_1$ is an eigenvector with eigenvalue $\lambda_1 = (e_1, \varphi e_1)$.
