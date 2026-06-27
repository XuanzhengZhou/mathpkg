---
role: proof
locale: en
of_concept: local-resolvent-expansion
source_book: gtm055
source_chapter: "12"
source_section: "Bounded linear transformations"
---

If $|\lambda - \lambda_0| < 1/d$, then

$$\| (\lambda_0 - \lambda) R_x(\lambda_0) \| = r < 1$$

and

$$\| (\lambda_0 - \lambda)^n R_x(\lambda_0)^n \| \leq r^n$$

for every $n$. Hence the series $\sum_{n=0}^{\infty} (\lambda_0 - \lambda)^n R_x(\lambda_0)^{n+1}$ is absolutely convergent and therefore convergent. Moreover, multiplying this series (on either side) term by term by $\lambda - x = (\lambda_0 - x) - (\lambda_0 - \lambda)$ gives rise to the difference

$$\sum_{n=0}^{\infty} ((\lambda_0 - \lambda) R_x(\lambda_0))^n - \sum_{n=0}^{\infty} ((\lambda_0 - \lambda) R_x(\lambda_0))^{n+1} = 1_{\mathcal{A}},$$

which shows that the sum is indeed $R_x(\lambda) = (\lambda - x)^{-1}$. In particular, no point of $\sigma_{\mathcal{A}}(x)$ lies in the disc $D$.
