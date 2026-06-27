---
role: proof
locale: en
of_concept: jacobian-matrix-of-differential
source_book: gtm051
source_chapter: "0"
source_section: "0.3"
---

From the definition of differentiability, for $x = x_0 + h$ with $h \to 0$,

$$F(x_0 + h) - F(x_0) = dF_{x_0}(h) + o(|h|).$$

Let $h = t e_j$ where $e_j$ is the $j$-th standard basis vector and $t \to 0$. Then

$$\frac{F(x_0 + t e_j) - F(x_0)}{t} = dF_{x_0}(e_j) + \frac{o(|t|)}{t}.$$

Taking the limit $t \to 0$, the left side is precisely the partial derivative $\frac{\partial F}{\partial x^j}(x_0)$. The $o(|t|)/t$ term vanishes, yielding

$$dF_{x_0}(e_j) = \frac{\partial F}{\partial x^j}(x_0) = \left( \frac{\partial F^1}{\partial x^j}(x_0), \ldots, \frac{\partial F^m}{\partial x^j}(x_0) \right)^\top.$$

The $j$-th column of the matrix of $dF_{x_0}$ is $dF_{x_0}(e_j)$, so the matrix is indeed the Jacobian matrix $(\partial F^i / \partial x^j)(x_0)$.
