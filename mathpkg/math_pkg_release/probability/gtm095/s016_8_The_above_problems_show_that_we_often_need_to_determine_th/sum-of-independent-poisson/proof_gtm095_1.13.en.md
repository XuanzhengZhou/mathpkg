---
role: proof
locale: en
of_concept: sum-of-independent-poisson
source_book: gtm095
source_chapter: "1"
source_section: "13"
---

# Proof of Sum of Independent Poisson Random Variables

Let $\xi_1$ and $\xi_2$ be two independent random variables having the Poisson distributions with parameters $\lambda_1 > 0$ and $\lambda_2 > 0$ respectively:

$$P(\xi_i = k) = \frac{\lambda_i^k e^{-\lambda_i}}{k!}, \quad k = 0, 1, 2, \ldots, \quad i = 1, 2.$$

The generating function $G_{\xi_i}(x)$ for $|x| \leq 1$ is

$$G_{\xi_i}(x) = \mathbb{E}\, x^{\xi_i} = \sum_{k=0}^{\infty} P(\xi_i = k) \, x^k = \sum_{k=0}^{\infty} \frac{\lambda_i^k e^{-\lambda_i}}{k!} \, x^k = e^{-\lambda_i} \sum_{k=0}^{\infty} \frac{(\lambda_i x)^k}{k!} = e^{-\lambda_i(1-x)}.$$

By independence of $\xi_1$ and $\xi_2$, the generating function of the sum $\xi_1 + \xi_2$ is the product of the individual generating functions:

$$G_{\xi_1 + \xi_2}(x) = \mathbb{E}\, x^{\xi_1 + \xi_2} = \mathbb{E}\bigl[x^{\xi_1} x^{\xi_2}\bigr] = \mathbb{E}\, x^{\xi_1} \cdot \mathbb{E}\, x^{\xi_2} = G_{\xi_1}(x) \, G_{\xi_2}(x).$$

Substituting the expressions for $G_{\xi_1}$ and $G_{\xi_2}$:

$$G_{\xi_1 + \xi_2}(x) = e^{-\lambda_1(1-x)} \cdot e^{-\lambda_2(1-x)} = e^{-(\lambda_1 + \lambda_2)(1-x)}.$$

This is exactly the generating function of a Poisson random variable with parameter $\lambda_1 + \lambda_2$. Since the generating function uniquely determines the distribution, we conclude

$$\xi_1 + \xi_2 \sim \operatorname{Poisson}(\lambda_1 + \lambda_2).$$

By induction, if $\xi_1, \ldots, \xi_n$ are independent with $\xi_i \sim \operatorname{Poisson}(\lambda_i)$, then

$$\sum_{i=1}^{n} \xi_i \sim \operatorname{Poisson}\!\left(\sum_{i=1}^{n} \lambda_i\right).$$
