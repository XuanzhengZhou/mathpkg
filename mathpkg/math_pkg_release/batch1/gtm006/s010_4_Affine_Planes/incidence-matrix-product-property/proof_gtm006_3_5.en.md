---
role: proof
locale: en
of_concept: incidence-matrix-product-property
source_book: gtm006
source_chapter: "3"
source_section: "5"
---

**Proof.** Let $A$ be the incidence matrix and let $B = AA'$. Then $b_{ij}$ is the scalar product of the $i$-th row of $A$ with the $j$-th row of $A$.

If $i = j$, then $b_{ii}$ counts the number of lines through $P_i$, which is $n+1$ (since each point lies on exactly $n+1$ lines in a projective plane of order $n$).

If $i \neq j$, then $b_{ij}$ equals the number of values of $k$ such that $a_{ik} = a_{jk} = 1$, i.e., the number of lines containing both $P_i$ and $P_j$. Since any two distinct points determine a unique line in a projective plane, $b_{ij} = 1$ for all $i \neq j$.

Thus $AA'$ has diagonal entries $n+1$ and all off-diagonal entries equal to $1$, which is precisely $nI + J$.

For the determinant, we compute:
$$\det(AA') = \det(nI + J) = \begin{vmatrix}
n+1 & 1 & \dots & 1 \\
1 & n+1 & \dots & 1 \\
\vdots & \vdots & \ddots & \vdots \\
1 & 1 & \dots & n+1
\end{vmatrix}$$

Subtract the first row from each of the others, then add each column to the first column. This yields an upper triangular determinant with diagonal entries $(n+1)^2, n, n, \dots, n$ (where $n$ appears $n^2+n$ times). Hence
$$\det(AA') = (n+1)^2 n^{n^2+n}. \quad \square$$
