---
role: proof
locale: en
of_concept: cauchy-transform-vanishing-implies-measure-zero
source_book: gtm035
source_chapter: "2"
source_section: "2.7"
---

# Proof of Vanishing Cauchy Transform Implies Measure Zero

**Lemma 2.7.** Let $\mu$ be a measure of compact support in $\mathbb{C}$.

(i) If $\hat{\mu} = 0$ almost everywhere with respect to $dx\,dy$, then $\mu = 0$.

(ii) If $\mu^* = 0$ almost everywhere with respect to $dx\,dy$, then $\mu = 0$.

## Proof

(i) Suppose $\hat{\mu} = 0$ a.e. Let $g \in C_0^1(\mathbb{C})$. By Lemma 2.5,

$$g(\zeta) = -\frac{1}{\pi} \int \frac{\partial g}{\partial \overline{z}}(z) \frac{dx\,dy}{z - \zeta}.$$

Integrating both sides with respect to $\mu(\zeta)$ and applying Fubini's theorem,

$$\int g\,d\mu = -\frac{1}{\pi} \int \frac{\partial g}{\partial \overline{z}}(z) \left( \int \frac{d\mu(\zeta)}{z - \zeta} \right) dx\,dy = -\frac{1}{\pi} \int \frac{\partial g}{\partial \overline{z}}(z) \,\hat{\mu}(z)\,dx\,dy.$$

Since $\hat{\mu} = 0$ a.e., we deduce $\int g\,d\mu = 0$ for all $g \in C_0^1(\mathbb{C})$.

But the class of functions obtained by restricting to $\operatorname{supp} \mu$ the functions in $C_0^1(\mathbb{C})$ is dense in $C(\operatorname{supp} \mu)$ by the Stone-Weierstrass theorem. Hence $\int f\,d\mu = 0$ for all $f \in C(\operatorname{supp} \mu)$, which implies $\mu = 0$.

(ii) Using Lemma 2.6, we proceed similarly. For $g \in C_0^2(\mathbb{C})$,

$$-\int g\,d\mu = \frac{1}{2\pi} \int \Delta g(z) \cdot \mu^*(z)\,dx\,dy.$$

If $\mu^* = 0$ a.e., then $\int g\,d\mu = 0$ for all $g \in C_0^2(\mathbb{C})$, and again by density we conclude $\mu = 0$. $\square$
