---
role: proof
locale: en
of_concept: first-integrals-for-freely-falling-particles
source_book: gtm048
source_chapter: "7"
source_section: "7.3"
---

Since $\partial/\partial t$ is a Killing vector field on $U$, Section 3.6.3e implies that $g(\gamma_*, \partial/\partial t \circ \gamma)$ is constant along the geodesic $\gamma$. Denote this constant by $-E$, giving (a).

For (c), define a vector field $V: U \to TU$ by the conditions $P_* V = K_x$ and $Q_* V = 0$, where $K_x$ is the generator of rotations about the $x$-axis on $\mathcal{S}^2$ (Section 7.0) and $Q$ is the projection onto the $(t,r)$-plane. One verifies that $V$ is a Killing vector field (it generates the isometry corresponding to rotation about the $x$-axis). Then

$$\rho^2 h(\delta_*, K_x) = g(V \circ \gamma, \gamma_*)$$

is constant along $\gamma$, and we denote this constant by $J_x \in \mathbb{R}$.

For (b), the rotational symmetry of the Schwarzschild metric implies that the total squared angular momentum is conserved. The quantity $\rho^4 h(\delta_*, \delta_*)$ (which is the squared norm of the angular part of the geodesic velocity, weighted by $r^4$) is constant. Denote this constant by $J^2$ with $J \geq 0$. The inequality $J_x \in [-J, J]$ then follows from Exercise 7.0.1, which establishes that $|J_x| \leq J$ for the angular momentum components.

The uniqueness of $E, J, J_x$ follows from the fact that they are defined as the values of specific conserved quantities evaluated at any point along $\gamma$.
