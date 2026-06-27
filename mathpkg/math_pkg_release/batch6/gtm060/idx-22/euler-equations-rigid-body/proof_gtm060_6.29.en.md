---
role: proof
locale: en
of_concept: euler-equations-rigid-body
source_book: gtm060
source_chapter: "6"
source_section: "29"
---

Apply the formula for the velocity of a point $M(t) \in K$ with respect to the stationary space $k$ (Section 26, formula (5)):

$$\dot{m} = B\dot{M} + [\omega, m] = B(\dot{M} + [\Omega, M]).$$

Since the angular momentum $m$ with respect to space is conserved, we have $\dot{m} = 0$. Therefore

$$\dot{M} + [\Omega, M] = 0,$$

which yields the Euler equation

$$\frac{dM}{dt} = [M, \Omega].$$

Since $M = A\Omega$ where $A$ is the inertia operator, and $M_i = I_i \Omega_i$ with respect to the principal axes at $O$, substitution gives the system of three scalar equations

$$\frac{dM_1}{dt} = \frac{I_2 - I_3}{I_2 I_3} M_2 M_3, \quad \frac{dM_2}{dt} = \frac{I_3 - I_1}{I_3 I_1} M_3 M_1, \quad \frac{dM_3}{dt} = \frac{I_1 - I_2}{I_1 I_2} M_1 M_2.$$
