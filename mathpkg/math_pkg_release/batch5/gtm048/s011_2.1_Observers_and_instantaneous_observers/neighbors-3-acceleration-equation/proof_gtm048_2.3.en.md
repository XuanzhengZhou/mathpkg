---
role: proof
locale: en
of_concept: neighbors-3-acceleration-equation
source_book: gtm048
source_chapter: "2"
source_section: "2.3"
---

By Exercise 2.0.4, $L_Q W = 0$. Fix $u \in \mathcal{E}$, and let $\tilde{W}$ be a vector field defined in some neighborhood of $\gamma u$ such that $[\tilde{W}, Q] = 0$ and $\tilde{W} \circ \gamma = W$. Now
$$D_Q^2 \tilde{W} = D_Q D_Q \tilde{W} = D_Q(D_{\tilde{W}} Q + [Q, \tilde{W}]) = D_Q D_{\tilde{W}} Q = R_{Q\tilde{W}} Q + D_{\tilde{W}} D_Q Q + D_{[Q,\tilde{W}]} Q = R_{Q\tilde{W}} Q,$$
where the last equality uses $D_Q Q = 0$ (geodesic frame). Restricting to $\gamma$, we have $D_{\gamma_*}^2 W = R_{\gamma_* W \gamma_*}$. Since $g(R_{ZX}Z, Z) = 0$ for all $X \in R$, the operator $\psi_Z$ is self-adjoint with respect to $gz|_R$. The Fermi-Walker connection decomposition then yields $F_{\gamma_*}^2 W = \psi W$.
