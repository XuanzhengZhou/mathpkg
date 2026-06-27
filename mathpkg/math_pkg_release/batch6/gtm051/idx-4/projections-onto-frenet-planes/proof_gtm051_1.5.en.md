---
role: proof
locale: en
of_concept: projections-onto-frenet-planes
source_book: gtm051
source_chapter: "1"
source_section: "1.5"
---
Using Proposition 1.5.3, the Taylor expansion of $c(t)$ in the Frenet frame at $t_0 = 0$ is

$$c(t) = c(0) + t e_1 + \frac{t^2}{2} \kappa e_2 + \frac{t^3}{6}(-\kappa^2 e_1 + \dot{\kappa} e_2 + \kappa \tau e_3) + o(t^3).$$

Projecting onto the $(e_1, e_2)$-plane (osculating plane) gives coordinates $(t, \frac{t^2}{2}\kappa) + o(t^2)$.
Projecting onto the $(e_2, e_3)$-plane (normal plane) gives $(\frac{t^2}{2}\kappa + \frac{t^3}{6}\dot{\kappa}, \frac{t^3}{6}\kappa\tau) + o(t^3)$.
Projecting onto the $(e_3, e_1)$-plane (rectifying plane) gives $(t - \frac{t^3}{6}\kappa^2, \frac{t^3}{6}\kappa\tau) + o(t^3)$.
