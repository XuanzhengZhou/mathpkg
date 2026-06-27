---
role: proof
locale: en
of_concept: orthonormal-projection-frame-independence
source_book: gtm020
source_chapter: "3"
source_section: "3.1"
---

**Proof.** Let $(v'_1, \ldots, v'_k) = (v_1, \ldots, v_k)a$ where $a = (a_{i,j}) \in U_F(k)$, so that $v'_j = \sum_i a_{i,j} v_i$. We compute:

$$\sum_{1 \leq j \leq k} (x|v'_j)v'_j = \sum_{i,j,m} (x|a_{i,j}v_i)a_{m,j}v_m = \sum_{i,m} \left( \sum_{1 \leq j \leq k} \bar{a}_{i,j}a_{m,j} \right) (x|v_i)v_m$$

Since $a$ is unitary (i.e., $a \in U_F(k)$), we have $\sum_j \bar{a}_{i,j}a_{m,j} = \delta_{i,m}$ (the Kronecker delta). Therefore

$$\sum_{1 \leq j \leq k} (x|v'_j)v'_j = \sum_{i,m} \delta_{i,m}(x|v_i)v_m = \sum_{1 \leq i \leq k} (x|v_i)v_i$$

This proves the proposition.
