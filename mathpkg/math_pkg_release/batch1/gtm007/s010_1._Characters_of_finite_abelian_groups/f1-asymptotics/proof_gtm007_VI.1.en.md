---
role: proof
locale: en
of_concept: f1-asymptotics
source_book: gtm007
source_chapter: "VI"
source_section: "§1. Characters of finite abelian groups"
---

The function $f_1(s)$ differs from $\sum_p 1/p^s$ by only finitely many terms (those primes dividing $m$). It is known (Corollary 2 to Proposition 10) that $\sum_p 1/p^s \sim \log\frac{1}{s-1}$. More precisely, from $\zeta(s) \sim 1/(s-1)$ and the Euler product, taking logarithms gives
$$
\log \zeta(s) = \sum_p \frac{1}{p^s} + \sum_p \sum_{n \geq 2} \frac{1}{n p^{ns}},
$$
and the second sum is bounded near $s=1$, so $\sum_p 1/p^s = \log \zeta(s) + O(1) \sim \log\frac{1}{s-1}$.
