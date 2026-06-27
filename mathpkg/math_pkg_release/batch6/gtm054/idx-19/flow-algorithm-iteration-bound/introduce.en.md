---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

This proposition establishes an upper bound on the number of iterations that the Flow Algorithm requires to reach a maximum flow. Starting from an initial feasible flow $h$, each iteration increases the flow on the distinguished edge $e_0$ by exactly $1$, and since the capacity $k(e_0)$ is an upper bound, the algorithm terminates after at most $k(e_0) - h(e_0)$ iterations. This guarantees finite termination for integral networks.
