---
role: proof
locale: en
of_concept: karhunen-loeve-expansion
source_book: gtm017
source_chapter: "7"
source_section: "Additional Topics"
---

First, $\int_0^T E|X_t|dt \leq \int_0^T \{r(t,t)\}^{1/2}dt < \infty$, so by Fubini the integrals defining $Z_i$ are well-defined for almost all realizations.

The $Z_i$ are orthonormal: $E Z_i Z_j = \sqrt{\lambda_i\lambda_j} \iint \varphi_i(t)\varphi_j(\tau)r(t,\tau)dtd\tau = \sqrt{\lambda_i\lambda_j} \int \varphi_i(t)\varphi_j(t)/\lambda_j dt = \delta_{ij}$.

The mean-square error of the $N$-term approximation is
$$E|X_t - \sum_{i=1}^N Z_i \varphi_i(t)/\sqrt{\lambda_i}|^2 = r(t,t) - \sum_{i=1}^N \varphi_i^2(t)/\lambda_i.$$
By Mercer's theorem this tends to zero as $N \to \infty$. If $X_t$ is Gaussian, the linear functionals $Z_i$ are jointly Gaussian and, being orthonormal, are independent standard normal.
