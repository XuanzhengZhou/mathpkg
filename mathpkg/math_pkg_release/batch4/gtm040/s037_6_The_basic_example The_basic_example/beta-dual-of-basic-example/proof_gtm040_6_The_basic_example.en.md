---
role: proof
locale: en
of_concept: beta-dual-of-basic-example
source_book: gtm040
source_chapter: "6"
source_section: "The basic example"
---

By definition of the $\beta$-dual, $\hat{P}_{ij} = \frac{\beta_j P_{ji}}{\beta_i}$. For the basic example, $P$ has $P_{i,i+1} = p_{i+1}$ and $P_{i,0} = q_{i+1}$ as the only nonzero entries. Thus:

For $j = i-1$ (with $i \geq 1$):
$$\hat{P}_{i,i-1} = \frac{\beta_{i-1} P_{i-1,i}}{\beta_i} = \frac{\beta_{i-1} p_i}{\beta_i} = \frac{\beta_i}{\beta_i} = 1,$$
since $\beta_i = \beta_{i-1} p_i$.

For $i = 0$ and any $j$:
$$\hat{P}_{0j} = \frac{\beta_j P_{j0}}{\beta_0} = \beta_j q_{j+1} = \beta_j(1 - p_{j+1}) = \beta_j - \beta_j p_{j+1} = \beta_j - \beta_{j+1}.$$

All other entries are zero since $P_{ji} = 0$ for those transitions.

The sum of transition probabilities from $0$ is
$$\sum_{j=0}^\infty \hat{P}_{0j} = \sum_{j=0}^\infty (\beta_j - \beta_{j+1}) = \beta_0 - \lim_{j \to \infty} \beta_j = 1 - \beta_\infty,$$
which is $< 1$ when $\beta_\infty > 0$, confirming that the extended chain for $\hat{P}$ is absorbing in the transient case.

For regularity of $\beta$ with respect to $\hat{P}$:
$$\sum_i \beta_i \hat{P}_{ij} = \beta_{j+1} \hat{P}_{j+1,j} + \beta_0 \hat{P}_{0j} = \beta_{j+1} \cdot 1 + \beta_0(\beta_j - \beta_{j+1}) = \beta_j.$$
