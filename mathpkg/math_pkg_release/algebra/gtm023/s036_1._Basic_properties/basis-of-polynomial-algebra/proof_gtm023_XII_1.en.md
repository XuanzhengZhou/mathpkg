---
role: proof
locale: en
of_concept: basis-of-polynomial-algebra
source_book: gtm023
source_chapter: "XII"
source_section: "1"
---

Denote the polynomial with $1$ at position $k$ and $0$ elsewhere by $t^k$. Then $t = (0,1,0,\ldots)$ satisfies $t^k = (0,\ldots,0,1,0,\ldots)$ with the $1$ at the $(k+1)$-th position (indexing from $0$). For any polynomial $f = (\alpha_0, \alpha_1, \ldots)$, we have $f = \sum_{v=0}^{\infty} \alpha_v t^v$ since only finitely many terms are non-zero. Uniqueness follows from the definition of equality of sequences: if $\sum \alpha_v t^v = \sum \beta_v t^v$, then comparing components gives $\alpha_v = \beta_v$ for all $v$. Linear independence of $\{t^k\}$ follows from the same argument: if $\sum c_k t^k = 0$, then each $c_k = 0$.
