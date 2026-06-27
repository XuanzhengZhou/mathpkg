---
role: proof
locale: en
of_concept: coefficient-bound-non-cusp-forms
source_book: gtm041
source_chapter: "6"
source_section: "6.15"
---

Every entire modular form $f \in M_{2k}$ can be written uniquely as
$$f = \lambda G_{2k} + f_0,$$
where $\lambda$ is a constant and $f_0 \in M_{2k,0}$ is a cusp form. By Theorem 6.17, the coefficients of $f_0$ satisfy $O(n^k)$.

For the Eisenstein series $G_{2k}$, the Fourier coefficients are proportional to the divisor sum $\sigma_{2k-1}(n)$:
$$G_{2k}(\tau) = 2\zeta(2k) + \frac{2(2\pi i)^{2k}}{(2k-1)!} \sum_{n=1}^{\infty} \sigma_{2k-1}(n) e^{2\pi i n\tau}.$$

We estimate
$$\sigma_{2k-1}(n) = \sum_{d \mid n} d^{2k-1} \leq n^{2k-1} \sum_{d \mid n} \frac{1}{d^{2k-1}} \leq n^{2k-1} \sum_{d=1}^{\infty} \frac{1}{d^{2k-1}} = n^{2k-1} \zeta(2k-1),$$
where $\zeta(2k-1)$ converges since $2k-1 \geq 3$ for $k \geq 2$. Hence $\sigma_{2k-1}(n) = O(n^{2k-1})$.

Since $O(n^k) \subset O(n^{2k-1})$ for $k \geq 1$, both the cuspidal and Eisenstein components satisfy $O(n^{2k-1})$. Therefore
$$c(n) = O(n^{2k-1}).$$
