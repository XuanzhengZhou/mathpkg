---
role: proof
locale: en
of_concept: so3-homeomorphic-to-rp3
source_book: gtm020
source_chapter: "4"
source_section: "12"
---

An element $u \in SO(3)$ is a rotation of $\mathbf{R}^3$. By the spectral theorem for orthogonal matrices, $u$ leaves a 1-dimensional subspace invariant. Thus there exists a unit vector $x_u \in S^2$ such that $u(x_u) = x_u$. The restriction of $u$ to the plane orthogonal to $x_u$ is a rotation in $SO(2)$, which is determined by an angle $\theta_u$ (mod $2\pi$).

We associate to $u$ the point $\theta_u x_u$ in the closed ball $B(0, \pi) \subset \mathbf{R}^3$. Observe the following:
- For the identity ($\theta = 0$), the associated point is the origin.
- For $0 < \theta < \pi$, the map is bijective onto the interior of the ball.
- For $\theta = \pi$, rotation by $\pi$ about $x_u$ equals rotation by $\pi$ about $-x_u$, so antipodal points on the boundary $\partial B(0, \pi)$ must be identified.

The resulting quotient space of $B(0, \pi)$ with antipodal identifications on the boundary is precisely $\mathbf{R}P^3$. This identification is a continuous bijection from the compact space $SO(3)$ onto the Hausdorff space $\mathbf{R}P^3$, hence a homeomorphism.
