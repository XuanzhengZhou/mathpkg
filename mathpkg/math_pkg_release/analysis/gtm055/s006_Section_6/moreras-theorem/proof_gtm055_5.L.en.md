---
role: proof
locale: en
of_concept: moreras-theorem
source_book: gtm055
source_chapter: "5"
source_section: "6"
---

Suppose $f$ is continuous on $\Delta$ and the integral of $f$ around every triangular arc in $\Delta$ is zero. Fix a point $\alpha \in \Delta$ and let $D \subset \Delta$ be a disc centered at $\alpha$. For any $\lambda \in D$, define $F(\lambda) = \int_{\sigma(\alpha, \lambda)} f(\zeta) d\zeta$, where the integral is taken along the directed line segment. Because the integral around every triangle vanishes, one shows that $F(\lambda) - F(\lambda_0) = \int_{\sigma(\lambda_0, \lambda)} f(\zeta) d\zeta$ for any $\lambda, \lambda_0 \in D$.

Given $\varepsilon > 0$, choose $\delta > 0$ such that $|f(\zeta) - f(\lambda_0)| < \varepsilon$ whenever $|\zeta - \lambda_0| < \delta$. For $\lambda$ with $|\lambda - \lambda_0| < \delta$, estimating the line integral yields
$$\left| \frac{F(\lambda) - F(\lambda_0)}{\lambda - \lambda_0} - f(\lambda_0) \right| < \varepsilon,$$
which shows $F'(\lambda_0) = f(\lambda_0)$. Thus $F$ is a primitive of $f$ on $D$, so $F$ is analytic on $D$. Since derivatives of analytic functions are analytic (Taylor's theorem), $f = F'$ is analytic on $D$. As the argument works for a disc about any point of $\Delta$, $f$ is analytic on $\Delta$.
