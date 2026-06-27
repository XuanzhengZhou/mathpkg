---
role: proof
locale: en
of_concept: riemann-lebesgue-integrability-criterion
source_book: gtm002
source_chapter: "7"
source_section: "7. Functions of First Class"
---

**Forward direction:** Suppose $f$ is Riemann integrable on $I$. For $\varepsilon > 0$, let $F_n = \{x : \omega(x) \geq 1/n\}$. For any $k$, the set $F_k$ is a bounded closed set. Since $f$ is Riemann integrable, for each $n$ there is a partition such that the sum of lengths of intervals where oscillation exceeds $1/n$ is arbitrarily small. Hence $m(F_k) = 0$ for each $k$, and $D = \bigcup F_k$ is a nullset.

**Reverse direction:** Suppose $D$ is a nullset and $f$ is bounded on $I$, with upper and lower bounds $M$ and $m$, respectively. For any $\varepsilon > 0$, choose $k$ so that $(M - m) + |I| < k\varepsilon$. Since $F_k$ is a bounded closed nullset, cover $F_k$ with a finite number of disjoint open intervals the sum of whose lengths is less than $1/k$. The endpoints of these intervals that belong to $I$ determine a subdivision of $I$ into nonoverlapping intervals $I_i$ and $J_j$ such that $\sum |I_i| < 1/k$ and $\omega(x) < 1/k$ on each $J_j$. Hence, by Lemma 7.6,

$$F(I) = \sum F(I_i) + \sum F(J_j) \leq (M - m) \sum |I_i| + \sum (1/k) |J_j| \leq (M - m)/k + |I|/k < \varepsilon.$$

Consequently, $f$ is Riemann integrable on $I$.
