---
role: proof
locale: en
of_concept: szego-orthogonal-polynomials-symmetric
source_book: gtm034
source_chapter: "V"
source_section: "22"
---

The existence and uniqueness of the polynomials $p_n(z)$ satisfying conditions (b) and (c) follow from the Gram-Schmidt orthogonalization process applied to the monomials $1, z, z^2, \ldots$ with respect to the inner product
$$(f,g) = \frac{1}{2\pi} \int_{-\pi}^{\pi} f(e^{i\theta}) \overline{g(e^{i\theta})} [1 - \phi(\theta)] \, d\theta.$$

Explicit determinantal formulas are available: $p_0(z) = [1 - P(0,0)]^{-1/2}$ and
$$p_n(z) = (D_n D_{n-1})^{-1/2} \det\begin{pmatrix} (f_0,f_0) & \cdots & (f_n,f_0) \\ \vdots & \ddots & \vdots \\ (f_0,f_{n-1}) & \cdots & (f_n,f_{n-1}) \\ 1 & \cdots & z^n \end{pmatrix},$$
where $D_n = \det[(f_i, f_j)]_{0 \leq i,j \leq n}$ and $(f_n, f_m) = \delta(m,n) - P(n,m)$, so the Gram matrix is exactly $I_N - Q_N$.

The proof of the Green function representation uses $g_N(j,k) = (I_N - Q_N)^{-1}(j,k)$. Since the eigenvalues of $Q_N$ lie between 0 and 1 (for symmetric random walk with non-negative transition probabilities), the Neumann series converges. The representation in terms of reproducing kernels leads to
$$\sum_{k=0}^{N} \sum_{j=0}^{N} g_N(k,j) z^j \bar{w}^k = \sum_{n=0}^{N} p_n(z) \overline{p_n(w)}.$$

For part (e), the sequence $g_N(k,j)$ increases monotonically to $g(k,j)$ as $N \to \infty$ (where $g$ is the half-line Green function). Since the random walk is symmetric, P19.3 gives the explicit form of $g(k,j)$. Setting $k=0$ and extracting coefficients yields $\lim_{N \to \infty} p_{N,N-k} = u(k)$.
