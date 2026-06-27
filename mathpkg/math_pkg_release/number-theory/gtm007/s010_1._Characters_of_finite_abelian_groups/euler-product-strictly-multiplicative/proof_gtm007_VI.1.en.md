---
role: proof
locale: en
of_concept: euler-product-strictly-multiplicative
source_book: gtm007
source_chapter: "VI"
source_section: "§1. Characters of finite abelian groups"
---

Since $f$ is strictly multiplicative, $f(p^m) = f(p)^m$ for all primes $p$. Each prime factor in Lemma 4 becomes a geometric series:
$$
\sum_{m=0}^\infty \frac{f(p^m)}{p^{ms}} = \sum_{m=0}^\infty \left(\frac{f(p)}{p^s}\right)^m = \frac{1}{1 - f(p)/p^s},
$$
convergent for $|f(p)/p^s| < 1$, i.e., for $R(s) > 0$ if $|f(p)| \leq 1$.
