---
role: proof
locale: en
of_concept: edge-partition-4-colorable-condition
source_book: gtm054
source_chapter: "VII"
source_section: "B"
---
**Necessity.** Suppose $\chi_0(\Gamma) \leq 4$ and let
$$h_0 : V \rightarrow \mathbb{K} \times \mathbb{K}$$
be a vertex 4-coloring of $\Gamma$. We represent the four elements of $\mathbb{K} \times \mathbb{K}$ in the natural way: $(0, 0), (0, 1), (1, 0)$, and $(1, 1)$. Based on $h_0$, we define a function $h_1 : \mathcal{E} \rightarrow \{(0, 1), (1, 0), (1, 1)\}$ given by
$$h_1(\{x, y\}) = h_0(x) + h_0(y) \text{ for each } \{x, y\} \in \mathcal{E}.$$
(In general $h_1$ will not be an edge coloring.) We define
$$\mathcal{E}_1 = h_1^{-1}[(0, 1)], \quad \mathcal{E}_2 = h_1^{-1}[(1, 0)], \quad \mathcal{E}_3 = h_1^{-1}[(1, 1)].$$
The parity condition on regions follows from the fact that summing $h_1$ around any closed region boundary yields zero in $\mathbb{K} \times \mathbb{K}$.

**Sufficiency.** If the three subsets exist, one can reconstruct a vertex 4-coloring by assigning colors based on edge membership along paths. $\square$
