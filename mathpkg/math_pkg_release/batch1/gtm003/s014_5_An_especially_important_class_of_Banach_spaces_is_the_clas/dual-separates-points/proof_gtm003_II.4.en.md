---
role: proof
locale: en
of_concept: dual-separates-points
source_book: gtm003
source_chapter: "II"
source_section: "4"
---

This result is an immediate consequence of Mazur's theorem (Theorem 3.1). Given $x \neq y$ in $E$, set $z = x - y \neq 0$. Since $E$ is a locally convex space, there exists a convex, circled, open neighborhood $V$ of $0$ not containing $z$ (by the Hausdorff separation property, or if $E$ is not Hausdorff, by the existence of a convex open set not containing $z$). Applying Mazur's theorem with $M = \{0\}$ and $A = z + V$ (or more directly, with $M$ the one-dimensional subspace spanned by $z$ and $A$ a suitable convex open neighborhood of $0$ not intersecting a hyperplane in $M$), there exists a closed hyperplane $H$ containing $0$ and not intersecting a convex open set containing $z$. The continuous linear form $f$ defining $H$ then satisfies $f(z) \neq 0$, hence $f(x) \neq f(y)$.

Equivalently, this is formally contained in Chapter II, Proposition 4.2, Corollary 1.
