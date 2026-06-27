---
role: proof
locale: en
of_concept: characteristic-flow-preserves-integral-manifolds
source_book: gtm060
source_chapter: "Appendix M"
source_section: "Integration of first-order partial differential equations"
---

From the preceding derivation, on the hypersurface $E^{2n}$ we have $L_\xi \alpha = c\alpha$. Set $\eta(t) = g^t_* \eta$ and $y(t) = \alpha(\eta(t))$. Then

$$\frac{dy}{dt} = \frac{d}{dt} \alpha(g^t_* \eta) = (L_\xi \alpha)(\eta(t)) = c(t)\,\alpha(\eta(t)) = c(t)\,y(t).$$

If $\eta(0)$ is tangent to an integral manifold $I$, then $y(0) = \alpha(\eta(0)) = 0$. The solution to the linear ODE $\frac{dy}{dt} = c(t)y(t)$ with initial condition $y(0) = 0$ is identically zero. Hence for all $t$, $\alpha(\eta(t)) = 0$, meaning each $\eta(t)$ lies in the contact plane. Therefore $g^t I$ is an integral manifold of the contact field for all small $t$.

Since the characteristic vector $\xi$ does not belong to the contact plane (as $d\Phi(\xi) = 0$ on the tangent plane to $E$, but $\xi$ lies in the intersection of the contact plane and the tangent plane — actually $\xi$ is in the contact plane by definition), the union $\bigcup_t g^t I$ for small $t$ has dimension $\dim I + 1 = (n-1) + 1 = n$, which is half the dimension of the contact plane $(2n)$, hence it is a Legendre manifold.
