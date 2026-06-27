---
role: proof
locale: en
of_concept: exponential-orthonormal-basis-of-l2
source_book: gtm012
source_chapter: "6"
source_section: "§6. Fourier series"
---

# Proof of The exponential functions form an orthonormal basis for L^2

**Proof.** Clearly $\|e_n\| = 1$ for each $n$, since

$$\|e_n\|^2 = \frac{1}{2\pi} \int_0^{2\pi} |e^{inx}|^2 \, dx = \frac{1}{2\pi} \int_0^{2\pi} 1 \, dx = 1.$$

If $m \neq n$, then

$$\int_0^{2\pi} e_n(x) \overline{e_m(x)} \, dx = \int_0^{2\pi} \exp(inx - imx) \, dx = \frac{1}{i(n-m)} \exp(i(n-m)x) \Big|_0^{2\pi} = 0.$$

Thus $(e_n)_{-\infty}^{\infty}$ is an orthonormal set.

Now suppose $F \in L^2$. Given $\varepsilon > 0$, there is a function $u \in \mathcal{C}$ (continuous and periodic) such that

$$\|F_u - F\| < \varepsilon.$$

By the Weierstrass approximation theorem (or the classical theorem on approximation by trigonometric polynomials), there is a linear combination $v = \sum a_n e_n$ (a trigonometric polynomial) such that

$$\sup_x |v(x) - u(x)| < \varepsilon.$$

Then

$$\|F_v - F_u\| = \|v - u\| = \left( \frac{1}{2\pi} \int_0^{2\pi} |v(x) - u(x)|^2 \, dx \right)^{1/2} \leq \sup_x |v(x) - u(x)| < \varepsilon.$$

By the triangle inequality,

$$\|F_v - F\| \leq \|F_v - F_u\| + \|F_u - F\| < 2\varepsilon.$$

Thus $F$ is in the closed linear span of $\{e_n\}_{-\infty}^{\infty}$. Therefore $(e_n)_{-\infty}^{\infty}$ is a complete orthonormal set, i.e., an orthonormal basis for $L^2$. $\square$
