---
role: proof
locale: en
of_concept: equilibrium-position-condition
source_book: gtm060
source_chapter: "5"
source_section: "Equilibrium Positions"
---

Write down Lagrange's equations

$$\frac{d}{dt} \frac{\partial T}{\partial \dot{q}} = \frac{\partial T}{\partial q} - \frac{\partial U}{\partial q}.$$

For $\dot{q} = 0$, the kinetic energy $T(q, \dot{q})$ is a homogeneous quadratic form in $\dot{q}$, so $\partial T / \partial q = 0$ and $\partial T / \partial \dot{q} = 0$ when $\dot{q} = 0$. Therefore, the left-hand side of Lagrange's equation vanishes, and the right-hand side reduces to $-\partial U / \partial q$. Consequently, the equation of motion is satisfied at $q = q_0$, $\dot{q} = 0$ if and only if $\partial U / \partial q|_{q_0} = 0$. $\square$
