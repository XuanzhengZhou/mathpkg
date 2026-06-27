---
role: proof
locale: en
of_concept: first-homotopy-groups-of-classical-groups
source_book: gtm020
source_chapter: "4"
source_section: "12"
---

First, for the symplectic group: $Sp(1) \cong SU(2) \cong S^3$, the 3-sphere, which is simply connected, so $\pi_1(Sp(1)) = 0$. Using Proposition 11.1 with $c = 4$ (quaternionic case), we have $1 \leq 4(n+1)-3$ for all $n \geq 1$, giving $\pi_1(Sp(1)) \cong \pi_1(Sp(n))$, hence $\pi_1(Sp(n)) = 0$ for all $1 \leq n \leq +\infty$.

For the special orthogonal group, the inequality $1 \leq (n+1)-3$ requires $n \geq 3$, so $\pi_1(SO(n))$ is computed from $\pi_1(SO(3))$ using stability.

**Claim: $SO(3)$ is homeomorphic to $\mathbf{R}P^3$.**

*Proof of claim:* An element $u \in SO(3)$ fixes some point $x_u$ on the unit sphere $S^2$ (the axis of rotation) and rotates the orthogonal plane by an angle $\theta_u$. Associate to $u$ the point $\theta_u x_u$ in the ball $B(0, \pi) \subset \mathbf{R}^3$. Since rotation by $\theta$ around $x$ is the same as rotation by $-\theta$ around $-x$, antipodal points of $\partial B(0, \pi)$ are identified. This quotient is precisely $\mathbf{R}P^3$.

Therefore, $\pi_1(SO(3)) = \pi_1(\mathbf{R}P^3)$. The universal cover of $\mathbf{R}P^3$ is $S^3$, so $\pi_1(\mathbf{R}P^3) = \mathbf{Z}_2$. Hence $\pi_1(SO(3)) = \mathbf{Z}_2$.

By the stability isomorphisms (Proposition 11.1 with $c=1$), $\pi_1(SO(3)) \cong \pi_1(SO(n))$ for all $n \geq 3$, giving $\pi_1(SO(n)) = \mathbf{Z}_2$ for $3 \leq n \leq +\infty$. By 12.2, $\pi_1(O(n)) \cong \pi_1(SO(n))$ for $n \geq 3$, so $\pi_1(O(n)) = \mathbf{Z}_2$ as well.
