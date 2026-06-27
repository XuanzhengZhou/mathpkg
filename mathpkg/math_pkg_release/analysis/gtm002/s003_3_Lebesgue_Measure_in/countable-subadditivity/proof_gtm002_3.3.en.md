---
role: proof
locale: en
of_concept: countable-subadditivity
source_book: gtm002
source_chapter: "3"
source_section: "3. Lebesgue Measure in r-Space"
---

For any $\varepsilon > 0$ there exists, for each $i$, a sequence of intervals $I_{ij}$ ($j = 1, 2, \ldots$) that covers $A_i$ such that

$$
\sum_j |I_{ij}| \leq m^*(A_i) + \frac{\varepsilon}{2^i}.
$$

Then $A \subset \bigcup_{i,j} I_{ij}$ and

$$
\sum_{i,j} |I_{ij}| \leq \sum_i m^*(A_i) + \varepsilon.
$$

Therefore $m^*(A) \leq \sum_i m^*(A_i) + \varepsilon$. Letting $\varepsilon \to 0$, the required inequality follows.
