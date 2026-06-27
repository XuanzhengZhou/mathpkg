---
role: proof
locale: en
of_concept: b-operator-2d
source_book: gtm060
source_chapter: "Appendix 2"
source_section: "Section 47"
---

The bilinear operation $B$ is defined by the relation
$$\langle [a, b], c \rangle \equiv \langle B(c, a), b \rangle,$$
where $\langle \cdot, \cdot \rangle$ is the $L^2$ inner product on vector fields. In two dimensions, using the stream function representation $a = I \operatorname{grad} \psi_a$, $c = I \operatorname{grad} \psi_c$, we compute the commutator's stream function as $J(\psi_c, \psi_a)$ by the previous proposition.

The $L^2$ inner product of divergence-free vector fields can be expressed in terms of their stream functions via integration by parts:
$$\langle u, v \rangle = \int_D u \cdot v \, dS = \int_D \nabla \psi_u \cdot \nabla \psi_v \, dS = -\int_D \psi_u \Delta \psi_v \, dS,$$
using the boundary conditions that the fields are tangent to $\partial D$.

The condition $\langle [a, b], c \rangle \equiv \langle B(c, a), b \rangle$ determines $B(c, a)$ up to a gradient term $\operatorname{grad} \alpha$. Computing with the stream function of the commutator yields
$$B(c, a) = -(\Delta \psi_c) \operatorname{grad} \psi_a + \operatorname{grad} \alpha,$$
where $\alpha$ is uniquely determined (up to an additive constant) by the requirement that $\operatorname{div} B = 0$ and $B$ is tangent to the boundary.
