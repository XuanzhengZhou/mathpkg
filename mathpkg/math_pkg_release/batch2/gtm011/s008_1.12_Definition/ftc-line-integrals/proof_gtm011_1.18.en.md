---
role: proof
locale: en
of_concept: ftc-line-integrals
source_book: gtm011
source_chapter: "1"
source_section: "1.18"
---

The proof uses Lemma 1.19 (polygonal approximation). By Lemma 1.19, for every $\epsilon > 0$ there is a polygonal path $\Gamma$ in $G$ such that $\Gamma(a) = \gamma(a)$, $\Gamma(b) = \gamma(b)$, and

$$\left| \int_{\gamma} f - \int_{\Gamma} f \right| < \epsilon.$$

Since $\Gamma$ is a polygonal path, it is piecewise $C^1$. On each linear segment of $\Gamma$, say $\Gamma(t) = t v + (1-t) u$ for $t \in [0, 1]$, we have $\Gamma'(t) = v - u$. Then by the chain rule,

$$\frac{d}{dt} F(\Gamma(t)) = F'(\Gamma(t)) \Gamma'(t) = f(\Gamma(t)) \Gamma'(t).$$

Integrating over each segment and summing gives

$$\int_{\Gamma} f = F(\Gamma(b)) - F(\Gamma(a)) = F(\beta) - F(\alpha).$$

Thus

$$\left| \int_{\gamma} f - (F(\beta) - F(\alpha)) \right| = \left| \int_{\gamma} f - \int_{\Gamma} f \right| < \epsilon.$$

Since $\epsilon > 0$ is arbitrary, $\int_{\gamma} f = F(\beta) - F(\alpha)$.
