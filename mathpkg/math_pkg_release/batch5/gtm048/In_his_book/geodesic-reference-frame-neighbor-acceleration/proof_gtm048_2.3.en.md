---
role: proof
locale: en
of_concept: geodesic-reference-frame-neighbor-acceleration
source_book: gtm048
source_chapter: "2"
source_section: "2.3"
---

First, note that $g(R_{Z X} Z, Z) = 0$ for all $X \in R_u$, because $R_{Z X}$ is skew-adjoint (Section 1.0.2, Exercise 1.0.6). Also, $\psi_Z$ is self-adjoint with respect to $g_z|_R$: for all $V, W \in R_u$,
$$g(\psi_Z V, W) = g(R_{Z V} Z, W) = \hat{R}(W, Z, Z, V) = \hat{R}(V, Z, Z, W) = g(R_{Z W} Z, V) = g(\psi_Z W, V),$$
where $\hat{R}$ is the $(0, 4)$ tensor field physically equivalent to $R$ (Section 1.0.2).

Now, since $W$ is a neighbor, $L_Q W' = 0$ for some $W'$ with $pW' = W$ (Exercise 2.0.4). Fix $u \in \mathcal{E}$, and let $\tilde{W}$ be a vector field defined in a neighborhood of $\gamma u$ such that $[\tilde{W}, Q] = 0$ and $\tilde{W} \circ \gamma = W$ (Section 2.0.3). Then:
$$D_Q^2 \tilde{W} = D_Q D_Q \tilde{W} = D_Q (D_{\tilde{W}} Q + [Q, \tilde{W}]) = D_Q D_{\tilde{W}} Q$$
$$= R_{Q \tilde{W}} Q + D_{\tilde{W}} D_Q Q + D_{[Q, \tilde{W}]} Q = R_{Q \tilde{W}} Q,$$
since $D_Q Q = 0$ (geodesic reference frame) and $[Q, \tilde{W}] = 0$. Restricting to $\gamma$,
$$D_{\gamma_*}^2 W = R_{\gamma_* W \gamma_*} = -\psi_{\gamma_*} W.$$

The negative sign arises from the curvature convention. By the properties of the Fermi-Walker connection (Proposition 2.2.2), for a spatial vector field $W$, $F_{\gamma_*} W = p(D_{\gamma_*} W)$, and applying this twice yields $F_{\gamma_*}^2 W = \psi W$ as stated.
