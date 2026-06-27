---
role: proof
locale: en
of_concept: stationary-rotation-principal-axes
source_book: gtm060
source_chapter: "6"
source_section: "29"
---

A stationary rotation satisfies $\dot{M} = 0$ in the Euler equations. From the scalar Euler equations

$$\frac{dM_1}{dt} = \frac{I_2 - I_3}{I_2 I_3} M_2 M_3, \quad \frac{dM_2}{dt} = \frac{I_3 - I_1}{I_3 I_1} M_3 M_1, \quad \frac{dM_3}{dt} = \frac{I_1 - I_2}{I_1 I_2} M_1 M_2,$$

the condition $\dot{M} = 0$ requires that at least two of the components $M_1, M_2, M_3$ vanish. This means $M$ is aligned with one of the principal axes $e_1, e_2,$ or $e_3$, and the body rotates about that axis. The corresponding $\Omega = A^{-1}M$ is then $\Omega = (M_i/I_i) e_i$, so $\Omega$ is constant. If $I_1 > I_2 > I_3$, then $I_i \neq I_j$ for all $i \neq j$, and the right-hand side cannot vanish when two components of $M$ are simultaneously nonzero. Hence no other equilibrium points exist.
