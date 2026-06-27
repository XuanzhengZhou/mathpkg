---
role: proof
locale: en
of_concept: uniform-convergence-zeta-integral
source_book: gtm011
source_chapter: "8"
source_section: "8.4"
---

The proof of Corollary 8.4 follows from Lemma 8.3, which provides the existence of numbers $\alpha, \beta$ with $0 < \alpha < \beta < \infty$ such that the integrals over $(0, \alpha]$ and $[\beta, \infty)$ can be made arbitrarily small. For part (a), on the compact vertical strip $S = \{z : a \leq \operatorname{Re} z \leq A\}$ with $1 < a < A < \infty$, one bounds $|t^{z-1}| = t^{\operatorname{Re} z - 1}$ and uses the uniform bounds from Lemma 8.3 to control the tails. For part (b), on the left half-plane $S = \{z : \operatorname{Re} z \leq A\}$, the integral over $[1, \infty)$ is controlled since $t^{\operatorname{Re} z - 1} \leq t^{A-1}$ for $t \geq 1$, and the exponential decay of $(e^t-1)^{-1}$ ensures uniform convergence through the Weierstrass M-test combined with the estimates from Lemma 8.3.
