---
role: proof
locale: en
of_concept: cauchy-product-eigenform-coefficients
source_book: gtm041
source_chapter: "6"
source_section: "6.14"
---

The normalized eigenform in $M_{2k,0}$ (for $2k \geq 16$) is given by the product
$$(2\pi)^{-12}\Delta(\tau) \cdot \frac{G_{2k-12}(\tau)}{2\zeta(2k-12)}.$$

Writing each factor as a Fourier series with $x = e^{2\pi i\tau}$,
$$\Delta(\tau) = (2\pi)^{12} \sum_{n=1}^{\infty} \tau(n) x^n,$$
$$\frac{G_{2k-12}(\tau)}{2\zeta(2k-12)} = 1 - \frac{2(2k-12)}{B_{2k-12}} \sum_{m=1}^{\infty} \sigma_{2k-13}(m) x^m.$$

The product of these two series gives the Fourier expansion of the eigenform. Setting $\tau(0) = 0$ and $\sigma_{2k-1}(0) = -B_{2k}/(4k)$, the coefficient $c(n)$ is given by the Cauchy product of the two series:
$$c(n) = -\frac{4k-24}{B_{2k-12}} \sum_{m=0}^{n} \tau(m) \sigma_{2k-13}(n-m).$$

Because both $\Delta$ and the normalized Eisenstein series are eigenfunctions of all Hecke operators, their product is also an eigenfunction, and its coefficients satisfy the multiplicative property
$$c(m)c(n) = \sum_{d \mid (m,n)} d^{2k-1} c\left(\frac{mn}{d^2}\right).$$
