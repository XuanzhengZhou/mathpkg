---
role: proof
locale: en
of_concept: rank-and-index-from-diagonal-form
source_book: gtm023
source_chapter: "9"
source_section: "2. The decomposition of E"
---

Assume $\Phi \neq 0$. Then at least one coefficient $\alpha_{ij} \neq 0$.

**Case 1:** Some diagonal entry $\alpha_{ii} \neq 0$. After reordering, assume $\alpha_{11} \neq 0$. Write
$$\Phi(x) = \alpha_{11}(\xi^1)^2 + 2\sum_{\mu=2}^n \alpha_{1\mu} \xi^1 \xi^\mu + \sum_{v,\mu=2}^n \alpha_{v\mu} \xi^v \xi^\mu.$$

Complete the square in $\xi^1$:
$$\Phi(x) = \alpha_{11}\left(\xi^1 + \sum_{\mu=2}^n \frac{\alpha_{1\mu}}{\alpha_{11}} \xi^\mu\right)^2 + \sum_{v,\mu=2}^n \beta_{v\mu} \xi^v \xi^\mu$$
for some new coefficients $\beta_{v\mu}$. Setting $\eta^1 = \xi^1 + \sum_{\mu=2}^n \frac{\alpha_{1\mu}}{\alpha_{11}} \xi^\mu$ and $\eta^v = \xi^v$ for $v \geq 2$ yields
$$\Phi(x) = \alpha_{11}(\eta^1)^2 + \sum_{v,\mu=2}^n \beta_{v\mu} \eta^v \eta^\mu.$$

**Case 2:** All diagonal entries are zero but some off-diagonal $\alpha_{ij} \neq 0$ ($i \neq j$). Apply the substitution
$$\xi^i = \bar{\xi}^i + \bar{\xi}^j, \quad \xi^j = \bar{\xi}^i - \bar{\xi}^j.$$
Then $\xi^i \xi^j = (\bar{\xi}^i)^2 - (\bar{\xi}^j)^2$, creating nonzero diagonal coefficients $\bar{\alpha}_{ii} \neq 0$ and $\bar{\alpha}_{jj} \neq 0$. Now Case 1 applies.

The sum $\sum_{v,\mu=2}^n \beta_{v\mu} \eta^v \eta^\mu$ is a symmetric bilinear form in $n-1$ variables. Applying the same reduction repeatedly yields a full diagonalization
$$\Phi(x) = \sum_{v=1}^n \lambda_v (\zeta^v)^2.$$

Rearranging variables so that positive $\lambda_v$ come first, then negative, then zero, we obtain $r$ (the number of nonzero $\lambda_v$) as the rank and $s$ (the number of positive $\lambda_v$) as the index, by Sylvester's law of inertia.
