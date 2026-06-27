---
role: proof
locale: en
of_concept: rate-of-change-of-angular-momentum-system
source_book: gtm060
source_chapter: "2"
source_section: "10"
---

$$\frac{dM}{dt} = \sum_{i=1}^{n} [\dot{r}_i, m_i \dot{r}_i] + \sum_{i=1}^{n} [r_i, m_i \ddot{r}_i] = \sum_{i=1}^{n} [r_i, F_i].$$

The first term vanishes since $[\dot{r}_i, m_i \dot{r}_i] = 0$. Now $F_i = \sum_j F_{ij} + F'_i$, so
$$\sum_{i=1}^{n} [r_i, F_i] = \sum_{i,j} [r_i, F_{ij}] + \sum_i [r_i, F'_i].$$

The sum of moments of internal forces vanishes:
$$[r_i, F_{ij}] + [r_j, F_{ji}] = [(r_i - r_j), F_{ij}] = 0$$
since $F_{ij} = -F_{ji}$ and $F_{ij}$ is parallel to $r_i - r_j$. Therefore $dM/dt = \sum_i [r_i, F'_i] = N$.
