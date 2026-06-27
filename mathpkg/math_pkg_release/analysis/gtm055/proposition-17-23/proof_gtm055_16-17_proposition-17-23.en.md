---
role: proof
locale: en
of_concept: proposition-17-23
source_book: gtm055
source_chapter: "16-17"
source_section: "Section 18_Section_18"
---

PROOF. Clearly $\alpha f + \beta g$ and $fg$ are locally analytic on $U_1 \cap U_2$, and if $\gamma$ is an oriented envelope of $\sigma_{\mathcal{A}}(x)$ in $U_1 \cap U_2$, then

$$\int_{\gamma} [\alpha f(\zeta) + \beta g(\zeta)] R_x(\zeta) d\zeta = \alpha \int_{\gamma} f(\zeta) R_x(\zeta) d\zeta + \beta \int_{\gamma} g(\zeta) R_x(\zeta) d\zeta$$

by Proposition 17.20. Hence $(\alpha f + \beta g)(x) = \alpha f(x) + \beta g(x)$. To verify the second equation in (11) is more difficult.

Let $\gamma$ be an oriented envelope of $\sigma_{\mathcal{A}}(x)$ in $U_1 \cap U_2$ as above, let $V$ denote the (open) set of those points $\lambda$ in $\mathbb{C}$ such that the winding number $w_{\gamma}(\lambda)$ is one, and let $\gamma'$ be an oriented envelope of $V^{-}$ in $U_1 \cap U_2$. (Since $V^{-}$ is a compact subset of $U_1 \cap U_2$, such an oriented envelope exists. Observe that if $\lambda$ lies in the range $W_{\gamma}$ of $\gamma$ then the winding number of $\gamma'$ at $\lambda$ is one, while if $\lambda$ lies in the range $W_{\gamma'}$ of $\gamma'$, then the winding number of $\gamma$ at $\lambda$ is zero.) Then, as is easily seen, $\gamma'$ is also an oriented envelope of $\sigma_{\mathcal{A}}(x)$ in $U_1 \cap U_2$, so

$$f(x) = \frac{1}{2\pi i} \int_{\gamma} f(\zeta) R_x(\zeta) d\zeta \quad \text{and} \quad g(x) = \frac{1}{2\pi i} \int_{\gamma'} g(\lambda) R_x(\lambda) d\lambda

Furthermore the inner integrals in both summands in (12) are readily evaluated by the Cauchy integral formula. Indeed,

$$\int_{\gamma} \frac{f(\zeta)}{\zeta - \lambda} d\zeta = (2\pi i)w_{\gamma}(\lambda)f(\lambda) = 0,$$

while

$$\int_{\gamma'} \frac{g(\lambda)}{\lambda - \zeta} d\lambda = (2\pi i)w_{\gamma'}(\zeta)g(\zeta) = 2\pi i g(\zeta).$$

(Recall that $\gamma'$ surrounds $W_{\gamma}$, but not vice versa.) Thus, putting everything together, we obtain

$$f(x)g(x) = \frac{-1}{4\pi^2} \int_{\gamma} 2\pi i f(\zeta)g(\zeta)R_x(\zeta)d\zeta$$

$$= \frac{1}{2\pi i} \int_{\gamma} f(\zeta)g(\zeta)R_x(\zeta)d\zeta,$$

and the theorem is proved.
