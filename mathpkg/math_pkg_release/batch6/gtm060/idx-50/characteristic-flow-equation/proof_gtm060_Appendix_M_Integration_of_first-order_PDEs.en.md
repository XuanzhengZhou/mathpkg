---
role: proof
locale: en
of_concept: characteristic-flow-equation
source_book: gtm060
source_chapter: "Appendix M"
source_section: "Integration of first-order partial differential equations"
---

Since $\xi$ lies in the intersection of the tangent plane to $E^{2n}$ with the contact plane, we have $d\Phi(\xi) = 0$ on the contact plane. On the tangent plane to $E^{2n}$, $d\Phi = 0$. Therefore, on the tangent plane we have $i_\xi \omega = d\Phi = 0$. More precisely, on the contact plane $\mathbb{R}^{2n}$ we have $i_\xi \omega = d\Phi$ by definition of the characteristic vector, while on the full tangent space to $E^{2n}$ the $1$-form $d\Phi$ vanishes. Hence on the tangent plane to $E$,

$$i_\xi \omega = c\alpha$$

for some function $c$. Applying Cartan's formula:

$$L_\xi \alpha = i_\xi d\alpha + d(i_\xi \alpha) = i_\xi \omega + d(\alpha(\xi)).$$

Since $\xi$ lies in the contact plane, $\alpha(\xi) = 0$, so $d(\alpha(\xi)) = 0$. Thus $L_\xi \alpha = i_\xi \omega = c\alpha$ on the hypersurface $E$.

For the second part, let $\eta(t) = g^t_* \eta$ and $y(t) = \alpha(\eta(t))$. Then

$$\frac{dy}{dt} = \frac{d}{dt} \alpha(g^t_* \eta) = (L_\xi \alpha)(\eta(t)) = c(t)\,\alpha(\eta(t)) = c(t)\,y(t).$$

This is a first-order linear differential equation. If $\eta(0)$ is tangent to an integral manifold $I$ of the contact field, then $y(0) = \alpha(\eta(0)) = 0$. By uniqueness of solutions to the linear ODE $\frac{dy}{dt} = c(t)y(t)$, we obtain $y(t) \equiv 0$, meaning $\alpha(\eta(t)) = 0$ for all $t$, i.e., $\eta(t)$ remains in the contact plane. Therefore $g^t I$ is an integral manifold of the contact field, and the manifold formed by the union $\bigcup_t g^t I$ for small $t$ is a Legendre manifold.
