---
role: proof
locale: en
of_concept: matrix-representation-group-isomorphism
source_book: gtm031
source_chapter: "II"
source_section: "3"
---

We already know $A \mapsto (\alpha)$ is a bijection. It remains to verify it is a group homomorphism.

If $A \mapsto (\alpha)$ and $B \mapsto (\beta)$, then for each $i$,
$$e_i(A + B) = e_i A + e_i B = \sum_j \alpha_{ij} f_j + \sum_j \beta_{ij} f_j = \sum_j (\alpha_{ij} + \beta_{ij}) f_j.$$

Thus $A + B \mapsto (\alpha) + (\beta)$ where the $(i,j)$-entry of $(\alpha) + (\beta)$ is $\alpha_{ij} + \beta_{ij}$.

The zero transformation maps to the zero matrix, and $-A$ maps to $-(\alpha)$. Therefore $A \mapsto (\alpha)$ is a group isomorphism.
