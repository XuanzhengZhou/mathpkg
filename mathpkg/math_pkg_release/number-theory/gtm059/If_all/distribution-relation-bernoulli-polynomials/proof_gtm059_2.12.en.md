---
role: proof
locale: en
of_concept: distribution-relation-bernoulli-polynomials
source_book: gtm059
source_chapter: "2"
source_section: "12"
---

Consider the generating function $F(t,X) = te^{tX}/(e^t-1) = \sum_{k=0}^{\infty} B_k(X) t^k/k!$. On one hand, we compute:
$$\sum_{k=0}^{\infty} \frac{N^{k-1} \sum_{a=0}^{N-1} B_k\!\left(\frac{X+a}{N}\right)}{k!} \, t^k = \frac{1}{N} \sum_{a=0}^{N-1} \sum_{k=0}^{\infty} \frac{B_k\!\left(\frac{X+a}{N}\right) N^k t^k}{k!}.$$

Substituting the generating function,
$$= \frac{1}{N} \sum_{a=0}^{N-1} \frac{Nt \, e^{t(X+a)}}{e^{Nt} - 1} = \frac{t}{e^{Nt}-1} e^{tX} \sum_{a=0}^{N-1} e^{ta} = \frac{t}{e^{Nt}-1} e^{tX} \cdot \frac{e^{Nt}-1}{e^t-1} = \frac{t e^{tX}}{e^t-1} = \sum_{k=0}^{\infty} B_k(X) \frac{t^k}{k!}.$$

Comparing coefficients of $t^k/k!$ yields $B_k(X) = N^{k-1} \sum_{a=0}^{N-1} B_k(\frac{X+a}{N})$, as desired.
