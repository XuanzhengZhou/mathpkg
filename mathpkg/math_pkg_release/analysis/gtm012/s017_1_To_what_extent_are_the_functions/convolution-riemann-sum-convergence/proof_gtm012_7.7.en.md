---
role: proof
locale: en
of_concept: convolution-riemann-sum-convergence
source_book: gtm012
source_chapter: "7"
source_section: "7. Convolution of distributions"
---

# Proof of Riemann Sum Approximation of Convolution

**Corollary 7.3.** If $u \in \mathcal{P}$ and $v \in \mathcal{C}$, then the functions $w_n$ given by

$$w_n(x) = \frac{1}{2\pi} \sum_{m=1}^{n} \frac{2\pi}{n} u(x - x_{mn}) v(x_{mn}), \quad x_{mn} = \frac{2\pi m}{n}, \tag{9}$$

converge to $w = u * v$ in the sense of $\mathcal{P}$ as $n \to \infty$.

*Proof.* Since $D^k(T_x u) = T_x(D^k u)$, the function $D^k w_n$ is the corresponding sequence of functions for $(D^k u) * v = D^k(u * v)$. Therefore $D^k w_n \to D^k w$ uniformly as $n \to \infty$, for each $k$. This is precisely convergence in the sense of $\mathcal{P}$. $\square$

The key idea behind this corollary is that the Riemann sum (9) approximates the convolution integral

$$(u * v)(x) = \frac{1}{2\pi} \int_0^{2\pi} u(x - y) v(y) \, dy,$$

and because differentiation commutes with the Riemann sum construction, the convergence is uniform for all derivatives.
