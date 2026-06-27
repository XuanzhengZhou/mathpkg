---
role: proof
locale: en
of_concept: schwarzschild-geodesic-first-integrals
source_book: gtm048
source_chapter: "7"
source_section: "7.3"
---

**(a) Conservation of energy.** Since $\partial/\partial t$ is a Killing vector field on $U$, and $\gamma$ is a geodesic, the quantity $g(\gamma_*, \partial/\partial t \circ \gamma)$ is constant along $\gamma$ (by Section 3.6.3e). Let $E = -g(\gamma_*, \partial)$; then equation (a) holds for some $E \in \mathbb{R}$.

**(b) and (c) Conservation of angular momentum.** Consider the vector field $V: U \to TU$ determined by $P_* V = K_x$ (the generator of rotations about the $x$-axis on $\mathcal{S}^2$) and $Q_* V = 0$. Since the Schwarzschild metric is spherically symmetric, $V$ is a Killing vector field. Then by the same geodesic conservation law (Section 3.6.3e), the quantity $g(V, \gamma_*)$ is constant along $\gamma$. Computing:

$$\rho^2 h(\delta_*, K_x) = g(V, \gamma_*) = \text{constant}.$$

Let $J_x$ denote this constant; then (c) follows for some $J_x \in \mathbb{R}$.

Now (b) follows from the spherical symmetry: by Exercise 7.0.1, there exists $J \in [0, \infty)$ such that $\rho^4 h(\delta_*, \delta_*) = J^2$, and $J_x \in [-J, J]$.

The uniqueness of $E$, $J$, and $J_x$ follows because each is defined directly as the value of a geometric quantity evaluated along $\gamma$.
