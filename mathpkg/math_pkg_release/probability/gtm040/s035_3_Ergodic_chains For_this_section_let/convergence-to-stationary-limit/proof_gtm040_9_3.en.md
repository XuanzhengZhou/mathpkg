---
role: proof
locale: en
of_concept: convergence-to-stationary-limit
source_book: gtm040
source_chapter: "9"
source_section: "3"
---

$$\sum_j P_{ij}^{(n)}h_j = \frac{1}{\alpha_i} \sum_j (\alpha_j h_j) \hat{P}_{ji}^{(n)} \rightarrow \frac{1}{\alpha_i} \sum_j (\alpha_j h_j) \alpha_i \quad \text{by dominated convergence} = \alpha h.$$

The equality uses the duality relation $P_{ij}^{(n)} = \frac{\alpha_j}{\alpha_i} \hat{P}_{ji}^{(n)}$. The limit inside the sum uses that $\hat{P}_{ji}^{(n)} \to \hat{\alpha}_j = \alpha_i$ for the dual chain, which is also noncyclic ergodic.
