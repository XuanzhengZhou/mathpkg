---
role: proof
locale: en
of_concept: gamma-integral-bounds
source_book: gtm011
source_chapter: "7"
source_section: "7.16"
---

**Proof of (a).** If $0 < t \leq 1$ and $z \in S$, then $(\operatorname{Re} z - 1) \log t \leq (a-1) \log t$. Since $e^{-t} \leq 1$, we have

$$|e^{-t} t^{z-1}| \leq t^{\operatorname{Re} z - 1} \leq t^{a-1}.$$

So if $0 < \alpha < \beta < 1$, then

$$\left| \int_{\alpha}^{\beta} e^{-t} t^{z-1} \, dt \right| \leq \int_{\alpha}^{\beta} t^{a-1} \, dt = \frac{1}{a} (\beta^a - \alpha^a)$$

for all $z \in S$. Given $\epsilon > 0$, we can choose $\delta$ with $0 < \delta < 1$ such that $a^{-1}(\beta^a - \alpha^a) < \epsilon$ whenever $|\alpha - \beta| < \delta$. This proves part (a).

**Proof of (b).** For $z \in S$ and $t \geq 1$, we have $|t^{z-1}| \leq t^{A-1}$. The function $t^{A-1} \exp(-t/2)$ is continuous on $[1, \infty)$ and tends to $0$ as $t \to \infty$, hence is bounded. Writing $e^{-t} t^{z-1} = e^{-t/2} \cdot e^{-t/2} t^{z-1}$ and using the bound on $t^{A-1} e^{-t/2}$, the tail integral can be made arbitrarily small uniformly for $z \in S$ by choosing $\kappa$ sufficiently large.
