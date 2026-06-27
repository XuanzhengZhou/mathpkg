---
role: proof
locale: en
of_concept: geodesics-of-poincare-half-plane
source_book: gtm051
source_chapter: "5"
source_section: "5.1"
---

**Proof of 5.1.7 (Geodesics of the Poincar\'e Half-Plane).**

It suffices to prove the statement for $r = 1$, since the identity map from $H_1^2$ to $H_r^2$ is a homothetic transformation with constant factor $r$ (i.e., a conformal map with $\lambda(u) \equiv r$). Such a map preserves geodesics (this is left as an exercise).

For $H_1^2$, the metric coefficients are $g_{11} = 1/v^2$, $g_{12} = 0$, and $g_{22} = 1/v^2$. Computing the Christoffel symbols, one finds
$$
\Gamma_{11}^1 = \Gamma_{22}^1 = \Gamma_{11}^2 = 0, \qquad \Gamma_{12}^1 = -\Gamma_{22}^2 = -\Gamma_{12}^2 = \frac{1}{v}.
$$

The differential equations for geodesics (see (4.3.3)) therefore become
$$
\ddot{u} - \frac{2\dot{u}\dot{v}}{v} = 0, \qquad \ddot{v} + \frac{\dot{u}^2 - \dot{v}^2}{v} = 0.
$$

If $\dot{u} = 0$, then $u = \text{constant}$, and the geodesic is a vertical line orthogonal to the boundary $v = 0$.

If $\dot{u} \neq 0$, the first equation implies $\frac{d}{dt}\ln(\dot{u}/v^2) = 0$, hence $\dot{u} = c v^2 \neq 0$ for some constant $c$. The second equation yields $\dot{u}^2 + \dot{v}^2 = b v^2 > 0$ for some constant $b$. Combining these two equations gives
$$
\left(\frac{dv}{du}\right)^2 = \frac{\dot{v}^2}{\dot{u}^2} = \frac{b v^2 - \dot{u}^2}{\dot{u}^2} = \frac{b v^2 - c^2 v^4}{c^2 v^4} = \frac{b}{c^2 v^2} - 1.
$$

Solving this differential equation yields curves of the form $(u - u_0)^2 + v^2 = R^2$, which are semicircles centered on the real axis and meeting $v = 0$ orthogonally.
