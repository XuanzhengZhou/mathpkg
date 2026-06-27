---
role: proof
locale: en
of_concept: mean-return-time-ii-formula
source_book: gtm040
source_chapter: "6"
source_section: "2. Duality"
---

By definition, $\bar{M}_{ii} = \sum_j {}^i \bar{N}_{ij}$. Using Corollary 6-21 with $E = \{i\}$,

$$\bar{M}_{ii} = \sum_j {}^i \bar{N}_{ij} = \sum_j \frac{\alpha_j}{\alpha_i} = \frac{1}{\alpha_i} \sum_j \alpha_j.$$

Since $\alpha$ is a regular measure, we may normalize so that $\sum_j \alpha_j = 1$, yielding $\bar{M}_{ii} = 1/\alpha_i$. More generally, if $\alpha$ is any positive regular measure (defined up to a multiplicative constant), the formula holds for the normalized measure.
