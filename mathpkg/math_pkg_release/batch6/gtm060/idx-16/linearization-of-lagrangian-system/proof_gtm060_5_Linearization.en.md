---
role: proof
locale: en
of_concept: linearization-of-lagrangian-system
source_book: gtm060
source_chapter: "5"
source_section: "Linearization"
---

Reduce the Lagrangian system to the form $\dot{x} = f(x)$ by using the canonical variables $p$ and $q$:

$$\dot{p} = -\frac{\partial H}{\partial q}, \quad \dot{q} = \frac{\partial H}{\partial p}, \quad H(p, q) = T + U.$$

Since $p = q = 0$ is an equilibrium position, the expansions of the right-hand sides in Taylor series at zero begin with terms that are linear in $p$ and $q$. Because the right-hand sides are partial derivatives, these linear terms are determined by the quadratic terms $H_2$ of the expansion for $H(p, q)$. But $H_2$ is precisely the Hamiltonian function of the system with Lagrangian $L_2 = T_2 - U_2$, since $H_2 = T_2(p) + U_2(q)$. Therefore, the linearized equations of motion are exactly the equations of motion for the system described in the theorem, with Lagrangian $L_2 = T_2 - U_2$. $\square$
