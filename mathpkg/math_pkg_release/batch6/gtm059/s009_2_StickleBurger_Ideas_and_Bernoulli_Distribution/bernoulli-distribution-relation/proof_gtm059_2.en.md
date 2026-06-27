---
role: proof
locale: en
of_concept: bernoulli-distribution-relation
source_book: gtm059
source_chapter: "2"
source_section: "2. Stickelberger Ideals and Bernoulli Distributions"
---

Starting from the generating series:

$$\sum_{k=0}^{\infty} B_k(X) \frac{t^k}{k!} = \frac{t e^{tX}}{e^t - 1},$$

we compute the right-hand side of the distribution relation:

$$N^{k-1} \sum_{a=0}^{N-1} B_k\!\left(\frac{X+a}{N}\right) \frac{t^k}{k!} = \frac{1}{N} \sum_{a=0}^{N-1} \frac{t e^{t(X+a)/N}}{e^{t/N} - 1} = \frac{t e^{tX/N}}{N(e^{t/N} - 1)} \sum_{a=0}^{N-1} e^{ta/N}.$$

The geometric sum gives $\sum_{a=0}^{N-1} e^{ta/N} = \frac{e^t - 1}{e^{t/N} - 1}$. Substituting:

$$= \frac{t e^{tX/N}}{N(e^{t/N} - 1)} \cdot \frac{e^t - 1}{e^{t/N} - 1} = \frac{t e^{tX}}{e^t - 1} = \sum_{k=0}^{\infty} B_k(X) \frac{t^k}{k!}.$$

Comparing coefficients of $t^k/k!$ yields the relation.
