---
role: proof
locale: en
of_concept: homeomorphism-join-to-product-boundary
source_book: gtm020
source_chapter: "15"
source_section: "3. Hopf Invariant and Bidegree"
---

Proof. Both maps are verified by direct inspection. For $u$, the join parameter $t \in [0,1]$ is split into two regimes: when $t \leq 1/2$, the first coordinate in $B^n$ scales with $t$ while the second coordinate in $S^{m-1}$ is simply $y$; when $t \geq 1/2$, the first coordinate in $S^{n-1}$ is $x$ and the second coordinate in $B^m$ scales with $1-t$. The gluing conditions at $t=0$ and $t=1$ match the join identifications, and the map is continuous and bijective onto the boundary $\partial(B^n \times B^m)$, which is compact, giving a homeomorphism.

For $v$, the trigonometric parametrization $(\sin(\pi t/2)x, \cos(\pi t/2)y)$ maps the join interval continuously onto the unit sphere in $\mathbb{R}^{n+m}$. At $t=0$, the point is $(0, y)$, and at $t=1$, it is $(x, 0)$, matching the join identifications. The map is a continuous bijection from a compact space to a Hausdorff space, hence a homeomorphism onto $S^{n+m-1}$.
