---
role: proof
locale: en
of_concept: tm-is-elementary
source_book: gtm037
source_chapter: "3"
source_section: "1"
---

For any $e, x_0, \ldots, x_{m-1}, u$, we have $(e, x_0, \ldots, x_{m-1}, u) \in T_m$ iff

$$e \in g^*\mathbb{T}, u \in R_2, ((u)_0)_0 = e,$$

$$\left(((u)_0)_1, f_3^m(x_0, \ldots, x_{m-1}), s, 1\right) \in R_3,$$

$$\forall t \leq ((u)_0)_1 \left(t \text{ odd } \land t > s \Rightarrow (((u)_0)_1)_t = 0\right),$$

$$\forall t \leq ((u)_0)_1 \left(t \text{ even } \Rightarrow (((u)_0)_1)_t = 0\right)$$

for some $s \leq ((u)_0)_1$, with $((u)_0)_3 = 0$, and $(((u)_1)_1)_2 = 1$.

All of these conditions involve only elementary relations: membership in $g^*\mathbb{T}$ and $R_2$, $R_3$, sequence number projections, bounded quantifiers, and simple arithmetic comparisons. Hence $T_m$ is elementary.
