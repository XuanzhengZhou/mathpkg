---
role: proof
locale: en
of_concept: equality-of-iterated-line-integrals
source_book: gtm055
source_chapter: "3"
source_section: "Problems"
---

Let $[a, b]$ and $[c, d]$ be the parameter intervals. Then
$$\int_{\alpha} \left[ \int_{\beta} g(\zeta, \lambda) d\lambda \right] d\zeta = \int_a^b \left[ \int_c^d g(\alpha(s), \beta(t)) \beta'(t) dt \right] \alpha'(s) ds.$$
Since $g(\alpha(s), \beta(t)) \alpha'(s) \beta'(t)$ is continuous on $[a,b] \times [c,d]$, the classical Fubini theorem for Riemann integrals yields equality of the iterated integrals, which is exactly the claimed identity.
