---
role: proof
locale: en
of_concept: weierstrass-polynomial-approximation-theorem
source_book: gtm012
source_chapter: "4"
source_section: "4. The Weierstrass approximation theorems"
---

# Proof of Theorem 4.5: Weierstrass Polynomial Approximation Theorem

We first reduce to the case of the interval $[0, \pi]$. By an affine change of variables, any closed interval $[a, b]$ can be mapped to $[0, \pi]$; polynomial approximation is preserved under this transformation.

Suppose therefore that $u$ is continuous on $[0, \pi]$. We extend $u$ to a $2\pi$-periodic even function on $\mathbb{R}$ by setting

$$u(-x) = u(x), \quad x \in [0, \pi],$$

and taking the unique periodic extension of this function. The resulting function belongs to $\mathbb{C}$, the space of continuous $2\pi$-periodic functions.

By Theorem 4.3 (the Weierstrass trigonometric approximation theorem), there exists a sequence $(u_n)_{1}^{\infty}$ of trigonometric polynomials converging uniformly to $u$ on $[0, 2\pi]$, and hence on $[0, \pi]$. Each $u_n$ has the form

$$u_n(x) = \sum_{k=-N_n}^{N_n} a_{k,n} \exp(ikx).$$

Now the partial sums of the power series expansions of the exponentials $\exp(ikx)$ provide polynomial approximations. Specifically, for each $k$, the Taylor series

$$\exp(ikx) = \sum_{m=0}^{\infty} \frac{(ikx)^m}{m!}$$

converges uniformly on the compact interval $[0, \pi]$. Truncating each series at a sufficiently high degree and combining the finite sums yields a sequence of polynomials $(p_n)_{1}^{\infty}$ that converges uniformly to $u$ on $[0, \pi]$.

Returning to the original interval $[a, b]$ via the inverse affine transformation gives polynomial approximation on any closed interval $[a, b] \subset \mathbb{R}$.
