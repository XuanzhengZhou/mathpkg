---
role: proof
locale: en
of_concept: growth-of-eisenstein-coefficients
source_book: gtm007
source_chapter: "VII"
source_section: "1"
---

By Proposition 8, there exists a constant $A > 0$ such that
$$a_n = (-1)^k A \sigma_{2k-1}(n).$$
Hence $|a_n| = A \sigma_{2k-1}(n)$.

For the lower bound: since $n \mid n$, we have $\sigma_{2k-1}(n) \geq n^{2k-1}$.

For the upper bound:
$$\frac{|a_n|}{n^{2k-1}} = A \sum_{d \mid n} \frac{1}{d^{2k-1}} \leq A \sum_{d=1}^{\infty} \frac{1}{d^{2k-1}} = A \zeta(2k-1) < +\infty,$$
since $2k-1 \geq 3 > 1$ for $k \geq 2$. Thus $|a_n| \leq A \zeta(2k-1) n^{2k-1}$.
