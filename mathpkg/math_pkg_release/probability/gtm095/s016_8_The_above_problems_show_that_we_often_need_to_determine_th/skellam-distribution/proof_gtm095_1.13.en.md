---
role: proof
locale: en
of_concept: skellam-distribution
source_book: gtm095
source_chapter: "1"
source_section: "13"
---

# Proof of Distribution of the Difference of Independent Poisson Random Variables

Let $\xi_1 \sim \operatorname{Poisson}(\lambda_1)$ and $\xi_2 \sim \operatorname{Poisson}(\lambda_2)$ be independent random variables with $\lambda_1, \lambda_2 > 0$. We seek the distribution of the difference $\xi_1 - \xi_2$, which takes integer values $k = 0, \pm 1, \pm 2, \ldots$

The generating function of a $\operatorname{Poisson}(\lambda)$ random variable is

$$G(x) = \mathbb{E}\, x^{\xi} = e^{-\lambda(1-x)}, \quad |x| \leq 1.$$

Hence

$$G_{\xi_1}(x) = e^{-\lambda_1(1-x)}, \qquad G_{\xi_2}(x) = e^{-\lambda_2(1-x)}.$$

By independence, the generating function of the difference is

$$G_{\xi_1 - \xi_2}(x) = \mathbb{E}\, x^{\xi_1 - \xi_2} = \mathbb{E}\bigl[ x^{\xi_1} \cdot x^{-\xi_2} \bigr] = G_{\xi_1}(x) \, G_{\xi_2}\!\left(\frac{1}{x}\right).$$

Substituting the Poisson generating functions:

$$G_{\xi_1 - \xi_2}(x) = e^{-\lambda_1(1-x)} \cdot e^{-\lambda_2(1-1/x)} = e^{-(\lambda_1 + \lambda_2) + \lambda_1 x + \lambda_2/x}.$$

Introduce the change of variable $t = x\sqrt{\lambda_1/\lambda_2}$. Then

$$\lambda_1 x + \frac{\lambda_2}{x} = \sqrt{\lambda_1\lambda_2} \left( x\sqrt{\frac{\lambda_1}{\lambda_2}} + \frac{1}{x}\sqrt{\frac{\lambda_2}{\lambda_1}} \right) = \sqrt{\lambda_1\lambda_2} \left( t + \frac{1}{t} \right).$$

Therefore

$$G_{\xi_1 - \xi_2}(x) = e^{-(\lambda_1 + \lambda_2)} \, \exp\!\left( \sqrt{\lambda_1\lambda_2} \, \bigl(t + t^{-1}\bigr) \right).$$

A classical expansion from the theory of Bessel functions states that for any real $\lambda$,

$$e^{\lambda(t + 1/t)} = \sum_{k=-\infty}^{\infty} t^k \, I_k(2\lambda),$$

where $I_k$ is the modified Bessel function of the first kind of order $k$, defined by

$$I_k(2\lambda) = \lambda^k \sum_{r=0}^{\infty} \frac{\lambda^{2r}}{r! \, \Gamma(k + r + 1)}, \quad k = 0, \pm 1, \pm 2, \ldots$$

with the convention $I_{-k}(z) = I_k(z)$. Applying this with $\lambda = \sqrt{\lambda_1\lambda_2}$:

$$G_{\xi_1 - \xi_2}(x) = e^{-(\lambda_1 + \lambda_2)} \sum_{k=-\infty}^{\infty} t^k \, I_k\!\left(2\sqrt{\lambda_1\lambda_2}\right).$$

Since $t^k = \bigl(x\sqrt{\lambda_1/\lambda_2}\bigr)^k = x^k (\lambda_1/\lambda_2)^{k/2}$, we obtain

$$G_{\xi_1 - \xi_2}(x) = \sum_{k=-\infty}^{\infty} x^k \cdot e^{-(\lambda_1 + \lambda_2)} \left(\frac{\lambda_1}{\lambda_2}\right)^{k/2} I_k\!\left(2\sqrt{\lambda_1\lambda_2}\right).$$

By definition, the generating function of the integer-valued random variable $\xi_1 - \xi_2$ is

$$G_{\xi_1 - \xi_2}(x) = \sum_{k=-\infty}^{\infty} P(\xi_1 - \xi_2 = k) \, x^k.$$

Comparing coefficients yields the **Skellam distribution**:

$$P(\xi_1 - \xi_2 = k) = e^{-(\lambda_1 + \lambda_2)} \left(\frac{\lambda_1}{\lambda_2}\right)^{k/2} I_k\!\left(2\sqrt{\lambda_1\lambda_2}\right), \quad k = 0, \pm 1, \pm 2, \ldots$$

This distribution is symmetric in the sense that exchanging $\lambda_1$ and $\lambda_2$ and replacing $k$ by $-k$ leaves the probability unchanged, as expected from the symmetry $\xi_1 - \xi_2 = -(\xi_2 - \xi_1)$.
