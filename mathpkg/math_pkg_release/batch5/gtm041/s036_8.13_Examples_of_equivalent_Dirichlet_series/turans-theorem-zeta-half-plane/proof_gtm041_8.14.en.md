---
role: proof
locale: en
of_concept: turans-theorem-zeta-half-plane
source_book: gtm041
source_chapter: "8"
source_section: "8.14"
---

The partial sums $\zeta_n(s) = \sum_{k=1}^n k^{-s}$ are ordinary Dirichlet series. Since $\zeta(s) \neq 0$ for $\sigma > 1$, we have $\zeta_n(s) \neq 0$ for all sufficiently large $n$ in the half-plane $\sigma > 1$. By Bohr's equivalence theorem, this implies that the corresponding series with coefficients $\lambda(k)$ (the Liouville function) is also nonzero for $\sigma > 1$, because the equivalence takes the coefficients $1$ to $\lambda(k)$ via the completely multiplicative function $f(k) = \lambda(k)$.

For real $s$, we have
$$
\lim_{s \to +\infty} \sum_{k=1}^n \frac{\lambda(k)}{k^s} = \lambda(1) = 1.
$$
Hence for all real $s > 1$ we must have $\sum_{k=1}^n \lambda(k) k^{-s} > 0$. Letting $s \to 1$ we obtain
$$
\sum_{k=1}^n \frac{\lambda(k)}{k} \geq 0 \quad \text{for } n \geq n_0.
$$
That is, $C(x) = \sum_{n \leq x} \lambda(n)/n \geq 0$ for $x \geq n_0$.

By Theorem 8.19,
$$
\frac{\zeta(2s)}{(s-1)\zeta(s)} = \int_1^\infty \frac{C(x)}{x^s} \, dx, \qquad \sigma > 1.
$$
Note that $(s-1)\zeta(s)$ is nonzero on the real axis for $s > 1/2$, and $\zeta(2s)$ is finite for real $s > 1/2$. By the integral analogue of Landau's theorem (Theorem 11.13 in [4]), the function on the left is analytic in the half-plane $\sigma > 1/2$. This implies $\zeta(s) \neq 0$ for $\sigma > 1/2$.
