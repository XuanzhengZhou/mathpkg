---
role: proof
locale: en
of_concept: liouville-numbers-hausdorff-measure-zero
source_book: gtm002
source_chapter: "1"
source_section: "2"
---

**Proof of Theorem 2.4.** It suffices to find, for each $\varepsilon > 0$ and for each positive integer $m$, a sequence of intervals $I_n$ such that

$$E \cap (-m, m) \subset \bigcup_{n=1}^{\infty} I_n, \quad \sum_{n=1}^{\infty} |I_n|^s < \varepsilon, \quad |I_n| < \varepsilon.$$

For each positive integer $n$, we have

$$E \cap (-m, m) \subset \bigcup_{q=2}^{\infty} \bigcup_{p=-mq}^{mq} \left( \frac{p}{q} - \frac{1}{q^n}, \frac{p}{q} + \frac{1}{q^n} \right).$$

Choose $n$ so as to satisfy simultaneously the following conditions:

$$\frac{1}{2^{n-1}} < \varepsilon, \quad ns > 2, \quad \frac{(2m+1)2^s}{ns-2} < \varepsilon.$$

Then each of the intervals $(p/q - 1/q^n, p/q + 1/q^n)$ has length $2/q^n \leq 2/2^n < \varepsilon$, and we have

$$\sum_{q=2}^{\infty} \sum_{p=-mq}^{mq} \left( \frac{2}{q^n} \right)^s = \sum_{q=2}^{\infty} \frac{(2mq+1)2^s}{q^{ns}}$$

$$\leq (2m+1)2^s \sum_{q=2}^{\infty} \frac{1}{q^{ns-1}} \leq (2m+1)2^s \int_1^{\infty} \frac{dx}{x^{ns-1}}$$

$$= \frac{(2m+1)2^s}{ns-2} < \varepsilon.$$

Thus the $s$-dimensional Hausdorff measure of $E \cap (-m, m)$ is zero for every $m$, and therefore the $s$-dimensional Hausdorff measure of $E$ is zero. $\square$
