---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Proposition F9 states that the cycle matroid and cocycle matroid of any multigraph are regular matroids, i.e., representable over every field. This is a fundamental result connecting graph theory to matroid theory. The proof constructs an explicit orientation-based linear transformation: for each vertex $x$, an incidence function $i_x: E \to \mathbb{F}$ is defined (with values $0$, $\pm 1$) so that $i_x(e)i_y(e) = -1$ when $f(e) = \{x, y\}$. The kernel of the resulting map $\varphi: \mathbb{F}^E \to \mathbb{F}^V$ defined by $\varphi(h)(x) = \sum_{e \in E} i_x(e)h(e)$ is then shown to be a Tutte subspace, whose minimal nonempty supports are precisely the elementary cycles of the multigraph. Since this construction works over any field $\mathbb{F}$, the cycle matroid is regular.
