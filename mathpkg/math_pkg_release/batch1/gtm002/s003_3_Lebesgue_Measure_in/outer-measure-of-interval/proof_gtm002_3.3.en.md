---
role: proof
locale: en
of_concept: outer-measure-of-interval
source_book: gtm002
source_chapter: "3"
source_section: "3. Lebesgue Measure in r-Space"
---

The inequality $m^*(I) \leq |I|$ is clear, since $I$ covers itself. To prove the inverse inequality, let $\varepsilon > 0$ be arbitrary and let $\{I_i\}$ be an open covering of $I$ such that

$$
\sum |I_i| < m^*(I) + \varepsilon.
$$

Let $J$ be a closed subinterval of $I$ such that $|J| > |I| - \varepsilon$. By the Heine-Borel theorem, $J \subset \bigcup_{i=1}^k I_i$ for some $k$. Let $K_1, \ldots, K_n$ be an enumeration of the closed intervals into which the closures $\bar{I}_1, \ldots, \bar{I}_k$ are divided by all the $(r-1)$-dimensional hyperplanes that contain an $(r-1)$-dimensional face of one of the intervals $I_1, \ldots, I_k$, or $J$, and let $J_1, \ldots, J_m$ be the closed intervals into which $J$ is divided by these same hyperplanes.

Then each interval $J_i$ is equal to at least one of the intervals $K_j$. Consequently,

$$
|J| = \sum_{i=1}^m |J_i| \leq \sum_{j=1}^n |K_j| \leq \sum_{i=1}^k |I_i| < m^*(I) + \varepsilon.
$$

Thus $|I| - \varepsilon < |J| < m^*(I) + \varepsilon$. Since $\varepsilon$ is arbitrary, $|I| \leq m^*(I)$.
