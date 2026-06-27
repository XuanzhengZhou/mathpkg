---
role: proof
locale: en
of_concept: g-matrix-reflecting-random-walk
source_book: gtm040
source_chapter: "7"
source_section: "7. Further examples"
---

First compute $0\bar{H}_{jj}$ for $j > 0$. From the recurrence relations for hitting probabilities in the reflecting random walk:

$$0\bar{H}_{jj} = \frac{1}{2} \, 0H_{j+1,j} + \frac{1}{2} \, 0H_{j-1,j}.$$

Since $0H_{j+1,j} = 1$ (from $j+1$ one must pass through $j$ to reach $0$, but actually hitting probability from $j+1$ to $j$...), we use known results:

$$0\bar{H}_{jj} = \frac{1}{2} + \frac{1}{2} \, 0H_{j-1,j}.$$

From Section 5-4, $0H_{j-1,j} = \frac{j-1}{j}$. Substituting:

$$0\bar{H}_{jj} = \frac{1}{2} + \frac{1}{2} \cdot \frac{j-1}{j} = 1 - \frac{1}{2j}.$$

Therefore, $0N_{jj} = \frac{1}{1 - 0\bar{H}_{jj}} = \frac{1}{1/(2j)} = 2j$.

By translation invariance (since the walk is spatially homogeneous for $j > i$), $iN_{jj} = 0N_{j-i,j-i} = 2(j-i)$.

Thus $G_{ij} = iN_{jj} = 2(j-i)$ for $j > i$, and $G_{ij} = 0$ for $j \leq i$ (since the chain cannot visit $j$ if starting above it without an absorption mechanism).
