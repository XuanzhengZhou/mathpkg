---
role: proof
locale: en
of_concept: lebesgue-riemann-integrability-criterion
source_book: gtm002
source_chapter: "7"
source_section: "7"
---

For a given function $f$, bounded on $I$, let $F(I)$ be the greatest lower bound of all sums of the form
$$\sum_{i=1}^{n} \omega(I_i) |I_i|,$$
where $\{I_1, \ldots, I_n\}$ is any subdivision of $I$ (a finite set of non-overlapping closed intervals whose union is $I$). $F(I)$ is the difference between the upper and lower integrals of $f$ on $I$; the equation $F(I) = 0$ expresses the condition that $f$ be Riemann integrable on $I$. It is easy to verify that if $\{I_1, \ldots, I_n\}$ is any subdivision of $I$, then $F(I) = \sum_{i=1}^{n} F(I_i)$.

**Lemma 7.6.** If $\omega(x) < \varepsilon$ for each $x$ in $I$, then $F(I) < \varepsilon|I|$.

*Proof of Lemma.* Suppose the contrary, $F(I) \geq \varepsilon|I|$. Then $F(I_1) \geq \varepsilon|I|/2$ for at least one of the intervals obtained by bisecting $I$. By repeated bisection we obtain a nested sequence of closed intervals $I_n$ such that $F(I_n) \geq \varepsilon|I|/2^n$. These intersect in a point $x$ of $I$. By hypothesis, $\omega(x) < \varepsilon$ and therefore $\omega(J) < \varepsilon$ for some open interval $J$ containing $x$. Choose $n$ so that $I_n \subset J$. Then $F(I_n) \leq \omega(I_n)|I_n| \leq \omega(J)|I|/2^n < \varepsilon|I|/2^n$, contradiction.

Now, for any $k$, let $F_k = \{x : \omega(x) \geq 1/k\}$. If $f$ is Riemann integrable, then for each $k$ there is a subdivision of $I$ such that the sum of the lengths of the intervals that meet $F_k$ is arbitrarily small. Hence each $F_k$ is a nullset, and the set of discontinuities $D = \bigcup_k F_k$ is a nullset.

Conversely, suppose $D$ is a nullset and $f$ is bounded on $I$, with upper and lower bounds $M$ and $m$. For any $\varepsilon > 0$, choose $k$ so that $(M-m) + |I| < k\varepsilon$. Since $F_k$ is a bounded closed nullset, it is possible to cover $F_k$ with a finite number of disjoint open intervals whose total length is less than $1/k$. The endpoints of these intervals that belong to $I$ determine a subdivision of $I$ into non-overlapping intervals $I_i$ and $J_j$ such that $\sum |I_i| < 1/k$ and $\omega(x) < 1/k$ on each $J_j$. Hence, by Lemma 7.6,

$$F(I) = \sum F(I_i) + \sum F(J_j) \leq (M-m)\sum |I_i| + \sum (1/k)|J_j|$$
$$\leq (M-m)/k + |I|/k < \varepsilon.$$

Since $\varepsilon > 0$ is arbitrary, $F(I) = 0$, so $f$ is Riemann integrable on $I$.
