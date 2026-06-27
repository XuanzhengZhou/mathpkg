---
role: proof
locale: en
of_concept: basis-cardinality-invariance
source_book: gtm031
source_chapter: "1"
source_section: "2"
---

Let $e_1, e_2, \cdots, e_n$ be one basis and let $f_1, f_2, \cdots, f_m$ be another basis of $\mathfrak{R}$.

Since the $e_i$ form a basis, they are generators. Any $f_j$ can be expressed as a linear combination $\sum \xi_i e_i$. Moreover, the $f_j$ are linearly independent; indeed, if $\sum \beta_j f_j = 0$, writing each $f_j$ in terms of the $e_i$ gives a linear relation among the $e_i$, forcing all coefficients to vanish by the uniqueness of representation.

By Theorem 2, a space with an $n$-element basis cannot contain $n+1$ linearly independent vectors, so $m \leq n$. Reversing the roles of the two bases gives $n \leq m$. Hence $m = n$.

Thus the number of elements in any basis is uniquely determined. This number is the \textbf{dimensionality} of $\mathfrak{R}$ over $\Delta$.

Equivalent vector spaces have the same dimensionality. In particular, the spaces $\Delta^{(m)}$ and $\Delta^{(n)}$ are equivalent if and only if $m = n$.
