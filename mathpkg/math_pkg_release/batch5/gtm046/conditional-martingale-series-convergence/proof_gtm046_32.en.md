---
role: proof
locale: en
of_concept: conditional-martingale-series-convergence
source_book: gtm046
source_chapter: "IX"
source_section: "32"
---
Let $X_n = \sum_{k=1}^n Y_k$ form a martingale sequence. According to 29.2A,
$$P[\sup_{k \leq n} |X_k| > c] \leq E|X_n|^r / c^r, \quad r \geq 1.$$
For $r = 2$, the summands are orthogonal: $EX_n^2 = \sum_{k=1}^n E Y_k^2$, and the inequality reduces to the extended Kolmogorov inequality.

Define the stopping time $\nu$ by $[\nu = n] = [\sum_{k=1}^{n-1} E^{\mathfrak{B}_{k-1}} Y_k^2 \leq a, \sum_{k=1}^n E^{\mathfrak{B}_{k-1}} Y_k^2 > a]$, $[\nu = \infty] = [\sum E^{\mathfrak{B}_{n-1}} Y_n^2 \leq a]$. The $\nu$-truncated sums form a martingale bounded by $a$. Taking expectations,
$$E^2|X'_n| \leq E X'_n^2 \leq \sum E Y'_n^2 \leq a + c^2,$$
so $X'_n \xrightarrow{\text{a.s.}} X'$ finite by 29.3A. Therefore $X_n \xrightarrow{\text{a.s.}} X$ finite on $[\sum P^{\mathfrak{B}_{n-1}} Y_n^2 < \infty]$.
