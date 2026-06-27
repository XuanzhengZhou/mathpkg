---
role: proof
locale: en
of_concept: distance-to-rational-algebra
source_book: gtm035
source_chapter: "Chapter 21"
source_section: "21.2"
---
# Proof of Lemma 21.2 (Distance to the Rational Algebra $R(K)$)

**Lemma 21.2.** Let $K$ be a compact subset of the plane, and set

$$F(z) = \iint_K \frac{1}{\zeta - z} \, du \, dv, \quad \text{where } \zeta = u + iv.$$

Then $F$ is continuous on the plane and $\|F\|_K \leq (\pi \operatorname{area}(K))^{1/2}$.

**Proof.** The continuity of $F$ is a consequence of the fact that the convolution of a local $L^1$ function with a bounded function of compact support is continuous.

To estimate $F(z)$, we may assume, by a translation, that $z = 0$. Then, by a rotation we may assume that $F(0)$ is real and positive. Writing $\zeta = re^{i\theta}$, we have

$$F(0) = \operatorname{Re}(F(0)) = \iint_K \cos(\theta) \, dr \, d\theta.$$

Letting $K^+$ be the part of $K$ in the right half-plane, we get

$$F(0) \leq \iint_{K^+} \cos(\theta) \, dr \, d\theta.$$

Let $\ell(\theta)$ be the linear measure of the set of points $\zeta$ of $K^+$ with $\arg(\zeta) = \theta$. We have

$$F(0) \leq \iint_{K^+} \cos(\theta) \, dr \, d\theta = \int_{-\frac{\pi}{2}}^{\frac{\pi}{2}} \ell(\theta) \cos(\theta) \, d\theta \leq \left( \frac{\pi}{2} \int_{-\frac{\pi}{2}}^{\frac{\pi}{2}} \ell(\theta)^2 \, d\theta \right)^{1/2},$$

by the Cauchy–Schwarz inequality (since $\int_{-\pi/2}^{\pi/2} \cos^2\theta \, d\theta = \pi/2$).

The reader can verify that

$$\int_{\{r : re^{i\theta} \in K^+\}} r \, dr \geq \int_0^{\ell(\theta)} r \, dr = \frac{\ell(\theta)^2}{2}.$$

We conclude that

$$F(0) \leq \left( \pi \iint_{K^+} r \, dr \, d\theta \right)^{1/2} = \left( \pi \operatorname{area}(K^+) \right)^{1/2} \leq \left( \pi \operatorname{area}(K) \right)^{1/2}.$$

Since the bound holds for any $z$ after translation, $\|F\|_K \leq (\pi \operatorname{area}(K))^{1/2}$. ∎
