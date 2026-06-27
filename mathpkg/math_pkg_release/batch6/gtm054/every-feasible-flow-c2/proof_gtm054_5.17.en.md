---
role: proof
locale: en
of_concept: every-feasible-flow-c2
source_book: gtm054
source_chapter: "5"
source_section: "IVD"
---

Let $h \in F$ be feasible, let $C$ be a cut, and let $g$ be the function $g_U$ determined by $C$ and $e_0$ as above. Since Since $g \in F^\perp$, we have

$$0 = h \cdot g = \sum_{e \in W} h(e)g(e) = \sum_{g(e) = 1} h(e) - \sum_{g(e) = -

Define $h(i, j)$ to be 1 either if $j = i + 1$ and $i = 2, 3, \ldots, 7$ or if $(i, j) = (8, 2)$, and to be 0 otherwise. This may be visualized as a flow of one unit “around the outer rim” of the figure. It is clearly a feasible flow. If $e_0 = (8, 2)$, the cut $C$ determined by $U = \{1, 2, 3, 4\}$ is a cut through $e_0$. The edges which appear in the figure and belong to $C$ are $(8, 2), (1, 9), (1, 7), (5, 1)$, and $(4, 5)$. Furthermore, $k(C; e_0) = 13$.
