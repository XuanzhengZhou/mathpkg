---
role: proof
locale: en
of_concept: dimension-of-sum-formula
source_book: gtm023
source_chapter: "1"
source_section: "1.21"
---

Let $r = \dim(E_1 \cap E_2)$, $p = \dim E_1$, $q = \dim E_2$. Choose a basis $z_1, \ldots, z_r$ of $E_1 \cap E_2$ and extend it to a basis $z_1, \ldots, z_r, x_{r+1}, \ldots, x_p$ of $E_1$ and to a basis $z_1, \ldots, z_r, y_{r+1}, \ldots, y_q$ of $E_2$.

Consider the vectors
$$z_1, \ldots, z_r, \; x_{r+1}, \ldots, x_p, \; y_{r+1}, \ldots, y_q.$$
Clearly these vectors generate $E_1 + E_2$.

To show linear independence, note that the $x_i$ are linearly independent modulo $E_1 \cap E_2$: if $\sum_i \lambda^i x_i \in E_1 \cap E_2$, then $\sum_i \lambda^i x_i = \sum_k \mu^k z_k$, whence all coefficients vanish. Now assume a relation
$$\sum_k \zeta^k z_k + \sum_i \xi^i x_i + \sum_j \eta^j y_j = 0.$$
Then $\sum_i \xi^i x_i = -\sum_j \eta^j y_j - \sum_k \zeta^k z_k \in E_2$, so $\sum_i \xi^i x_i \in E_1 \cap E_2$, forcing $\xi^i = 0$ by the independence modulo $E_1 \cap E_2$. Similarly $\eta^j = 0$, then $\zeta^k = 0$. Hence the vectors are linearly independent and form a basis.

Counting gives $\dim(E_1 + E_2) = r + (p-r) + (q-r) = p + q - r = \dim E_1 + \dim E_2 - \dim(E_1 \cap E_2)$.
