---
role: proof
locale: en
of_concept: riesz-dunford-functional-calculus
source_book: gtm055
source_chapter: "17"
source_section: "18"
---

Clearly $\alpha f + \beta g$ and $fg$ are locally analytic on $U_1 \cap U_2$, and if $\gamma$ is an oriented envelope of $\sigma_{\mathcal{A}}(x)$ in $U_1 \cap U_2$, then

$$\int_{\gamma} [\alpha f(\zeta) + \beta g(\zeta)] R_x(\zeta) d\zeta = \alpha \int_{\gamma} f(\zeta) R_x(\zeta) d\zeta + \beta \int_{\gamma} g(\zeta) R_x(\zeta) d\zeta$$

by Proposition 17.20. Hence $(\alpha f + \beta g)(x) = \alpha f(x) + \beta g(x)$.

To verify the multiplicativity $f(x)g(x) = (fg)(x)$: let $\gamma$ be an oriented envelope of $\sigma_{\mathcal{A}}(x)$ in $U_1 \cap U_2$, let $V$ denote the open set of those points $\lambda$ in $\mathbb{C}$ such that the winding number $w_{\gamma}(\lambda)$ is one, and let $\gamma'$ be an oriented envelope of $V^{-}$ in $U_1 \cap U_2$. Then

$$f(x) = \frac{1}{2\pi i} \int_{\gamma} f(\zeta) R_x(\zeta) d\zeta \quad \text{and} \quad g(x) = \frac{1}{2\pi i} \int_{\gamma'} g(\lambda) R_x(\lambda) d\lambda.$$

Using the resolvent identity $R_x(\zeta)R_x(\lambda) = \frac{R_x(\zeta) - R_x(\lambda)}{\lambda - \zeta}$, the product becomes a sum of two double integrals. The inner integrals are evaluated by the Cauchy integral formula: $\int_{\gamma} \frac{f(\zeta)}{\zeta - \lambda} d\zeta = 0$ (since $w_{\gamma}(\lambda) = 0$ for $\lambda$ on $\gamma'$) and $\int_{\gamma'} \frac{g(\lambda)}{\lambda - \zeta} d\lambda = 2\pi i g(\zeta)$. Combining yields

$$f(x)g(x) = \frac{1}{2\pi i} \int_{\gamma} f(\zeta)g(\zeta)R_x(\zeta)d\zeta = (fg)(x).$$

The continuity statement follows from the fact that if $\{f_n\}$ converges uniformly on compact subsets of $U$ containing $\sigma_{\mathcal{A}}(x)$, then the integrals converge in norm.
