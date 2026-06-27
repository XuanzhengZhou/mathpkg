---
role: proof
locale: en
of_concept: gamma-logarithmic-derivative
source_book: gtm011
source_chapter: "7"
source_section: "7.11"
---

From the Weierstrass product representation

$$\frac{1}{\Gamma(z)} = z e^{\gamma z} \prod_{n=1}^{\infty} \left(1 + \frac{z}{n}\right) e^{-z/n},$$

take the logarithm:

$$-\log \Gamma(z) = \log z + \gamma z + \sum_{n=1}^{\infty} \left[ \log\left(1 + \frac{z}{n}\right) - \frac{z}{n} \right].$$

Differentiating term by term (justified by uniform convergence on compact sets avoiding the poles) gives

$$-\frac{\Gamma'(z)}{\Gamma(z)} = \frac{1}{z} + \gamma + \sum_{n=1}^{\infty} \left[ \frac{1/n}{1 + z/n} - \frac{1}{n} \right] = \frac{1}{z} + \gamma + \sum_{n=1}^{\infty} \left[ \frac{1}{n+z} - \frac{1}{n} \right].$$

Simplifying the series:

$$\sum_{n=1}^{\infty} \left( \frac{1}{n+z} - \frac{1}{n} \right) = \sum_{n=1}^{\infty} \frac{-z}{n(n+z)}.$$

Therefore,

$$\frac{\Gamma'(z)}{\Gamma(z)} = -\gamma - \frac{1}{z} + \sum_{n=1}^{\infty} \frac{z}{n(n+z)}.$$
