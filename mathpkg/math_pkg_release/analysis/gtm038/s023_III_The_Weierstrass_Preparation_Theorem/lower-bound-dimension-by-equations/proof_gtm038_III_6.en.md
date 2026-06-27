---
role: proof
locale: en
of_concept: lower-bound-dimension-by-equations
source_book: gtm038
source_chapter: "III"
source_section: "6. Analytic Sets"
---

**Proof.** $G$ itself is an irreducible analytic set of complex dimension $n$. By Theorem 6.18, intersecting with $\{f_1 = 0\}$ yields an analytic set whose irreducible components each have dimension $n-1$ (or the intersection is empty, in which case $M = \varnothing$ and the statement is vacuous). Applying Theorem 6.18 successively $n-k$ times, each step reduces the dimension of every irreducible component by at most one. Therefore, after intersecting with all $n-k$ hypersurfaces, each irreducible component of the resulting analytic set $M$ has dimension at least $n - (n-k) = k$.
