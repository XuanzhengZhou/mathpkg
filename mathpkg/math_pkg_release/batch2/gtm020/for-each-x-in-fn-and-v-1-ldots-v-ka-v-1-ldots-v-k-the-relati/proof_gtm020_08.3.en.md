---
locale: en
of_concept: for-each-x-in-fn-and-v-1-ldots-v-ka-v-1-ldots-v-k-the-relati
role: proof
source_book: gtm020
source_chapter: 8. Calculations Involving the Classical Groups
source_section: '3'
---

We calculate $\sum_j (x|v'_j)v'_j = \sum_{i,j,m} (x|a_{i,j}v_i)a_{m,j}v_m = \sum_{i,m} \left( \sum_j \bar{a}_{i,j}a_{m,j} \right) (x|v_i)v_m = \sum_{i,m} \delta_{i,m} (x|v_i)v_m = \sum_{i} (x|v_i)v_i$. This proves the proposition.

Let $\pi: V_k(F^n) \times F^n \rightarrow F^n$ be defined by the relation $\pi'((v_1, \ldots, v_k)) = \sum_{1 \leq i \leq k} (x|v_i)v_i$. By (3.1), $(v_i) \mapsto \pi'(v_i)(x)$ is constant on the fibre over a point of $G_k(F^n)$ of the projection $p: V_k(F^n) \rightarrow G_k(F^n)$. Therefore, since $F^n$ is locally compact, $\pi'$ defines a map $\pi: G_k(F^n) \times F^n \rightarrow F^n$ which we write $\pi_W(x)$ for $W \in G_k(F^n)$ and $x \in F^n$. If $W = \langle v_1, \ldots, v_k \rangle$, then $\pi_W(x)$ equals $\pi'(v_i)(x)$, and we have $\langle v_i|x - \pi_W(x) \rangle = 0$ for each $i$ with $1 \leq i \leq k$. Let $v_W(x)$ denote $x - \pi_W(x)$. With these notations we state the
