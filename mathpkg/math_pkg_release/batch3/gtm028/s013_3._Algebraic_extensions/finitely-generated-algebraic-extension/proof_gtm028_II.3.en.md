---
role: proof
locale: en
of_concept: finitely-generated-algebraic-extension
source_book: gtm028
source_chapter: "II"
source_section: "3. Algebraic extensions"
---

We proceed by induction on $n$.

For $n = 1$, $x_1$ is algebraic over $k$, so $k(x_1)$ is a simple algebraic extension. By the corollary of Theorem 4, $k(x_1)$ is a finite extension of $k$, i.e., $[k(x_1) : k] = m_1 < \infty$, and hence $k(x_1)$ is algebraic over $k$.

Assume the statement holds for $n - 1$ elements. Each $x_i$, being algebraic over $k$, is a fortiori algebraic over $k(x_1, x_2, \ldots, x_{i-1})$. Hence $k(x_1, x_2, \ldots, x_i)$ is a simple algebraic extension of $k(x_1, x_2, \ldots, x_{i-1})$, and therefore
$$[k(x_1, x_2, \ldots, x_i) : k(x_1, x_2, \ldots, x_{i-1})] = m_i$$
is a finite integer $\geq 1$ (by the corollary of Theorem 4). Applying the multiplicativity relation (2) repeatedly,
$$[k(x_1, x_2, \ldots, x_n) : k] = \prod_{i=1}^{n} m_i < \infty.$$
Thus $k(x_1, x_2, \ldots, x_n)$ has finite degree over $k$. By Theorem 4, it is an algebraic extension of $k$.
