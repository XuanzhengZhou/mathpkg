---
role: proof
locale: en
of_concept: power-series-analytic-in-disk
source_book: gtm011
source_chapter: "2"
source_section: "2.9"
---

By Theorem 2.8, the power series $f(z) = \sum_{n=0}^\infty a_n(z-a)^n$ can be differentiated term-by-term infinitely many times at every point in $B(a;R)$. Specifically, for each $k \geq 1$, the $k$-th derivative exists and is given by the differentiated series

$$f^{(k)}(z) = \sum_{n=k}^\infty n(n-1)\cdots(n-k+1) a_n (z-a)^{n-k},$$

which also has radius of convergence $R$. Since $f$ is infinitely differentiable at every point of $B(a;R)$, it is, by definition, analytic in $B(a;R)$.
