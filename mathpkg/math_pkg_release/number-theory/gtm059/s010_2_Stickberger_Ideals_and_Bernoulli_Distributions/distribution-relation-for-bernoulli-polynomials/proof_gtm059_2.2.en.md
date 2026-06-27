---
role: proof
locale: en
of_concept: distribution-relation-for-bernoulli-polynomials
source_book: gtm059
source_chapter: "2"
source_section: "2"
---

The proof uses the generating function. On one hand,
$$
\sum_{k=0}^{\infty} \left( N^{k-1} \sum_{a=0}^{N-1} B_k\left(\frac{X+a}{N}\right) \right) \frac{t^k}{k!}
= \frac{1}{N} \sum_{a=0}^{N-1} \sum_{k=0}^{\infty} B_k\left(\frac{X+a}{N}\right) \frac{(Nt)^k}{k!}
$$
$$
= \frac{1}{N} \sum_{a=0}^{N-1} \frac{Nt \, e^{(X+a)t}}{e^{Nt} - 1}
= \frac{t e^{Xt}}{e^{Nt} - 1} \sum_{a=0}^{N-1} e^{at}.
$$
Summing the geometric series gives $(e^{Nt} - 1)/(e^t - 1)$, so the expression equals
$$
\frac{t e^{Xt}}{e^t - 1} = \sum_{k=0}^{\infty} B_k(X) \frac{t^k}{k!}.
$$
Comparing coefficients yields the distribution relation.
