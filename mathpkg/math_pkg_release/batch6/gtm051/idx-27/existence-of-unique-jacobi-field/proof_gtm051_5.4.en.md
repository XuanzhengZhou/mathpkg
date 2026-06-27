---
role: proof
locale: en
of_concept: existence-of-unique-jacobi-field
source_book: gtm051
source_chapter: "5"
source_section: "5.4"
---

This follows directly from the existence and uniqueness theorem for ordinary differential equations. In the Frenet frame $\{e_1(t), e_2(t)\}$ along the unit-speed geodesic $c(t)$, any Jacobi field $Y(t)$ orthogonal to $c$ can be written as $Y(t) = y(t)e_2(t)$, and the Jacobi equation reduces to the scalar linear second-order ODE:

$$\ddot{y}(t) + K \circ c(t)\,y(t) = 0.$$

Given initial conditions $y(0) = a_0$ and $\dot{y}(0) = a_1$, the standard theory of ODEs guarantees a unique solution $y(t)$ defined for all $t \in [0,a]$. Since the coefficient $K \circ c(t)$ is smooth along the geodesic, the solution is smooth and defines a unique Jacobi field $Y(t) = y(t)e_2(t)$.
