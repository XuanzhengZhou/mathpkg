---
role: proof
locale: en
of_concept: first-integrals-2d-euler
source_book: gtm060
source_chapter: "Appendix 2"
source_section: "Section 47"
---

The two-dimensional Euler equations can be written in vorticity form as
$$\frac{\partial r}{\partial t} + \{ \psi, r \} = 0,$$
where $\{\psi, r\} = \frac{\partial \psi}{\partial x} \frac{\partial r}{\partial y} - \frac{\partial \psi}{\partial y} \frac{\partial r}{\partial x}$ is the Poisson bracket and $r = -\Delta \psi$.

This equation expresses that the vorticity $r$ is advected by the flow: $r$ is constant along trajectories. Consequently, for any function $\Phi$, the quantity $\Phi(r)$ is also advected:
$$\frac{\partial \Phi(r)}{\partial t} + \{ \psi, \Phi(r) \} = \Phi'(r) \left( \frac{\partial r}{\partial t} + \{ \psi, r \} \right) = 0.$$

Integrating over the domain $D$ and using that the flow is incompressible (so the Jacobian of the flow map is 1), we obtain
$$\frac{d}{dt} \int_D \Phi(r) \, dS = \int_D \frac{\partial \Phi(r)}{\partial t} \, dS = -\int_D \{ \psi, \Phi(r) \} \, dS = 0,$$
since the integral of a Poisson bracket over a domain with divergence-free Hamiltonian is zero by the divergence theorem (or by the fact that it is a total derivative).

In particular, choosing $\Phi(r) = r^k$ for $k = 1, 2, \ldots$ gives the infinite family of first integrals
$$I_k = \int_D r^k \, dS.$$
