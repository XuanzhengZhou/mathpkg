---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

The Max-Flow Min-Cut Theorem in its doubly-capacitated form (G3) states that whenever a feasible flow exists, there is a maximum flow through any specified edge $e_0$, and its value equals the minimum of the upper capacities of all cuts through $e_0$ (together with the trivial bound $k_2(e_0)$). The proof adapts the standard Ford-Fulkerson argument from the singly-capacitated case (C6), with the key modification being the altered definition of an unsaturated path: a reverse edge $e_i = (x_i, x_{i-1})$ is considered unsaturated only when $h(e) > k_1(e)$ rather than $h(e) > 0$.
