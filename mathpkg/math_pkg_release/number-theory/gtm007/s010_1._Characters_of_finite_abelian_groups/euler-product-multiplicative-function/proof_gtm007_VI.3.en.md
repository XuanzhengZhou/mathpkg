---
role: proof
locale: en
of_concept: euler-product-multiplicative-function
source_book: gtm007
source_chapter: "VI"
source_section: "3"
---

The absolute convergence of the series follows from Proposition 8, since $f$ is bounded. Let $S$ be a finite set of primes and let $N(S)$ be the set of integers $\geq 1$ all of whose prime factors belong to $S$. By multiplicativity,
$$\sum_{n \in N(S)} f(n)/n^s = \prod_{p \in S} \left(\sum_{m=0}^{\infty} f(p^m)p^{-ms}\right).$$

When $S$ increases, the left-hand side tends to $\sum_{n=1}^{\infty} f(n)/n^s$. Hence the infinite product converges and its value equals the sum of the series.

