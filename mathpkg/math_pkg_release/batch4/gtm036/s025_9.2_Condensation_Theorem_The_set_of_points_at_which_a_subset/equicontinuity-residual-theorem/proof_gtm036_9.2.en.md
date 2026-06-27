---
role: proof
locale: en
of_concept: equicontinuity-residual-theorem
source_book: gtm036
source_chapter: "9"
source_section: "9.2"
---

Because the sequence $\{f_n(x)\}$ is convergent, the requirement of equicontinuity of $\{f_n\}$ at $x$ can be rephrased: for $\varepsilon > 0$ there are a neighborhood $U$ of $x$ and a positive integer $k$ such that $d(f_p(y), f_k(y)) < \varepsilon$ for $y \in U$ and for $p \geq k$.

Let $K_{n,k}$ be the closed set defined by
$$K_{n,k} = \{x : d(f_p(x), f_k(x)) \leq 1/n \text{ for } p \geq k\},$$
and let $K_n = \bigcup \{K_{n,k}^i : k = 1, 2, \cdots\}$, the union of the interiors. Then the set of points of equicontinuity is the intersection $\bigcap \{K_n : n = 1, 2, \cdots\}$.

On the other hand, $\bigcup \{K_{n,k} : k = 1, 2, \cdots\} = X$, since the sequence $\{f_n\}$ is convergent. Hence
$$X \setminus K_n \subset \bigcup \{K_{n,k} \setminus K_{n,k}^i : k = 1, 2, \cdots\},$$
which is obviously of the first category in $X$ (each $K_{n,k} \setminus K_{n,k}^i$ is the boundary of $K_{n,k}$ and hence nowhere dense). Therefore $X \setminus \bigcap \{K_n : n = 1, 2, \cdots\}$ is of the first category, so the set of equicontinuity points is residual.
