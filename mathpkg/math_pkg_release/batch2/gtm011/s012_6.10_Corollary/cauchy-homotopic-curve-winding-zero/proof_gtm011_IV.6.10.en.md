---
role: proof
locale: en
of_concept: cauchy-homotopic-curve-winding-zero
source_book: gtm011
source_chapter: "IV"
source_section: "6.10"
---

The result follows immediately from the second version of Cauchy's Theorem by letting $\gamma_1$ be a constant path in equation (6.7). Specifically, if $\gamma \sim 0$ and $\gamma_1$ is a constant path (so that $\int_{\gamma_1} f = 0$ for any analytic $f$), then Cauchy's Theorem (second version) gives

$$\int_{\gamma} f = \int_{\gamma_1} f = 0$$

for every analytic function $f$ on $G$. Applying this to the function $f(z) = \frac{1}{z - w}$ for $w \in \mathbb{C} - G$ (which is analytic on $G$ since $w \notin G$) yields

$$n(\gamma; w) = \frac{1}{2\pi i} \int_{\gamma} \frac{dz}{z - w} = 0.$$

Note that the converse is false: there exist closed rectifiable curves $\gamma$ in a region $G$ with $n(\gamma; w) = 0$ for all $w \in \mathbb{C} - G$ that are not homotopic to a constant curve (see Exercise 8).
