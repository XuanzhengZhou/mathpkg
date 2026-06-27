---
role: proof
locale: en
of_concept: "let-and-be-as-in-83-suppose-that"
source_book: gtm025
source_chapter: "Riemann-Stieltjes Integral"
source_section: "8.4"
---

Let $\gamma = \sup \{L(f, \alpha, \Delta) : \Delta \in \mathcal{D}([a, b])\}$ and $\delta = \inf \{U(f, \alpha, \Delta) : \Delta \in \mathcal{D}([a, b])\}$. It follows from (8.5) that $\gamma$ and $\delta$ are real numbers and that $\gamma \leq \delta$. We need only show that $\gamma = \delta$. Assume that $\gamma < \delta$. Since $\delta - \gamma > 0$, the definition of integrability (8.3) shows that there is a $\Delta \in \mathcal{D}([a, b])$ such that $U(f, \alpha, \Delta) - L(f, \alpha, \Delta) < \delta - \gamma$. Then

$$\delta \leq U(f, \alpha, \Delta) = (U(f, \alpha, \Delta) - L(f, \alpha, \Delta)) + L(f, \alpha, \Delta) < (\delta - \gamma) + \gamma = \delta,$$

a clear contradiction. Thus $\gamma = \delta$.
