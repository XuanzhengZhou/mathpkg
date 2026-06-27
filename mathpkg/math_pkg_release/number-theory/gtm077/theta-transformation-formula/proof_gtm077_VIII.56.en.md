---
role: proof
locale: en
of_concept: theta-transformation-formula
source_book: gtm077
source_chapter: "VIII"
source_section: "56"
---

# Proof of Theorem 159: Transformation Formula for Theta Functions

We consider a totally real algebraic number field $k$ of degree $n$. Let $\mathfrak{a} \neq 0$ be an ideal in $k$ with basis $\alpha_1, \ldots, \alpha_n$. Let $t_1, \ldots, t_n$ be $n$ positive real variables. We choose the quadratic form $Q$ of Theorem 158 as

$$Q(x_1, \ldots, x_n) = \sum_{p=1}^{n} t_p(\alpha_1^{(p)}x_1 + \cdots + \alpha_n^{(p)}x_n)^2,$$

which is obviously positive definite since each $t_p > 0$ and the conjugates $\alpha_k^{(p)}$ are real.

The corresponding theta-function, depending on $n$ complex parameters $z_1, \ldots, z_n$ related to real variables $u_1, \ldots, u_n$ by

$$z_p = \sum_{q=1}^{n} \alpha_q^{(p)}u_q \quad (p=1, \ldots, n),$$

is defined as

$$\theta(t, z; \mathfrak{a}) = \sum_{\mu \text{ in } \mathfrak{a}} \exp \left\{ -\pi \sum_{p=1}^{n} t_p(\mu^{(p)} + z_p)^2 \right\}. \tag{175}$$

In the series (175), $\mu$ runs through all numbers in $\mathfrak{a}$ exactly once.

By Theorem 102, the numbers $\beta_1, \ldots, \beta_n$ form a basis for the ideal $1/\mathfrak{a}\mathfrak{d}$ in $k$. The periodic function

$$T(u_1, \ldots, u_n) = \sum_{m_1, \ldots, m_n = -\infty}^{+\infty} a((m))e^{-2\pi i(m_1u_1 + \cdots + m_nu_n)}$$

admits the Fourier expansion with coefficients

$$a((m)) = a(m_1, \ldots, m_n)$$

$$= \int_{-\infty}^{+\infty} \cdots \int e^{-\pi Q(u_1, \ldots, u_n) + 2\pi i(m_1u_1 + \cdots + m_nu_n)} du_1 du_2 \cdots du_n.$$

We now relate the Fourier sum to the numbers in the reciprocal ideal. Observe that

$$\sum_{k=1}^{n} m_k u_k = \sum_{p=1}^{n} \lambda^{(p)} z_p$$

where $\lambda = \sum_{k=1}^{n} \beta_k m_k$ is a number from $1/\mathfrak{a}\mathfrak{d}$. This follows from the fact that $\beta_1, \ldots, \beta_n$ is the dual basis.

Making this substitution, the Fourier coefficient becomes

$$a((m)) = \frac{1}{|N(\mathfrak{a})\sqrt{d}|} \int_{-\infty}^{+\infty} \cdots \int \exp \left\{ -\pi \sum_{p=1}^{n} t_p z_p^2 + 2\pi i \sum_{p=1}^{n} \lambda^{(p)} z_p \right\} dz_1 \cdots dz_n,$$

where $d$ is the discriminant and the Jacobian of the change of variables $u \mapsto z$ contributes the factor $1/|N(\mathfrak{a})\sqrt{d}|$.

Now for positive $t$ and real $\lambda$, the Gaussian integral evaluates as

$$\int_{-\infty}^{+\infty} e^{-\pi t z^2 + 2\pi i \lambda z} dz = e^{-\pi \lambda^2/t} \int_{-\infty}^{+\infty} e^{-\pi t(z-i\lambda/t)^2} dz = \frac{e^{-\pi \lambda^2/t}}{\sqrt{t}},$$

where $\sqrt{t}$ denotes the positive square root.

Since the integral in $a((m))$ factorizes into a product of $n$ independent Gaussian integrals (one for each $p = 1, \ldots, n$), we obtain

$$a((m)) = \frac{1}{N(\mathfrak{a})|\sqrt{d}| \sqrt{t_1 t_2 \cdots t_n}} \exp\left\{ -\pi \sum_{p=1}^{n} \frac{\lambda^{(p)^2}}{t_p} \right\}.$$

Summing over all $m_1, \ldots, m_n$ (equivalently, over all $\lambda \in 1/\mathfrak{a}\mathfrak{b}$, where $\mathfrak{b} = \mathfrak{d}$ in this context), we obtain the dual representation:

$$\theta(t, z; \mathfrak{a}) = \frac{1}{N(\mathfrak{a})|\sqrt{d}| \sqrt{t_1 \cdot t_2 \cdots t_n}} \sum_{\lambda \text{ in } 1/\mathfrak{a}\mathfrak{b}} \exp \left\{ -\pi \sum_{p=1}^{n} \frac{\lambda^{(p)^2}}{t_p} - 2\pi i \sum_{p=1}^{n} \lambda^{(p)} z_p \right\}.$$

This is the transformation formula of Theorem 159: the theta-function admits a dual representation summing over the reciprocal ideal $1/\mathfrak{a}\mathfrak{b}$, with the two representations related by the transformation $t_p \mapsto 1/t_p$ in the exponent. Setting $z = 0$, this specializes to the identity

$$\theta(t; \mathfrak{f}) = \theta(t, 0; \mathfrak{f}) = \sum_{\mu \in \mathfrak{f}} \exp \left\{ -\pi \sum_{p=1}^{n} t_p \mu^{(p)^2} \right\}$$

and its dual.
