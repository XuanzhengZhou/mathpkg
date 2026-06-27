---
role: proof
locale: en
of_concept: prehilbert-innerproduct-equivalence
source_book: gtm015
source_chapter: "41"
source_section: "Hilbert spaces"
---

# Proof of Equivalence of pre-Hilbert spaces and inner product spaces

We prove the assertions for the complex case; the real case is entirely analogous.

**(i) Pre-Hilbert $\Rightarrow$ inner product, and back.**  Suppose $E$ is a complex pre-Hilbert space, i.e., a normed space whose norm satisfies the parallelogram law.  Theorem 41.6 provides $E$ with an inner product $(x|y)$ defined by the polarization formula (41.4)(2).  Apply Theorem 41.11 to this inner product: the norm $\|x\|' = (x|x)^{1/2}$ satisfies

$$\|x\|'^2 = (x|x) = \|x\|^2 \qquad \text{(by 41.6(i)),}$$

so $\|\cdot\|'$ coincides with the original norm.  Thus the round-trip (pre-Hilbert $\to$ inner product $\to$ pre-Hilbert) recovers the original norm.

**(ii) Inner product $\Rightarrow$ pre-Hilbert, and back.**  Suppose $E$ is a complex inner product space, with inner product $(x|y)$.  Theorem 41.11 yields a norm $\|x\| = (x|x)^{1/2}$ satisfying the parallelogram law, i.e., $E$ becomes a pre-Hilbert space.  Apply the polarization formula (41.4)(2) to this norm:

$$
\begin{aligned}
&\frac{1}{4}\Bigl\{\|x+y\|^2 - \|x-y\|^2 + i\|x+iy\|^2 - i\|x-iy\|^2\Bigr\} \\
&= \frac{1}{4}\Bigl\{(x+y|x+y) - (x-y|x-y) + i(x+iy|x+iy) - i(x-iy|x-iy)\Bigr\}.
\end{aligned}
$$

Expanding each term sesquilinearly and cancelling yields $(x|y)$; one verifies easily that the original inner product is recovered.  Thus the round-trip (inner product $\to$ pre-Hilbert $\to$ inner product) recovers the original inner product.

The two constructions are mutual inverses.  Consequently, the notions of **pre-Hilbert space** and **inner product space** are coextensive, and the terms may be used interchangeably.  $\square$
