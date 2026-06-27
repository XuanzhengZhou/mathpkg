---
role: proof
locale: en
of_concept: countable-union-of-measure-zero-sets
source_book: gtm014
source_chapter: "II"
source_section: "§1. Sard's Theorem"
---

Let $S_1, S_2, \ldots$ be sets of measure zero in $\mathbf{R}^n$. Given $\varepsilon > 0$, cover each $S_i$ by open cubes $\{C_{i,j}\}_{j=1}^{\infty}$ whose total volume satisfies
$$\sum_{j=1}^{\infty} \text{vol}[C_{i,j}] < \frac{\varepsilon}{2^i}.$$
Then the countable collection $\{C_{i,j} : i, j = 1, 2, \ldots\}$ covers $\bigcup_{i=1}^{\infty} S_i$, and the total volume of all these cubes is
$$\sum_{i=1}^{\infty} \sum_{j=1}^{\infty} \text{vol}[C_{i,j}] < \sum_{i=1}^{\infty} \frac{\varepsilon}{2^i} = \varepsilon.$$
Hence $\bigcup_{i=1}^{\infty} S_i$ has measure zero.
