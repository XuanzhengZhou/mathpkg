---
role: proof
locale: en
of_concept: liouville-numbers-hausdorff-measure-zero
source_book: gtm002
source_chapter: "2"
source_section: "2. Liouville Numbers"
---

It suffices to find, for each $\varepsilon > 0$ and for each positive integer $m$, a sequence of intervals $I_k$ such that

$$E \cap (-m, m) \subset \bigcup_{k=1}^{\infty} I_k, \quad \sum_{k=1}^{\infty} |I_k|^s < \varepsilon, \quad |I_k| < \varepsilon.$$

For each positive integer $n$, we have the covering

$$E \cap (-m, m) \subset \bigcup_{q=2}^{\infty} \bigcup_{p=-mq}^{mq} \left( \frac{p}{q} - \frac{1}{q^n}, \frac{p}{q} + \frac{1}{q^n} \right).$$

Choose $n$ so as to satisfy simultaneously the following conditions:

$$\frac{1}{2^{n-1}} < \varepsilon, \quad ns > 2, \quad \frac{(2m+1)2^s}{ns-2} < \varepsilon.$$

Then each of the intervals $\bigl(p/q - 1/q^n, p/q + 1/q^n\bigr)$ has length $2/q^n \leq 2/2^n < \varepsilon$, and we estimate

\begin{align*}
\sum_{q=2}^{\infty} \sum_{p=-mq}^{mq} \left( \frac{2}{q^n} \right)^s
&= \sum_{q=2}^{\infty} \frac{(2mq+1)2^s}{q^{ns}} \\
&\leq (2m+1)2^s \sum_{q=2}^{\infty} \frac{1}{q^{ns-1}} \\
&\leq (2m+1)2^s \int_{1}^{\infty} \frac{dx}{x^{ns-1}} \\
&= \frac{(2m+1)2^s}{ns-2} < \varepsilon.
\end{align*}

Thus the collection of all such intervals forms a suitable covering, proving that the $s$-dimensional Hausdorff measure of $E \cap (-m, m)$ is zero for every $m$. Hence $E$ has $s$-dimensional Hausdorff measure zero for every $s > 0$.
