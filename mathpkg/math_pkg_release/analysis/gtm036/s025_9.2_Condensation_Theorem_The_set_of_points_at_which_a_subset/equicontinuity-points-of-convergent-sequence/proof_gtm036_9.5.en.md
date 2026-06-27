---
role: proof
locale: en
of_concept: equicontinuity-points-of-convergent-sequence
source_book: gtm036
source_chapter: "9"
source_section: "9.5"
---

Because the sequence $\{f_n(x)\}$ is convergent, the requirement of equicontinuity of $\{f_n\}$ at $x$ can be rephrased: for $e > 0$ there are a neighborhood $U$ of $x$ and a positive integer $k$ such that $d(f_p(y), f_k(y)) < e$ for $y$ in $U$ and for $p \geq k$. Let $K_{n,k}$ be the closed set defined by $K_{n,k} = \{x : d(f_p(x), f_k(x)) \leq 1/n \text{ for } p \geq k\}$, and let $K_n = \bigcup \{K_{n,k}^i : k = 1, 2, \cdots\}$, the union of the interiors. Then the set of points of equicontinuity is the intersection $\bigcap \{K_n : n = 1, 2, \cdots\}$ of the sets $K_n$. On the other hand, $\bigcup \{K_{n,k} : k = 1, 2, \cdots\} = X$, since the sequence $\{f_n\}$ is convergent. Hence $X \sim K_n \subset \bigcup \{K_{n,k} \sim K_{n,k}^i : k = 1, 2, \cdots\}$, which is obviously of the first category in $X$, and hence $X \sim \bigcap \{K_n : n = 1, 2, \cdots\}$ is of the first category.
