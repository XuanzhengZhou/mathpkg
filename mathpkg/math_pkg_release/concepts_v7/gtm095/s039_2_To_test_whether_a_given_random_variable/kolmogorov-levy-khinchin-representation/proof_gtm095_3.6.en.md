---
role: proof
locale: en
of_concept: kolmogorov-levy-khinchin-representation
source_book: gtm095
source_chapter: "3"
source_section: "§6. Infinitely divisible and stable distributions"
---

# Kolmogorov–Lévy–Khinchin Representation (Proof Omitted)

The textbook (GTM 095, Probability-1, 3rd ed., A.N. Shiryaev) states this theorem without proof:

> We quote without proof the following result on the general form of the characteristic functions of infinitely divisible distributions.

**Theorem.** A random variable $T$ is infinitely divisible if and only if its characteristic function has the form $\varphi(t) = \exp \psi(t)$ with

$$\psi(t) = i t \beta - \frac{t^2 \sigma^2}{2} + \int_{-\infty}^{\infty} \left( e^{i t x} - 1 - \frac{i t x}{1 + x^2} \right) \frac{1 + x^2}{x^2} \, d\lambda(x),$$

where $\beta \in \mathbb{R}$, $\sigma^2 \geq 0$, and $\lambda$ is a measure on $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$ with $\lambda\{0\} = 0$, and

$$\int_{-\infty}^{\infty} \frac{x^2}{1 + x^2} \, d\lambda(x) < \infty.$$

The measure $\lambda$ is called the **Lévy measure**.

The proof of this deep result can be found in specialized monographs on limit theorems and infinitely divisible distributions, such as:

- B.V. Gnedenko and A.N. Kolmogorov, *Limit Distributions for Sums of Independent Random Variables*, Addison-Wesley, 1954.
- K. Sato, *Lévy Processes and Infinitely Divisible Distributions*, Cambridge University Press, 1999.
