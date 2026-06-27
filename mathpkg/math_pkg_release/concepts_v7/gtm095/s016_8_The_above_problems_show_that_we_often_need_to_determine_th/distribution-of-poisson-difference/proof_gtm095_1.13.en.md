---
role: proof
locale: en
of_concept: distribution-of-poisson-difference
source_book: gtm095
source_chapter: "1"
source_section: "13"
---

# Proof of Distribution of the Difference of Independent Poisson Variables

Let $\xi_1 \sim \operatorname{Poisson}(\lambda_1)$ and $\xi_2 \sim \operatorname{Poisson}(\lambda_2)$ be independent with $\lambda_1, \lambda_2 > 0$. The generating function of a Poisson random variable is

$$G_{\xi_i}(x) = \mathbb{E}\, x^{\xi_i} = e^{-\lambda_i(1-x)}, \quad i = 1, 2.$$

By independence, the generating function of the difference $\xi_1 - \xi_2$ is

$$G_{\xi_1 - \xi_2}(x) = \mathbb{E}\, x^{\xi_1 - \xi_2} = \mathbb{E}\bigl[ x^{\xi_1} \cdot (1/x)^{\xi_2} \bigr] = G_{\xi_1}(x) \, G_{\xi_2}\!\left(\frac{1}{x}\right).$$

Substituting the Poisson generating functions:

$$G_{\xi_1 - \xi_2}(x) = e^{-\lambda_1(1-x)} \cdot e^{-\lambda_2(1-1/x)} = e^{-(\lambda_1 + \lambda_2) + \lambda_1 x + \lambda_2 / x}.$$

Introduce the variable $t = x\sqrt{\lambda_1/\lambda_2}$. Then

$$\lambda_1 x + \frac{\lambda_2}{x} = \lambda_1 x + \lambda_2 \cdot \frac{1}{x} = \sqrt{\lambda_1\lambda_2} \left( x\sqrt{\frac{\lambda_1}{\lambda_2}} + \frac{1}{x}\sqrt{\frac{\lambda_2}{\lambda_1}} \right) = \sqrt{\lambda_1\lambda_2} \left( t + \frac{1}{t} \right).$$

Thus

$$G_{\xi_1 - \xi_2}(x) = e^{-(\lambda_1 + \lambda_2)} \, e^{\sqrt{\lambda_1\lambda_2}\,(t + 1/t)}.$$

It is known from the theory of Bessel functions that for any $\lambda \in \mathbb{R}$,

$$e^{\lambda(t + 1/t)} = \sum_{k=-\infty}^{\infty} t^k \, I_k(2\lambda),$$

where $I_k(2\lambda)$ is the modified Bessel function of the first kind of order $k$:

$$I_k(2\lambda) = \lambda^k \sum_{r=0}^{\infty} \frac{\lambda^{2r}}{r! \, \Gamma(k + r + 1)}, \quad k = 0, \pm 1, \pm 2, \ldots$$

Applying this expansion with $\lambda = \sqrt{\lambda_1\lambda_2}$:

$$G_{\xi_1 - \xi_2}(x) = e^{-(\lambda_1 + \lambda_2)} \sum_{k=-\infty}^{\infty} t^k \, I_k\!\left(2\sqrt{\lambda_1\lambda_2}\right).$$

Since $t^k = \bigl(x\sqrt{\lambda_1/\lambda_2}\bigr)^k = x^k (\lambda_1/\lambda_2)^{k/2}$, we obtain

$$G_{\xi_1 - \xi_2}(x) = \sum_{k=-\infty}^{\infty} x^k \cdot e^{-(\lambda_1 + \lambda_2)} \left(\frac{\lambda_1}{\lambda_2}\right)^{k/2} I_k\!\left(2\sqrt{\lambda_1\lambda_2}\right).$$

By definition of the generating function, $G_{\xi_1 - \xi_2}(x) = \sum_{k=-\infty}^{\infty} P(\xi_1 - \xi_2 = k) \, x^k$. Comparing coefficients of $x^k$ yields the distribution:

$$P(\xi_1 - \xi_2 = k) = e^{-(\lambda_1 + \lambda_2)} \left(\frac{\lambda_1}{\lambda_2}\right)^{k/2} I_k\!\left(2\sqrt{\lambda_1\lambda_2}\right), \quad k = 0, \pm 1, \pm 2, \ldots$$

This distribution is known as the Skellam distribution.
