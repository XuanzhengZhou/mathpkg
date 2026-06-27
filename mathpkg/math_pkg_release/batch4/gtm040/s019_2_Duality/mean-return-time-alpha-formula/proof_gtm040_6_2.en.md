---
role: proof
locale: en
of_concept: mean-return-time-alpha-formula
source_book: gtm040
source_chapter: "6"
source_section: "2. Duality"
---

We have

$$\sum_{i \in E} \alpha_i \bar{M}_{iE} = \sum_{i \in E} \sum_j \alpha_i {}^E \bar{N}_{ij} = \sum_j \sum_{i \in E} \alpha_i {}^E \bar{N}_{ij}$$

$$= \sum_j \alpha_j = \alpha 1,$$

the next-to-last equality following from Corollary 6-22. The first equality uses the fact that $\bar{M}_{iE} = \sum_j {}^E \bar{N}_{ij}$, i.e., the mean return time to $E$ is the sum of expected visits to all states before returning.
