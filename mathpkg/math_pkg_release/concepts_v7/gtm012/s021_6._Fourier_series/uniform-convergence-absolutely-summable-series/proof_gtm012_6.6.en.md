---
role: proof
locale: en
of_concept: uniform-convergence-absolutely-summable-series
source_book: gtm012
source_chapter: "6"
source_section: "§6. Fourier series"
---

# Proof of Uniform convergence of trigonometric series with absolutely summable coefficients

**Proof.** Since $|e_n(x)| = |\exp(inx)| = 1$ for all $x \in \mathbb{R}$, we have

$$\sum_{n=-\infty}^{\infty} \sup_{x \in \mathbb{R}} |a_n e_n(x)| = \sum_{n=-\infty}^{\infty} |a_n| < \infty.$$

By the Weierstrass M-test, the series $\sum_{n=-\infty}^{\infty} a_n e_n(x)$ converges uniformly on $\mathbb{R}$. Let $u(x)$ denote its sum:

$$u(x) = \sum_{n=-\infty}^{\infty} a_n \exp(inx).$$

Each partial sum $u_N(x) = \sum_{n=-N}^{N} a_n e_n(x)$ is a continuous function, and the convergence $u_N \to u$ is uniform, so $u \in \mathcal{C}$ (the space of continuous periodic functions).

To verify that $(a_n)_{-\infty}^{\infty}$ are indeed the Fourier coefficients of $u$, observe that uniform convergence implies convergence in $L^2$. For each fixed $m$,

$$(u, e_m) = \lim_{N \to \infty} (u_N, e_m) = \lim_{N \to \infty} \sum_{n=-N}^{N} a_n (e_n, e_m) = a_m,$$

since $(e_n, e_m) = \delta_{nm}$ by orthonormality of the exponentials. Thus $a_n = (u, e_n)$ are the Fourier coefficients of $u$. $\square$
