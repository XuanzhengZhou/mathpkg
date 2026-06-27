---
role: proof
locale: en
of_concept: isoperimetric-inequality-via-rational-approximation
source_book: gtm035
source_chapter: "Chapter 21"
source_section: "21.4"
---
# Proof of Proposition 21.4 (Isoperimetric Inequality via Rational Approximation)

**Proposition 21.4.** Let $\Omega$ be a closed Jordan domain in the plane with a smooth boundary. Let $A = \operatorname{area}(\Omega)$ and let $L = \operatorname{length}(\partial\Omega)$. Then

$$\frac{2A}{L} \leq \operatorname{dist}(\bar{z}, R(\Omega)).$$

**Proof.** Let $\varepsilon > 0$ and choose $g$ a rational function with no poles on $\Omega$ such that

$$\|\bar{z} - g\|_\Omega < \operatorname{dist}(\bar{z}, R(\Omega)) + \varepsilon.$$

We have, since $\int_{\partial\Omega} g \, dz = 0$ by Cauchy's theorem,

$$\left| \int_{\partial\Omega} \bar{z} \, dz \right| = \left| \int_{\partial\Omega} (\bar{z} - g) \, dz \right| < L \left( \operatorname{dist}(\bar{z}, R(\Omega)) + \varepsilon \right).$$

By Stokes' Theorem we have

$$2iA = \iint_\Omega d\bar{z} \, dz = \int_{\partial\Omega} \bar{z} \, dz.$$

We get

$$2A < L \left( \operatorname{dist}(\bar{z}, R(\Omega)) + \varepsilon \right).$$

Now the proposition follows by letting $\varepsilon \to 0$. ∎

**Remark.** Combining Lemma 21.3 and Proposition 21.4 gives

$$\frac{2A}{L} \leq \operatorname{dist}(\bar{z}, R(\Omega)) \leq \left( \frac{A}{\pi} \right)^{1/2}.$$

The classical isoperimetric inequality follows directly:

$$4\pi A \leq L^2.$$
