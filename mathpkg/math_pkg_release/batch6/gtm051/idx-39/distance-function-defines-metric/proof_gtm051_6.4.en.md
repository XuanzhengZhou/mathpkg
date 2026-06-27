---
role: proof
locale: en
of_concept: distance-function-defines-metric
source_book: gtm051
source_chapter: "6"
source_section: "6.4"
---

**Proof.**

1. By definition, $d(p,q) \geq 0$ for all $p,q \in M$, and $d(p,p) = 0$. Symmetry $d(p,q) = d(q,p)$ is immediate since the length of a curve does not depend on orientation. The triangle inequality $d(p,q) \leq d(p,r) + d(r,q)$ follows from the definition of $d$ as an infimum of curve lengths: given any curve from $p$ to $r$ and any curve from $r$ to $q$, their concatenation is a piecewise smooth curve from $p$ to $q$ whose length is the sum of the two lengths.

2. Suppose $d(p,q) = 0$. Consider a geodesic disk $B_\rho(p)$ centered at $p$. By (5.3.4), $d(p,q) > 0$ for all $q \notin B_\rho(p)$, and for any $q \in B_\rho(p)$, $d(p,q) \geq 0$ with equality if and only if $p = q$. Although only smooth curves are considered in the proof of (5.3.4), piecewise smooth curves may also be admitted. One uses the fact that geodesic (polar) coordinates $(u^1, u^2)$ have the characteristic property that any curve connecting $(u^1_0, u^2_0)$ to $(u^1_1, u^2_1)$ must have length at least $|u^1_1 - u^1_0|$. This is because the distance between orthogonal trajectories to the "$u^1 = \text{constant}$" curves is given by the difference in the parameter values of these trajectories. Hence $d(p,q) = 0$ implies $p = q$, completing the proof that $d$ is a metric.

3. A basis for the open sets in the metric topology consists of embedded geodesic disks $B_\rho(p)$, $\rho > 0$, $p \in M$. These are open sets in the usual manifold topology. Conversely, given any neighborhood $U(p)$ of $p$ in the manifold topology, there exists $\rho > 0$ with $B_\rho(p) \subset U(p)$ (for sufficiently small $\rho$, $B_\rho(p)$ is a geodesic $\rho$-disk — the image of $B_\rho(0) \subset T_pM$ under $\exp_p$). Thus the two topologies coincide.
