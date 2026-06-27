---
role: proof
locale: en
of_concept: stability-criterion-2d-stationary-flow
source_book: gtm060
source_chapter: "Appendix 2"
source_section: "Section 47"
---

By the previous theorem, a stationary flow is a conditional extremum of the kinetic energy $H$ on the coadjoint orbit of isovorticial fields. The second variation $d^2 H$ on the tangent space to this orbit determines stability.

For the group $\operatorname{SDiff}(D)$ in two dimensions, the tangent space to the coadjoint orbit at a stationary flow with stream function $\psi$ consists of divergence-free vector fields $\delta v$ that are obtained as $\delta v = I \operatorname{grad} \varphi$ where $\varphi$ is a function with the same boundary conditions as $\psi$ and with zero circulation around each boundary component. The variation of vorticity is $\delta r = \operatorname{curl} \delta v = -\Delta \varphi$.

Computing the second variation (following Arnold's general formula for Lie groups, Theorem 9) gives
$$2 d^2 H = \iint_D (\delta v)^2 + \frac{\Delta \psi}{\nabla \Delta \psi} (\delta r)^2 \, dx \, dy$$
$$= \iint_D (\nabla \varphi)^2 + \frac{\nabla \psi}{\nabla \Delta \psi} (\Delta \varphi)^2 \, dx \, dy.$$

The ratio $\nabla \psi / \nabla \Delta \psi$ is well-defined because for a stationary flow, the gradients of $\psi$ and $\Delta \psi$ are collinear (both are orthogonal to the velocity $v$, which is tangent to the level sets of $\psi$).

If the quadratic form is positive-definite (respectively negative-definite), then the stationary flow is a strict local minimum (respectively maximum) of $H$ on the coadjoint orbit. By Dirichlet's principle for Hamiltonian systems (or Arnold's stability theorem), this implies Lyapunov stability.

The perturbation bound follows from the boundedness condition $c \leq -\nabla \psi / \nabla \Delta \psi \leq C$ with $0 < c < C < \infty$, which gives
$$c \iint_D (\Delta \varphi)^2 \, dx \, dy \leq -\iint_D \frac{\nabla \psi}{\nabla \Delta \psi} (\Delta \varphi)^2 \, dx \, dy \leq C \iint_D (\Delta \varphi)^2 \, dx \, dy.$$

Since $d^2 H$ is conserved (as a consequence of the Hamiltonian structure at a critical point), we obtain the a priori estimate bounding the perturbation at any time by its initial value.
