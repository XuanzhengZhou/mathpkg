---
role: proof
locale: en
of_concept: jacobi-delta-product
source_book: gtm007
source_chapter: "VII"
source_section: "1"
---

**Sketch of proof (elementary approach of Hurwitz).** Set
$$F(z) = q \prod_{n=1}^{\infty} (1 - q^n)^{24}, \qquad q = e^{2\pi i z}.$$
To prove $F$ and $(2\pi)^{-12} \Delta$ are proportional, it suffices to show $F$ is a modular form of weight 12; indeed, the constant term of its $q$-expansion is zero, so $F$ is a cusp form, and by Theorem 4 the space $M_6^0$ of cusp forms of weight 12 is one-dimensional.

Consider the logarithmic derivative:
$$\frac{dF}{F} = \frac{dq}{q} \left(1 - 24 \sum_{n,m=1}^{\infty} n q^{nm}\right) = \frac{dq}{q} \left(1 - 24 \sum_{n=1}^{\infty} \sigma_1(n) q^n\right).$$

Now, consider the auxiliary series
$$G_1(z) = \sum_{m \in \mathbf{Z}} \sum_{n \in \mathbf{Z}} {}' \frac{1}{(mz+n)(mz+n-1)},$$
where the summation is carried out by grouping terms with the same denominator. A careful analysis of this conditionally convergent series gives the transformation formula
$$G_1(-1/z) = z^2 G_1(z) - 2\pi i z.$$
A computation similar to that of Proposition 8 yields
$$G_1(z) = \frac{\pi^2}{3} - 8\pi^2 \sum_{n=1}^{\infty} \sigma_1(n) q^n.$$

Comparing with the logarithmic derivative of $F$, one obtains
$$\frac{dF}{F} = \frac{6i}{\pi} G_1(z) dz,$$
from which the transformation formula for $G_1$ implies that $F(-1/z) = z^{12} F(z)$. Since $F(z+1) = F(z)$ is obvious from $q = e^{2\pi i z}$, $F$ is weakly modular of weight 12. Holomorphy on $H$ and at infinity is clear from the product definition. Hence $F \in M_6^0$, so $F$ is a constant multiple of $(2\pi)^{-12} \Delta$. Comparing the first term of the $q$-expansion gives the constant factor.
