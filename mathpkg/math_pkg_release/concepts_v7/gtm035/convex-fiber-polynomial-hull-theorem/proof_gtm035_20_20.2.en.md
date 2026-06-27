---
role: proof
locale: en
of_concept: convex-fiber-polynomial-hull-theorem
source_book: gtm035
source_chapter: "Chapter 20"
source_section: "20.2"
---
# Proof of Polynomial Hull of Convex-Fibered Sets Over the Circle

**Theorem 20.2.** Fix a compact set $Y$ in $\mathbb{C}^2$ lying over $\Gamma$. Assume

$$(7) \quad Y_\lambda \text{ is convex for every } \lambda \in \Gamma.$$

Then $\hat{Y} \setminus Y$ equals the union of all graphs $\{(\lambda, f(\lambda)) : |\lambda| < 1\}$ with $f \in \mathcal{F}$.

**Proof.** Because of the claim just proved, it suffices to show that if $(\lambda_0, w_0) \in \hat{Y} \setminus Y$, then there exists $f \in \mathcal{F}$ with $f(\lambda_0) = w_0$.

We first take $\lambda_0 = 0$. Since $(0, w_0) \in \hat{Y}$, we may choose a probability measure $\mu$ on $Y$ such that, for each polynomial $P(\lambda, w)$,

$$(8) \quad P(0, w_0) = \int_Y P(\lambda, w) \, d\mu(\lambda, w).$$

Under the projection map $\pi : (\lambda, w) \mapsto \lambda$, $\mu$ "disintegrates" (see the Appendix) in the sense that there exists a probability measure $\mu_*$ on $\Gamma = \pi(Y)$, and for a.a. $\lambda$-$d\mu_*$ on $\Gamma$ there exists a probability measure $\sigma_\lambda$ on $Y_\lambda$, such that, for all $f \in C(Y)$,

$$\int_Y f \, d\mu = \int_\Gamma \left[ \int_{Y_\lambda} f(\lambda, w) \, d\sigma_\lambda(w) \right] d\mu_*(\lambda).$$

In view of (8), we have for $n = 1, 2, \ldots$,

$$0 = \int_Y \lambda^n \, d\mu = \int_\Gamma \lambda^n \, d\mu_*(\lambda).$$

This implies, writing $\lambda = e^{i\theta}$ for $\lambda \in \Gamma$, $\mu_* = \frac{1}{2\pi} d\theta$. (Why?) So we have for each $f \in C(Y)$

$$\int_Y f \, d\mu = \frac{1}{2\pi} \int_0^{2\pi} \left[ \int_{Y_{e^{i\theta}}} f(e^{i\theta}, w) \, d\sigma_{e^{i\theta}}(w) \right] d\theta.$$

Next fix $\lambda_0$ in $\{|\lambda| < 1\}$. We shall reduce our problem to the previous case. We put

$$\chi(\lambda) = \frac{\lambda - \lambda_0}{1 - \bar{\lambda}_0 \lambda};$$

therefore, $\chi$ gives a homeomorphism of $\Gamma$ onto $\Gamma$, and $\chi(\lambda_0) = 0$.

We define the set $Y'$ over $\Gamma$ by putting

$$Y'_\zeta = Y_{\chi^{-1}(\zeta)}, \quad \zeta \in \Gamma.$$

Then $Y'$ is compact. We verify that $(0, w_0) \in \hat{Y}'$. By the previous result, there exist $f \in H^\infty$, $f(0) = w_0$, and $f(\zeta) \in Y'_\zeta$ for a.a. $\zeta \in \Gamma$. Putting $g(\lambda) = f(\chi(\lambda))$, we then see that $g \in H^\infty$, $g(\lambda_0) = w_0$, and $g(\lambda) \in Y_\lambda$ for a.a. $\lambda$ in $\Gamma$, as desired.

Finally, fix $(\lambda_0, w_0)$ in $\hat{Y}$ with $\lambda_0 \in \Gamma$.

**EXERCISE 20.3.** $(\lambda_0, w_0) \in Y$.

This exercise completes the proof that $\hat{Y} \setminus Y = \{(\lambda, f(\lambda)) : |\lambda| < 1, f \in \mathcal{F}\}$. ∎
