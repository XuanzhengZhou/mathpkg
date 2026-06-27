---
role: proof
locale: en
of_concept: zeta-m-pole-and-l-nonvanishing
source_book: gtm007
source_chapter: "VI"
source_section: "3"
---

If $L(1, \chi) \neq 0$ for all $\chi \neq 1$, then since $L(s,1)$ has a simple pole at $s = 1$ (Proposition 11), the product $\zeta_m(s)$ also has a simple pole. Thus (b) $\Rightarrow$ (a).

Suppose now that $L(1, \chi) = 0$ for some $\chi \neq 1$. Then $\zeta_m$ would be holomorphic at $s = 1$, hence holomorphic for all $\Re(s) > 0$ (by Propositions 11 and 12). Since $\zeta_m$ is a Dirichlet series with positive coefficients, Proposition 7 would imply its convergence for all $\Re(s) > 0$.

But this is impossible: the $p$th factor of $\zeta_m$ is
$$\frac{1}{(1 - p^{-f(p)s})^{g(p)}} = (1 + p^{-f(p)s} + p^{-2f(p)s} + \cdots)^{g(p)},$$
which dominates $1 + p^{-\phi(m)s} + p^{-2\phi(m)s} + \cdots$. Hence $\zeta_m$ has all coefficients larger than those of $\sum_{(n,m)=1} n^{-\phi(m)s}$, which diverges at $s = 1/\phi(m)$. This contradiction proves (b), and hence (a).

