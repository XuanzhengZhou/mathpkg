---
role: proof
locale: en
of_concept: hadamard-matrix-size-condition
source_book: gtm054
source_chapter: "IX"
source_section: "C"
---
We may assume that $H$ is normalized and that $m \geq 4$. In the $3 \times m$ submatrix formed by the first three rows of $H$, exactly four types of columns are possible, namely
$$\begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}, \quad \begin{bmatrix} 1 \\ 1 \\ -1 \end{bmatrix}, \quad \begin{bmatrix} 1 \\ -1 \\ 1 \end{bmatrix}, \quad \text{and} \quad \begin{bmatrix} 1 \\ -1 \\ -1 \end{bmatrix},$$
which we presume to occur $c_1, c_2, c_3$, and $c_4$ times, respectively. Clearly
$$c_1 + c_2 + c_3 + c_4 = m.$$
From the inner products of rows 1 and 2, rows 1 and 3, and rows 2 and 3, respectively, we obtain
$$c_1 + c_2 - c_3 - c_4 = 0,$$
$$c_1 - c_2 + c_3 - c_4 = 0,$$
$$c_1 - c_2 - c_3 + c_4 = 0.$$
Adding all four equations yields $4c_1 = m$, so $m$ is divisible by $4$.
