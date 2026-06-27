---
role: proof
locale: en
of_concept: integral-maxwell-equations
source_book: gtm048
source_chapter: "3"
source_section: "3.7"
---

Condition (a) is equivalent to $\operatorname{div} \hat{F} = 4\pi J$ by the divergence theorem for semi-Riemannian manifolds. Specifically, for any space-section $\mathcal{D}$, Stokes' theorem gives

$$\int_{\partial \mathcal{D}} i(\hat{F})\Omega = \int_{\mathcal{D}} d(i(\hat{F})\Omega) = \int_{\mathcal{D}} (\operatorname{div} \hat{F}) \, \Omega,$$

where the last equality uses the identity $d(i(X)\Omega) = (\operatorname{div} X)\Omega$ for any vector field $X$ (see Section 3.0.2). Meanwhile, $\int_{\mathcal{D}} i(J)\Omega$ is the integral of the charge-current density over $\mathcal{D}$. Thus the equality $\int_{\partial \mathcal{D}} i(\hat{F})\Omega = 4\pi \int_{\mathcal{D}} i(J)\Omega$ holds for all space-sections $\mathcal{D}$ if and only if $\operatorname{div} \hat{F} = 4\pi J$ pointwise.

Condition (b) is equivalent to $dF = 0$ by Stokes' theorem. For any 3-dimensional compact submanifold-with-boundary $\mathcal{C}$, we have $\int_{\partial \mathcal{C}} F = \int_{\mathcal{C}} dF$. If this vanishes for all such $\mathcal{C}$, then $dF = 0$ pointwise (by the fundamental lemma of the calculus of variations). Conversely, if $dF = 0$, then all such integrals vanish.
