---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

A second-order linear ODE $f'' + bf' + cf = h$ can be solved by factoring the differential operator as $(D - a_1I)(D - a_2I)$ where $a_1, a_2$ are the roots of the characteristic polynomial $z^2 + bz + c$. The equation splits into two successive first-order problems: first solve $g' - a_1g = h$ with $g(0) = d_1 - a_2d_0$, then solve $f' - a_2f = g$ with $f(0) = d_0$. Theorem 5.2 applied twice yields existence and uniqueness, a technique that foreshadows the general theory of linear systems.
