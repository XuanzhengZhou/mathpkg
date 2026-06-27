---
role: proof
locale: en
of_concept: row-rank-equals-column-rank
source_book: gtm031
source_chapter: "II"
source_section: "8"
---

The rank of a linear transformation $A$ in a right vector space is the column rank of its matrix. Equivalent matrices have the same column rank as well as the same row rank. Any matrix $(\alpha)$ is equivalent to a matrix in the normal form (18):
$$
\begin{bmatrix}
1 & 0 & \cdots & 0 & 0 & \cdots & 0 \\
0 & 1 & \cdots & 0 & 0 & \cdots & 0 \\
\cdot & \cdot & \cdots & \cdot & \cdot & \cdots & \cdot \\
0 & 0 & \cdots & 1 & 0 & \cdots & 0 \\
0 & 0 & \cdots & 0 & 0 & \cdots & 0 \\
\cdot & \cdot & \cdots & \cdot & \cdot & \cdots & \cdot \\
0 & 0 & \cdots & 0 & 0 & \cdots & 0
\end{bmatrix}.
$$
A matrix in normal form has the same row rank and column rank (both equal the number of $1$'s on the diagonal). Since $(\alpha)$ is equivalent to this normal form, $(\alpha)$ inherits both equal ranks, establishing that row rank equals column rank for any matrix.
