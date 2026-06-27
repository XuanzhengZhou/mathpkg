---
role: proof
locale: en
of_concept: functorial-mapping-of-direct-products
source_book: gtm031
source_chapter: "VII"
source_section: "1. Product groups of vector spaces"
---

We must show that the correspondence

$$\sum_i x_i' \times y_i \longmapsto \sum_i x_i' A' \times_1 y_i B$$

is single-valued, i.e., a relation $\sum_k x_k' \times y_k = 0$ in $\mathfrak{P}$ implies $\sum_k x_k' A' \times_1 y_k B = 0$ in $\mathfrak{Q}_1$.

To prove this, express the $y_k$ in terms of a set of linearly independent elements. Write $y_k = \sum_l \alpha_{kl} f_l$ where the $f_l$ are linearly independent. Then

$$
0 = \sum_k x_k' \times y_k = \sum_k x_k' \times \sum_l \alpha_{kl} f_l
= \sum_l \left( \sum_k x_k' \alpha_{kl} \right) \times f_l.
$$

Since $\mathfrak{P}$ is a direct product and the $f_l$ are linearly independent, condition 4(a) implies $\sum_k x_k' \alpha_{kl} = 0$ for each $l$. By the linearity of $A'$,

$$
\sum_k (x_k' A') \alpha_{kl} = \left( \sum_k x_k' \alpha_{kl} \right) A' = 0.
$$

Now in $\mathfrak{Q}_1$,

$$
\sum_k x_k' A' \times_1 y_k B
= \sum_k x_k' A' \times_1 \left( \sum_l \alpha_{kl} f_l \right) B
= \sum_k x_k' A' \times_1 \sum_l \alpha_{kl} (f_l B)
$$

by the linearity of $B$. Rearranging,

$$
= \sum_l \left( \sum_k (x_k' A') \alpha_{kl} \right) \times_1 f_l B
= \sum_l 0 \times_1 f_l B = 0.
$$

Thus the mapping is single-valued. It is clearly a homomorphism because it is defined by linear extension of the action on pure products, and both $\times$ and $\times_1$ are bilinear. Hence the mapping is a homomorphism of $\mathfrak{P}$ into $\mathfrak{Q}_1$.
