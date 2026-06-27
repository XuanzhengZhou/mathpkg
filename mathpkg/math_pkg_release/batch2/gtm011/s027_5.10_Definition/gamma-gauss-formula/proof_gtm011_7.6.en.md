---
role: proof
locale: en
of_concept: gamma-gauss-formula
source_book: gtm011
source_chapter: "7"
source_section: "7.6"
---

Starting from the Weierstrass product representation

$$\frac{1}{\Gamma(z)} = z e^{\gamma z} \prod_{n=1}^{\infty} \left(1 + \frac{z}{n}\right) e^{-z/n},$$

consider the partial products. Using that

$$e^{-\gamma z} \exp\left[\left(1 + \frac{1}{2} + \cdots + \frac{1}{n}\right)z\right] = n^z \exp\left[z\left(-\gamma + 1 + \frac{1}{2} + \cdots + \frac{1}{n} - \log n\right)\right],$$

and the fact that the exponent tends to $0$ as $n \to \infty$ (by definition of Euler's constant), we obtain

$$\Gamma(z) = \lim_{n \to \infty} \frac{n! \, n^z}{z(z+1) \cdots (z+n)}$$

for all $z \neq 0, -1, -2, \ldots$.
