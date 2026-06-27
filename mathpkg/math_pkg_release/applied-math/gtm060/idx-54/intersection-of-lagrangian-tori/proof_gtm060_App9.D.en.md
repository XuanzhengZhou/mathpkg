---
role: proof
locale: en
of_concept: intersection-of-lagrangian-tori
source_book: gtm060
source_chapter: "Appendix 9"
source_section: "D"
---

Consider the function on the torus defined by the integral of the form $(x - c)dy$ along a path. Since the diffeomorphism is homologous to the identity, for any closed contour $\gamma$ we have

$$\oint_{A\gamma} (x - c)dy = \oint_{A\gamma} x dy - \oint_{A\gamma} c dy = \oint_\gamma x dy - \oint_{A\gamma} c dy = c \oint_\gamma dy - c \oint_{A\gamma} dy = 0.$$

Thus the function $F$ defined by $dF = (x - c)dy$ is single-valued on the image torus. Points of intersection of the torus with its image are critical points of $F$, since at them $dF = (x - c)dy = 0$ (so $x = c$).

Conversely, from the condition of single-valued projection of the image torus (i.e., the image torus has equation $x = f(y)$), it follows that all critical points of $F$ are points of intersection of the tori, because $y$ can be taken as local coordinates and $dF = 0$ for all tangent vectors implies $x = c$.

A smooth function on an $n$-dimensional torus has at least $2^n$ critical points, counting multiplicities, of which at least $n + 1$ are geometrically different (by Morse theory; cf. Milnor, "Morse Theory," Princeton University Press, 1967). Therefore the tori intersect in at least $2^n$ points (counting multiplicities), with at least $n+1$ geometrically different intersection points.

The same argument generalizes: any Lagrangian torus intersects its image in at least $2^n$ points, provided both the original torus and its image project single-valued onto the $y$-space. This reduces to the previous case by the canonical transformation $(x, y) \mapsto (x - f(y), y)$.
