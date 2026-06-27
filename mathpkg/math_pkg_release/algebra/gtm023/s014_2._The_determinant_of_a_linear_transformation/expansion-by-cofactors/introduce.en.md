---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

The Laplace expansion formula expresses the determinant of an $n \times n$ matrix in terms of determinants of $(n-1) \times (n-1)$ submatrices. Expanding along the $i$-th row gives $\det A = \sum_j (-1)^{i+j} \alpha_i^j \det S_i^j$, where $S_i^j$ is the submatrix obtained by deleting row $i$ and column $j$. A symmetric formula holds for expansion along columns. This recursive formula reduces the computation of an $n$-order determinant to the evaluation of $n$ determinants of order $n-1$.
