---
role: proof
locale: en
of_concept: hall-quasifield-is-weak-quasifield
source_book: gtm006
source_chapter: "IX"
source_section: "2"
---

We must show that for given $p, q \in H$ and given either the left factor $x + \lambda y \neq 0$ or the right factor $z + \lambda t \neq 0$, the equation
\[
(x + \lambda y)(z + \lambda t) = p + \lambda q \tag{4}
\]
has a unique solution for the other factor.

By the left distributive law, it suffices to show that $(x + \lambda y)(z + \lambda t) = 0$ implies $x + \lambda y = 0$ or $z + \lambda t = 0$, and then apply Theorem 7.3 (finite dimension over kernel implies weak quasifield is quasifield).

From the multiplication rule when $y \neq 0$, equation (4) becomes:
\[
xz - y^{-1}tf(x) = p, \qquad yz - xt + at = q. \tag{5}
\]

Multiplying the first equation by $y$ and the second by $x$ and subtracting gives:
\[
bt = py - qx. \tag{6}
\]

Combining (6) with the second equation of (4) yields the linear system:
\[
py - qx = bt, \qquad zy - tx = q - at. \tag{7}
\]

If $t = 0$, then (7) gives $y = qz^{-1}$, $x = pz^{-1}$, with $y = 0$ iff $q = 0$.

If $t \neq 0$, multiply the second equation of (7) by $qt^{-1}$ and subtract from the first:
\[
y(pt - qz) = -t^2 f(qt^{-1}). \tag{8}
\]

Since $t \neq 0$ and $f(s)$ is irreducible over $F$, the right-hand side of (8) is always non-zero. Thus if $pt - qz = 0$ (i.e., either $p = 0$ and $z = 0$, or $z \neq 0$ and $pz^{-1} = qt^{-1}$), then equations (7) are inconsistent and (4) has no solution with $y \neq 0$ (but in this case there exists a solution with $y = 0$ by the $y = 0$ branch of the multiplication). If $pt - qz \neq 0$, then
\[
y = \frac{-t^2 f(qt^{-1})}{pt - qz} \neq 0,
\]
as required.

Finally, from the definition of multiplication, $F$ is in the kernel of $H$, and since $H$ has finite dimension (2) over its kernel, Theorem 7.3 implies $H$ is a quasifield. $\square$
