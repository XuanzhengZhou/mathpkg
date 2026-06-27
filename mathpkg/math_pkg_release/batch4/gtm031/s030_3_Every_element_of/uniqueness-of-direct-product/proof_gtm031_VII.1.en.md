---
role: proof
locale: en
of_concept: uniqueness-of-direct-product
source_book: gtm031
source_chapter: "VII"
source_section: "1. Product groups of vector spaces"
---

Let $\mathfrak{P}$ and $\mathfrak{P}_1$ be direct products of $\mathfrak{R}'$ and $\mathfrak{S}$ relative to products $\times$ and $\times_1$ respectively. Consider the natural correspondence

$$\sum_i x_i' \times y_i \longmapsto \sum_i x_i' \times_1 y_i.$$

We must first show that this mapping is single-valued, i.e., that if $\sum_i x_i' \times y_i = \sum_j u_j' \times v_j$ in $\mathfrak{P}$, then the corresponding sums in $\mathfrak{P}_1$ are equal. Equivalently, we must show that $\sum_i x_i' \times y_i = 0$ in $\mathfrak{P}$ implies $\sum_i x_i' \times_1 y_i = 0$ in $\mathfrak{P}_1$.

Express the $y_i$ in terms of a basis $f_1, f_2, \ldots, f_r$ of the subspace they span. Write $y_k = \sum_l \alpha_{kl} f_l$. Then

$$
0 = \sum_k x_k' \times y_k = \sum_k x_k' \times \sum_l \alpha_{kl} f_l
= \sum_l \left( \sum_k x_k' \alpha_{kl} \right) \times f_l.
$$

Since the $f_l$ are linearly independent, condition 4(a) of the direct product definition implies that $\sum_k x_k' \alpha_{kl} = 0$ for each $l = 1, 2, \ldots, r$. Consequently, in $\mathfrak{P}_1$ we have

$$
\sum_l \left( \sum_k x_k' \alpha_{kl} \right) \times_1 f_l = 0.
$$

Retracing the steps using the bilinearity of $\times_1$,

$$
0 = \sum_l \sum_k (x_k' \alpha_{kl}) \times_1 f_l
= \sum_k x_k' \times_1 \sum_l \alpha_{kl} f_l
= \sum_k x_k' \times_1 y_k.
$$

Thus the two formally distinct images of any element of $\mathfrak{P}$ are equal, and the correspondence is single-valued. By construction it is a homomorphism and is surjective (every element of $\mathfrak{P}_1$ is a sum of the form $\sum_i x_i' \times_1 y_i$ by condition 3 of the product group definition).

If $\mathfrak{P}_1$ is also a direct product, then the symmetric argument shows that $\sum_i x_i' \times_1 y_i = 0$ in $\mathfrak{P}_1$ implies $\sum_i x_i' \times y_i = 0$ in $\mathfrak{P}$. Hence the kernel of the homomorphism is $0$, and the mapping is injective. Therefore the natural mapping is an isomorphism of $\mathfrak{P}$ onto $\mathfrak{P}_1$.
