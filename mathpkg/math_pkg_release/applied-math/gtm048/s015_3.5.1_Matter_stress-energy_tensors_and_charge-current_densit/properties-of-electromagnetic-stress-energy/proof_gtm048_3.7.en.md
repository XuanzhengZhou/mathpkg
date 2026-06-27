---
role: proof
locale: en
of_concept: properties-of-electromagnetic-stress-energy
source_book: gtm048
source_chapter: "3"
source_section: "3.7"
---

**(a)** The symmetry of $\hat{E}$ follows directly from the definition $E_{ij} = (1/4\pi)[F_{im}F_j^{\,m} - \frac{1}{4}g_{ij}F_{mn}F^{mn}]$. Since $F_{im}F_j^{\,m}$ is symmetric in $i,j$ (both indices are contracted with the symmetric metric) and $g_{ij}$ is symmetric, $\hat{E}$ is symmetric. For the trace: $\operatorname{trace} \hat{E} = g^{ij}E_{ij} = (1/4\pi)[F^{jm}F_{jm} - \frac{1}{4} \cdot 4 \cdot F_{mn}F^{mn}] = (1/4\pi)[F^{mn}F_{mn} - F^{mn}F_{mn}] = 0$.

**(b)** We first show $\hat{E}(\omega, \omega) \geq 0$ for every timelike 1-form $\omega$. Replacing $\omega$ by $\omega/|\omega|$ if necessary, we may assume $|\omega| = 1$. Locally, choose an orthonormal basis of 1-forms $\{\omega^i\}$ so that $\omega^4 = \omega$. Relative to $\{\omega^i\}$, we have $g_{\alpha\beta} = g^{\alpha\beta} = \delta_{\alpha\beta}$, $g_{\alpha 4} = g^{\alpha 4} = 0$ for $1 \leq \alpha, \beta \leq 3$, and $g_{44} = g^{44} = -1$.

In this basis, the antisymmetry of $F$ gives $F_{4\alpha} = -F_{\alpha 4}$. Computing $\hat{E}(\omega, \omega) = E^{44}$:
$$E^{44} = \frac{1}{4\pi}\left[F^{4m}F^4_{\,m} - \frac{1}{4}g^{44}F_{mn}F^{mn}\right] = \frac{1}{4\pi}\left[\sum_{\alpha=1}^{3}(F^{4\alpha})^2 + \frac{1}{4}F_{mn}F^{mn}\right].$$

Expanding $F_{mn}F^{mn}$ in the orthonormal basis yields $F_{mn}F^{mn} = 2\sum_{\alpha,\beta}(F_{\alpha\beta})^2 - 4\sum_{\alpha}(F_{4\alpha})^2$. Substituting gives $E^{44} = (1/8\pi)[\sum_{\alpha,\beta}(F_{\alpha\beta})^2 + \sum_{\alpha}(F_{4\alpha})^2] \geq 0$. The result extends to causal 1-forms by continuity.

**(c)** Assume $(M, F, J)$ obeys Maxwell's equations, so $dF = 0$ and $\operatorname{div} \hat{F} = 4\pi J$. Using the component expression for $\operatorname{div} \hat{E}$:

$$E^{ij}_{\;\;|j} = \frac{1}{4\pi}\left[(F^{im}F^{jm})_{|j} - \frac{1}{4}g^{ij}(F_{mn}F^{mn})_{|j}\right].$$

Applying the Leibniz rule and the fact that $dF = 0$ implies $F_{km|j} + F_{mj|k} + F_{jk|m} = 0$ (the second Bianchi-type identity for a closed 2-form, since the connection is torsion-free), we obtain after rearrangement:

$$E^{ij}_{\;\;|j} = \frac{1}{4\pi}\left\{-4\pi F^{im}J_m - \frac{1}{2}g^{ik}F^{mf}(F_{km|j} - F_{kj|m} + F_{mj|k})\right\}.$$

The second term vanishes by the closure condition on $F$. Thus $E^{ij}_{\;\;|j} = -F^{im}J_m$, which is $\operatorname{div} \hat{E} = -\tilde{F}J$ in coordinate-free notation.
