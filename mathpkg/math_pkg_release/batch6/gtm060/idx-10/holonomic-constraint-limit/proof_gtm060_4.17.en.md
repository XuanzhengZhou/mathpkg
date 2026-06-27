---
role: proof
locale: en
of_concept: holonomic-constraint-limit
source_book: gtm060
source_chapter: "4"
source_section: "17"
---

The textbook states this theorem as a motivation for the definition of holonomic constraints and notes explicitly (at the beginning of Section 17B): "We will not prove the theorem above, but neither will we use it. We need it only to justify the following [definition]."

The argument sketched in the text proceeds as follows. Introduce curvilinear coordinates $q_1$ (along $\gamma$) and $q_2$ (distance from $\gamma$) in a neighborhood of the curve. The potential energy is taken as
$$U_N = N q_2^2 + U_0(q_1, q_2),$$
so that the force $-\partial U_N / \partial q_2 = -2N q_2 - \partial U_0/\partial q_2$ grows without bound in the $q_2$-direction as $N \to \infty$, confining the motion to $q_2 = 0$. With initial conditions on $\gamma$ ($q_2(0) = \dot{q}_2(0) = 0$), the evolution $q_1 = \varphi(t, N)$ of the tangential coordinate is studied. As $N \to \infty$, the limit $\psi(t) = \lim_{N \to \infty} \varphi(t, N)$ exists and satisfies the Lagrange equation
$$\frac{d}{dt} \left( \frac{\partial L_*}{\partial \dot{q}_1} \right) = \frac{\partial L_*}{\partial q_1},$$
where the reduced Lagrangian $L_*$ is obtained by setting $q_2 = \dot{q}_2 = 0$ in the kinetic energy and restricting the potential: $L_* = T|_{q_2 = \dot{q}_2 = 0} - U_0|_{q_2 = 0}$.

The generalization to $n$ point masses in $3n$-dimensional configuration space follows the same pattern: the strong confining potential $N \mathbf{q}_2^2$ in the directions normal to the constraint submanifold $\gamma$ forces the motion to lie on $\gamma$ in the limit $N \to \infty$, and the dynamics on $\gamma$ is governed by the restricted Lagrangian $L_* = T|_{\mathbf{q}_2 = \dot{\mathbf{q}}_2 = 0} - U_0|_{\mathbf{q}_2 = 0}$.

A rigorous proof would involve showing that the solutions of the full system converge uniformly to a solution of the constrained Lagrange equations, which can be established via singular perturbation theory or by analyzing the Euler-Lagrange equations directly with the limit $N \to \infty$.
