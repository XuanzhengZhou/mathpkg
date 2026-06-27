---
role: proof
locale: en
of_concept: lemma-48b6ddede9
source_book: gtm077
source_chapter: "VIII"
source_section: "§57"
---
# Proof of Lemma (a): Limit of the Theta Function as $t \to 0$

**Statement.** Let $\sigma_1(t_1), \sigma_2(t_2), \ldots, \sigma_n(t_n)$ be functions of $t_1, \ldots, t_n$ respectively such that $\sigma_{p+r_2} = \bar{\sigma}_p$ for $p = r_1 + 1, \ldots, r_1 + r_2$ and $\sigma_p$ is real for $p = 1, 2, \ldots, r_1$. If $t_1, \ldots, t_n$ tend to $0$ simultaneously, then

$$\lim_{t \to 0} \sqrt{t_1 t_2 \cdots t_n} \, \theta(t, z, t \cdot \sigma; \mathfrak{f}) = \frac{1}{N(\mathfrak{f})|\sqrt{d}|},$$

independently of $z$, provided $\lim_{t_p \to 0} \sigma_p(t_p) = 0$.

**Proof.** Apply Theorem 158 to the theta series defined in (185):

$$\theta(t, z, t\cdot\sigma; \mathfrak{f}) = \sum_{\mu \in \mathfrak{f}} \exp\left\{-\pi \sum_{p=1}^{n} \left[ t_p |\mu^{(p)} + z_p|^2 - 2i \, t_p \sigma_p(t_p) (\mu^{(p)} + z_p)^2 \right]\right\}.$$

As $t \to 0$, the condition $\sigma_p(t_p) \to 0$ ensures that $\omega^{(p)} = t_p \sigma_p(t_p)$ tends to $0$ faster than $t_p$, i.e., $\omega^{(p)} = o(t_p)$. By the transformation formula established in Theorem 158 (the Poisson summation formula for the theta function), the series decomposes into a sum over residue classes $\rho$ modulo $\mathfrak{f}$:

$$\theta(t, z, t \cdot \sigma; \mathfrak{f}) = \sum_{\rho \bmod \mathfrak{f}} e^{2\pi i S(\rho^2 t \sigma)} \, \theta(t, \rho + z, 0; \mathfrak{f}).$$

For each fixed shift, the Gaussian integral computation carried out before the statement of Lemma (a) shows that

$$\lim_{t \to 0} \sqrt{t_1 \cdots t_n} \, \theta(t, \rho + z, 0; \mathfrak{f}) = \frac{1}{N(\mathfrak{f})|\sqrt{d}|}.$$

The key point is that the integral

$$\int_{-\infty}^{\infty} \exp\left\{-\pi(t_p - 2i\omega^{(p)})x^2 + 2\pi i \lambda^{(p)} x\right\} dx$$

(for each real component $p = 1, \ldots, r_1$) and the analogous double integrals for the complex conjugate pairs $(p, p+r_2)$ all yield leading terms that are independent of the linear coefficient $\lambda$ (and hence of $z$). When $\omega = t\sigma \to 0$, the factor $t_p - 2i\omega^{(p)}$ tends to $0$ with leading real part $t_p$, and the Gaussian integral evaluates to $1/\sqrt{t_p}$ times a factor that approaches $1$ as $\omega \to 0$. Multiplying by the functional determinant $2^{r_2}/|N(\mathfrak{f})\sqrt{d}|$ and the product $\sqrt{t_1 \cdots t_n}$ yields exactly the stated constant.

Since the exponential factor $e^{2\pi i S(\rho^2 t \sigma)}$ tends to $1$ as $t \to 0$ (because $t\sigma \to 0$), the sum over residue classes simply adds $N(\mathfrak{f})$ copies of the same limit, giving the result $1/(N(\mathfrak{f})|\sqrt{d}|)$, independent of $z$. $\square$
