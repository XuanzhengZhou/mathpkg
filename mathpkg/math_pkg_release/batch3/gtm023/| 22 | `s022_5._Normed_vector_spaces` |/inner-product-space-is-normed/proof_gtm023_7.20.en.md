---
role: proof
locale: en
of_concept: inner-product-space-is-normed
source_book: gtm023
source_chapter: "VII"
source_section: "5 (7.20)"
---

We verify the three norm axioms. $N_1$: Since $(x,x) \geq 0$ by positive definiteness of the inner product, $\|x\| = \sqrt{(x,x)} \geq 0$, and $\|x\| = 0$ iff $(x,x) = 0$ iff $x = 0$.

$N_2$: By the Cauchy-Schwarz inequality $|(x,y)| \leq \sqrt{(x,x)}\sqrt{(y,y)}$, we have
$$\|x+y\|^2 = (x+y, x+y) = (x,x) + 2(x,y) + (y,y) \leq \|x\|^2 + 2\|x\|\cdot\|y\| + \|y\|^2 = (\|x\| + \|y\|)^2.$$
Taking square roots yields $\|x+y\| \leq \|x\| + \|y\|$.

$N_3$: $\|\lambda x\| = \sqrt{(\lambda x, \lambda x)} = \sqrt{\lambda^2 (x,x)} = |\lambda| \cdot \|x\|$.
