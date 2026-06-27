---
role: proof
locale: en
of_concept: uniform-convexity-norm-weak-convergence
source_book: gtm036
source_chapter: "5"
source_section: "17"
---

This is stated as Problem C(a) in the text. A proof sketch is provided: first prove the result when $\|x_\alpha\| = \|x_0\| = 1$ for all $\alpha$. Let $f$ be a continuous linear functional with $f(x_0) = 1$ and $\|f\| = 1$ (such an $f$ exists by the Hahn-Banach theorem). Then for each $\varepsilon > 0$, using the modulus of convexity $\delta(\varepsilon)$, one has

$$1 - \delta(\varepsilon) < \left|f\left(\frac{x_\alpha + x_0}{2}\right)\right| \leq \frac{1}{2}\|x_\alpha + x_0\|$$

eventually. Since the right-hand side is at most $\frac{1}{2}(\|x_\alpha\| + \|x_0\|) = 1$, the uniform convexity condition forces $\|x_\alpha - x_0\| < \varepsilon$ eventually, proving norm convergence. The general case follows by normalizing the vectors.
