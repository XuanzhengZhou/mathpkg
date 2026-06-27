---
role: proof
locale: en
of_concept: characterization-of-circle
source_book: gtm051
source_chapter: "1"
source_section: "1.4"
---

($\Rightarrow$) Let $\kappa(t) = \kappa > 0$ be constant and $\tau(t) = 0$ (so the curve is planar). Let $(e_1(t), e_2(t))$ be the distinguished Frenet frame in $\mathbb{R}^2$, where $e_1 = \dot{c}$ and $e_2$ is the unit normal obtained by rotating $e_1$ by $\pi/2$.

The Frenet equations in the plane give:
$$\dot{e}_1(t) = \kappa e_2(t), \quad \dot{e}_2(t) = -\kappa e_1(t).$$

Consider the point $m(t) := c(t) + \frac{1}{\kappa} e_2(t)$. Then
$$\dot{m}(t) = \dot{c}(t) + \frac{1}{\kappa} \dot{e}_2(t) = e_1(t) - \frac{\kappa}{\kappa} e_1(t) = 0.$$
Thus $m(t)$ is constant, say $m$. Then $|c(t) - m| = |\frac{-1}{\kappa} e_2(t)| = \frac{1}{\kappa}$ for all $t$. Hence $c$ lies on a circle of radius $1/\kappa$ centered at $m$.

($\Leftarrow$) If $c$ lies on a circle of radius $R > 0$ centered at $m$, parametrize by arc length as $c(s) = m + R(\cos(s/R), \sin(s/R))$. Then $\dot{c}(s) = (-\sin(s/R), \cos(s/R))$, $\ddot{c}(s) = (-\frac{1}{R}\cos(s/R), -\frac{1}{R}\sin(s/R))$, so $\kappa(s) = |\ddot{c}(s)| = 1/R$, a positive constant. By direct computation or the fundamental theorem of plane curves, any arc-length parametrized plane curve with constant curvature $\kappa$ and zero torsion has this circular form.
