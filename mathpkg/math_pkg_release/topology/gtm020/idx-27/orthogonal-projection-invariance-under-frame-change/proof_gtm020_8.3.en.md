---
role: proof
locale: en
of_concept: orthogonal-projection-invariance-under-frame-change
source_book: gtm020
source_chapter: "8"
source_section: "3"
---

We calculate

$$\sum_j \langle x \mid v'_j \rangle v'_j = \sum_{i,j,m} \langle x \mid a_{i,j} v_i \rangle a_{m,j} v_m = \sum_{i,m} \left( \sum_j \overline{a}_{i,j} a_{m,j} \right) \langle x \mid v_i \rangle v_m$$

Since $(a_{ij}) \in U_F(k)$, the columns are orthonormal, so $\sum_j \overline{a}_{i,j} a_{m,j} = \delta_{i,m}$ (the Kronecker delta). Substituting,

$$\sum_{i,m} \delta_{i,m} \langle x \mid v_i \rangle v_m = \sum_{i} \langle x \mid v_i \rangle v_i$$

Thus the expression $\sum_i \langle x \mid v_i \rangle v_i$ is unchanged when the orthonormal frame is replaced by another spanning the same subspace.
