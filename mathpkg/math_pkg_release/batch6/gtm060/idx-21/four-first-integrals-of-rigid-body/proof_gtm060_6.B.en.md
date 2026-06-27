---
role: proof
locale: en
of_concept: four-first-integrals-of-rigid-body
source_book: gtm060
source_chapter: "6"
source_section: "B"
---

The Lagrangian function of a rigid body about a fixed point $O$ admits all rotations around $O$ (the configuration manifold is $\mathrm{SO}(3)$). By Noether's theorem, the three-parameter rotational symmetry $G = \mathrm{SO}(3)$ yields three conserved quantities: the three components $M_x, M_y, M_z$ of the angular momentum vector $\mathbf{M}$. Additionally, since the Lagrangian does not depend explicitly on time (no external forces), the total energy $E$ is conserved. Here the Lagrangian is purely kinetic:

$$L = T = \frac{1}{2}\sum_i m_i \dot{\mathbf{q}}_i^2.$$

Thus $E = T$. These four functions $M_x, M_y, M_z, E$ on the six-dimensional phase space $T\mathrm{SO}(3)$ are independent in the generic case (when the body has no particular symmetry). Their common level sets

$$M_x = C_1,\quad M_y = C_2,\quad M_z = C_3,\quad E = C_4 > 0$$

define a two-dimensional invariant submanifold $V_c \subset T\mathrm{SO}(3)$. This submanifold is compact, orientable, and admits a non-vanishing tangent vector field (the phase velocity field). By the classification of compact orientable 2-manifolds, $V_c$ must be a torus (or a disjoint union of tori), confirming that the motion is conditionally periodic.
