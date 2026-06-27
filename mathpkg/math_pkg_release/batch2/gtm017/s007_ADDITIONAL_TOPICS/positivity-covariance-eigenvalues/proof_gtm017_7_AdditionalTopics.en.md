---
role: proof
locale: en
of_concept: positivity-covariance-eigenvalues
source_book: gtm017
source_chapter: "7"
source_section: "Additional Topics"
---

The covariance function $r(t,\tau)$ is positive definite. Multiplying the eigenvalue equation by $\varphi(t)$ and integrating gives
$$\int_0^T |\varphi(t)|^2 dt = \lambda \iint_0^T \varphi(t) r(t,\tau) \varphi(\tau) dt d\tau.$$
The right-hand side is strictly positive by positive definiteness of $r$, while the left-hand side is positive for a nontrivial $\varphi$. Hence $\lambda > 0$.

If $\varphi(t)$ were complex-valued, write $\varphi = \varphi_1 + i\varphi_2$. By linearity, both $\varphi_1$ and $\varphi_2$ satisfy the equation with eigenvalue $\lambda$. Thus eigenfunctions may be taken real.
