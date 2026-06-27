---
role: proof
locale: en
of_concept: flow-bounded-by-cut-capacity
source_book: gtm054
source_chapter: "IV"
source_section: "18"
---

Let $h \in F$ be feasible, let $C$ be a cut, and let $g$ be the function $g_U$ determined by $C$ and $e_0$ as defined above. Since $g \in F^\perp$, we have

$$0 = h \cdot g = \sum_{e \in W} h(e)g(e) = \sum_{g(e) = 1} h(e) - \sum_{g(e) = -1} h(e).$$

Therefore

$$\sum_{g(e) = 1} h(e) = \sum_{g(e) = -1} h(e).$$

Now, since $g(e_0) = -1$ and $h$ is feasible (so $0 \leq h(e) \leq k(e)$ for all $e \in W$),

$$h(e_0) \leq \sum_{g(e) = -1} h(e) = \sum_{g(e) = 1} h(e) \leq \sum_{g(e) = 1} k(e) = k(C; e_0).$$

The inequality follows.
