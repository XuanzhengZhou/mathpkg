---
role: proof
locale: en
of_concept: gamma-trigamma-derivative
source_book: gtm011
source_chapter: "7"
source_section: "7.12"
---

Starting from the logarithmic derivative formula (7.11):

$$\frac{\Gamma'(z)}{\Gamma(z)} = -\gamma - \frac{1}{z} + \sum_{n=1}^{\infty} \frac{z}{n(n+z)}.$$

By Theorem 2.1, to calculate the derivative we may differentiate the series term by term (justified because convergence is uniform on compact sets avoiding the poles). Differentiating:

$$\left( \frac{\Gamma'(z)}{\Gamma(z)} \right)' = \frac{d}{dz} \left( -\gamma - \frac{1}{z} \right) + \sum_{n=1}^{\infty} \frac{d}{dz} \left( \frac{z}{n(n+z)} \right)$$

$$= \frac{1}{z^2} + \sum_{n=1}^{\infty} \frac{n(n+z) - z \cdot n}{n^2 (n+z)^2} = \frac{1}{z^2} + \sum_{n=1}^{\infty} \frac{n^2 + nz - nz}{n^2 (n+z)^2}$$

$$= \frac{1}{z^2} + \sum_{n=1}^{\infty} \frac{1}{(n+z)^2}.$$
