---
role: proof
locale: en
of_concept: cauchy-product-eigenform-coefficients
source_book: gtm041
source_chapter: "6"
source_section: "6.13"
---

The eigenforms are constructed by multiplying the normalized discriminant $\Delta(\tau)$ by a suitable Eisenstein series. Since $\dim M_{2k,0}=1$ for the weights under consideration, any nonzero cusp form is an eigenform of all Hecke operators $T_n$.

Recall the Fourier expansions
$$
\Delta(\tau) = (2\pi)^{12} \sum_{n=1}^\infty \tau(n) x^n, \qquad
\frac{G_{2k}(\tau)}{2\zeta(2k)} = 1 - \frac{4k}{B_{2k}} \sum_{m=1}^\infty \sigma_{2k-1}(m) x^m,
$$
with $x = e^{2\pi i\tau}$.

The normalized eigenform is obtained from the product
$$
(2\pi)^{-12} \Delta(\tau) \cdot \frac{G_{2k-12}(\tau)}{2\zeta(2k-12)}.
$$

Expanding the product yields
$$
\Bigl(\sum_{n=1}^\infty \tau(n) x^n\Bigr)
\Bigl(1 - \frac{2(2k-12)}{B_{2k-12}}\sum_{m=1}^\infty \sigma_{2k-13}(m) x^m\Bigr).
$$

With the conventions $\tau(0)=0$ and $\sigma_{2k-1}(0)=-B_{2k}/(4k)$, the Cauchy product formula for the resulting series gives
$$
c(n) = -\frac{4k-24}{B_{2k-12}} \sum_{m=0}^n \tau(m) \, \sigma_{2k-13}(n-m).
$$

Because the Hecke eigenvalues are multiplicative and the coefficients $c(n)$ are (up to normalization) the eigenvalues of $T_n$, they inherit the multiplicativity property: for all $m,n\ge 1$,
$$
c(m) c(n) = \sum_{d\mid (m,n)} d^{2k-1} \, c\!\left(\frac{mn}{d^2}\right).
$$
This follows from the formal identity for Hecke eigenforms and the fact that the Dirichlet series $\sum c(n) n^{-s}$ admits an Euler product.
