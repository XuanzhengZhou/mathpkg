---
role: proof
locale: en
of_concept: mobius-transformation-maps-circles-to-circles
source_book: gtm011
source_chapter: "III"
source_section: "3"
---

Given any circle $\Gamma$, pick three distinct points $z_2, z_3, z_4$ on $\Gamma$. Given any circle $\Gamma'$, pick three distinct points $\omega_2, \omega_3, \omega_4$ on $\Gamma'$. By the properties of the cross ratio, there exists a unique Möbius transformation $T$ such that $Tz_j = \omega_j$ for $j = 2, 3, 4$. Since a Möbius transformation maps generalized circles (circles or lines) to generalized circles, and $T$ sends three points of $\Gamma$ to three points of $\Gamma'$, it follows that $T(\Gamma) = \Gamma'$.

The uniqueness statement: if $Tz_j$ are specified for $j = 2, 3, 4$ (distinct $z_j$ in $\Gamma$), then $T$ is unique. This follows because any Möbius transformation is uniquely determined by its action on three distinct points. For if $S$ and $T$ both satisfy $Sz_j = Tz_j$ for $j = 2, 3, 4$, then $S^{-1}T$ fixes three distinct points and must therefore be the identity (a Möbius transformation fixing three distinct points is the identity). Hence $S = T$.
