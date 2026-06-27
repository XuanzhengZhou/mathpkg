---
role: proof
locale: en
of_concept: complexity-not-computable
source_book: gtm053
source_chapter: "III"
source_section: "9"
---

Suppose, toward a contradiction, that there exists an algorithm computing $C_u(f)$ for an optimal family $u$ of $1$-functions. Then we can effectively enumerate all functions $f$ with $C_u(f) \leqslant k$ for any given $k$.

Define a new function $g$ by diagonalization: $g(n)$ is defined as follows. Consider the first $n+1$ functions $f_1, \ldots, f_{n+1}$ in the family $u$ (i.e., those with smallest indices). Let $g(n)$ be a value different from $f_1(n), \ldots, f_n(n)$ (this is possible since the codomain $\mathbf{Z}^+$ is infinite). Then $g$ is a recursive function, so $C_u(g)$ is finite.

However, by construction, $g$ differs from $u_k$ for all $k \leqslant C_u(g)$, which means $g$ cannot appear among the first $C_u(g)$ functions in the enumeration $u$. This implies $C_u(g) > C_u(g)$, a contradiction.

Therefore, $C_u(f)$ is not computable.
