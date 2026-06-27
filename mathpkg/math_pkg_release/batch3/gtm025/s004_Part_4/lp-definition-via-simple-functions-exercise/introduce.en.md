---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Let $(X, \mathcal{A}, \mu)$ be a measure space and let $f$ be a complex-valued $\mathcal{A}$-measurable function on $X$. Prove that $f \in \mathfrak{L}_1(X, \mathcal{A}, \mu)$ if and only if there exists a sequence $(s_n)$ of simple functions such that $(s_n) \subset \mathfrak{L}_1$, $s_n \to f$ in measure, and

$$\lim_{m, n \to \infty} \int_X |s_m - s_n| d\mu = 0.$$

In this case we have

$$\int_X f d\mu = \lim_{n \to \infty} \int_X s_n d\mu.$$

[If one first defines $\int_X s d\mu$ for complex-valued, $\mathcal{A}$-measurable, simple functions, then the above facts can be used to define $\mathfrak{L}_1$ and the integral on $\mathfrak{L}_1$. This approach is useful when dealing with functions with values in a Banach space. It does not depend on the order properties of the real numbers.]
