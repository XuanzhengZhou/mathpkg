---
role: proof
locale: en
of_concept: dual-preserves-transition-matrix
source_book: gtm040
source_chapter: "6"
source_section: "2. Duality"
---

It is clear that $\hat{P} \geq 0$. For $\hat{P}1 \leq 1$ we have

$$\sum_j \hat{P}_{ij} = \sum_j rac{lpha_j P_{ji}}{lpha_i} \leq 1,$$

since $lpha$ is $P$-superregular. If all pairs communicate in $P$, then for any $i, j$ there exist paths $i = n_0, n_1, \ldots, n_s = j$ and $j = m_0, m_1, \ldots, m_r = i$ such that each consecutive transition has positive probability in $P$. Then they communicate in $\hat{P}$ by reversing these paths:

$$i, n_s, \ldots, n_1, j,$$
$$j, m_r, \ldots, m_1, i.$$

Since $\hat{P}_{n_{k+1} n_k} = lpha_{n_k} P_{n_k n_{k+1}} / lpha_{n_{k+1}} > 0$ whenever $P_{n_k n_{k+1}} > 0$, the reversed paths have positive probability in $\hat{P}$.
