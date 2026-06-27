---
role: proof
locale: en
of_concept: prehilbert-implies-innerproduct
source_book: gtm015
source_chapter: "41"
source_section: "Hilbert spaces"
---

# Proof of Every pre-Hilbert space is an inner product space

Let $E$ be a pre-Hilbert space, i.e., a normed space whose norm satisfies the parallelogram law

$$\|x + y\|^2 + \|x - y\|^2 = 2\|x\|^2 + 2\|y\|^2 \qquad \text{for all } x, y \in E.$$

**Real case.**  Define $(x, y) = \frac{1}{4}\{\|x+y\|^2 - \|x-y\|^2\}$.  Theorem 41.5 shows that $(\cdot,\cdot)$ is a symmetric, positive definite, bilinear form on $E$ — that is, a real inner product.  Hence $E$ is a real inner product space.

**Complex case.**  Define

$$(x|y) = \frac{1}{4}\Bigl\{\|x+y\|^2 - \|x-y\|^2 + i\|x+iy\|^2 - i\|x-iy\|^2\Bigr\}.$$

Theorem 41.6 shows that $(\cdot|\cdot)$ is a Hermitian, positive definite, sesquilinear form on $E$ — that is, a complex inner product.  Hence $E$ is a complex inner product space.

In both cases, the pre-Hilbert space structure yields an inner product via the polarization formulas of (41.4).  $\square$
