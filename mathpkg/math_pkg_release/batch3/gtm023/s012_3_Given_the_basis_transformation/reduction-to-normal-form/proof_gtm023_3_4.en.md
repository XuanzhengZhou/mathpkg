---
role: proof
locale: en
of_concept: reduction-to-normal-form
source_book: gtm023
source_chapter: "3"
source_section: "4. Elementary transformations"
---

Let $(\gamma_\nu^\mu)$ be the given $n \times m$ matrix.

**Step 1.** If all $\gamma_\nu^\mu = 0$, the matrix is already in normal form with $r = 0$. Otherwise, there exists at least one nonzero entry.

**Step 2.** By operations (I.1) and (I.2) (row and column interchanges), move a nonzero entry to the $(1,1)$ position. Now $\gamma_1^1 \neq 0$.

**Step 3.** Scale the first row by $(\gamma_1^1)^{-1}$ to make the $(1,1)$ entry equal to $1$. (This uses the scaling operation $a_v \to \lambda a_v$ with $\lambda \neq 0$.)

**Step 4.** For each $i = 2, \dots, n$, add $-\gamma_i^1$ times the first row to the $i$-th row (operation II.1 with $\lambda = -\gamma_i^1$, $j = 1$). This clears all entries below the $(1,1)$ position in the first column.

**Step 5.** For each $k = 2, \dots, m$, add $-\gamma_1^k$ times the first column to the $k$-th column (operation II.2 with $\lambda = -\gamma_1^k$, $l = 1$). This clears all entries to the right of the $(1,1)$ position in the first row.

The matrix now has the form

$$
\begin{bmatrix}
1 & 0 & \cdots & 0 \\
0 & * & \cdots & * \\
\vdots & \vdots & \ddots & \vdots \\
0 & * & \cdots & *
\end{bmatrix}.
$$

**Step 6.** Apply the same procedure recursively to the $(n-1) \times (m-1)$ submatrix in the lower right corner. At each recursive step, the size of the identity block grows by $1$.

Continue until the remaining submatrix consists entirely of zeros. The final matrix has the form

$$
\begin{bmatrix}
I_r & 0 \\
0 & 0
\end{bmatrix}
$$

where $r$ is the number of recursive steps performed. By construction, $r$ equals the rank of the original matrix, since elementary transformations preserve the rank.
