---
role: proof
locale: en
of_concept: taylor-expansion-space-curve
source_book: gtm051
source_chapter: "1"
source_section: "1.5"
---
The result follows from substituting the Frenet equations

$$\dot{e}_1(t) = |\dot{c}(t)| \kappa(t) e_2(t),$$
$$\dot{e}_2(t) = |\dot{c}(t)| (-\kappa(t) e_1(t) + \tau(t) e_3(t)),$$
$$\dot{e}_3(t) = -|\dot{c}(t)| \tau(t) e_2(t)$$

into the Taylor expansion of $c(t)$. Assuming arc-length parametrization, $|\dot{c}(t)| = 1$, we have

$$c(t) = c(0) + t \dot{c}(0) + \frac{t^2}{2} \ddot{c}(0) + \frac{t^3}{6} \dddot{c}(0) + o(t^3).$$

Since $\dot{c}(0) = e_1$, $\ddot{c}(0) = \kappa e_2$, and $\dddot{c}(0) = -\kappa^2 e_1 + \dot{\kappa} e_2 + \kappa \tau e_3$, the expansion of $c(t)$ in the Frenet frame is determined entirely by $\kappa$, $\tau$, and $\dot{\kappa}$.
