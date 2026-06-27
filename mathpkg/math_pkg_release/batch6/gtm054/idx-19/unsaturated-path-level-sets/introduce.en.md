---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

The level sets $U_i$ partition the vertices reachable from $x_0$ via unsaturated paths, grouping them by the minimal length of such a path. They form the basis of the search technique implicit in the proof of the Max-Flow Min-Cut Theorem, and are the standard search mechanism associated with the Flow Algorithm. The sets admit an inductive construction: $U_0 = \{x_0\}$, and $U_{i+1}$ consists of all previously unvisited vertices $x$ such that for some $y \in U_i$, either $h(y,x) < k(y,x)$ or $h(x,y) > 0$.
