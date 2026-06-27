---
role: proof
locale: en
of_concept: bernoulli-polynomial-leading-terms
source_book: gtm059
source_chapter: "2"
source_section: "12"
---

The result follows by direct multiplication of the generating series. Write
$$\frac{t e^{tX}}{e^t - 1} = \sum_{k=0}^{\infty} B_k(X) \frac{t^k}{k!}.$$
Expanding $e^{tX} = \sum_{j=0}^{\infty} \frac{X^j t^j}{j!}$ and comparing coefficients with the series expansion of $t/(e^t-1) = \sum B_k t^k/k!$, one obtains explicit formulas for $B_k(X)$ in terms of $B_j$. The leading term $X^k$ arises from $B_0 = 1$ multiplying $X^k t^k/k!$, and the term $-\frac{k}{2}X^{k-1}$ arises from $B_1 = -1/2$ multiplying $X^{k-1} t^{k-1}/(k-1)!$, together with the factor $k$ from the binomial expansion. The remaining terms involve $B_j$ for $j \geq 2$ and hence have rational coefficients.
