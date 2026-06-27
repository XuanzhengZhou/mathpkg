---
role: exercise
locale: en
chapter: "2"
section: "5"
exercise_number: 13
---

Prove
(a) $\mathcal{E}(U)$ is connected for any set $U$.
(b) If $|U| \geq 3$, then $\mathcal{E}(U)$ is the only connected $(|U| - 1)$-dimensional subspace of $\mathcal{P}(U)$.

Continuing our notation, let $M_i$ be an incidence matrix for the direct summand $\Lambda_i$ for $i = 1, \ldots, k$. Then the matrix

$$M = \begin{bmatrix}
M_1 & 0 \\
M_2 & \\
0 & M_k
\end{bmatrix}$$

is clearly an incidence matrix of $\bigoplus_{i=1}^{k} \Lambda_i$, provided none of the systems $\Lambda_i$ has an empty vertex set or empty block set. Its transpose $M^*$ has the same form except that $M_i^*$ replaces the submatrix $M_i$ for $i = 1, \ldots, k$. From this argument the following is clear:
