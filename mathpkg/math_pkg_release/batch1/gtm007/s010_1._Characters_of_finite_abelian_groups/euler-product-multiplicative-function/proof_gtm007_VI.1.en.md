---
role: proof
locale: en
of_concept: euler-product-multiplicative-function
source_book: gtm007
source_chapter: "VI"
source_section: "§1. Characters of finite abelian groups"
---

The absolute convergence follows from Proposition 8 (bounded coefficients). Let $S$ be a finite set of primes and $N(S)$ the set of integers whose prime factors all lie in $S$. By unique factorization and multiplicativity,
$$
\sum_{n \in N(S)} \frac{f(n)}{n^s} = \prod_{p \in S} \sum_{m=0}^\infty \frac{f(p^m)}{p^{ms}}.
$$
As $S$ increases to include all primes, the left side tends to the full Dirichlet series, establishing convergence of the infinite product and the Euler product identity.
