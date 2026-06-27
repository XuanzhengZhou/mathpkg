---
role: proof
locale: en
of_concept: polynomial-ring-generator-bound
source_book: gtm028
source_chapter: "II"
source_section: "18"
---

Since $y_j \in R[x_1,\dots,x_n]$, write $y_j = b_j + y^\prime_j$ where $b_j \in R$ and $y^\prime_j$ has zero constant term. Then $S = R[y^\prime_1,\dots,y^\prime_m]$, and the $y^\prime_j$ are algebraically independent if and only if the $y_j$ are. Hence we may assume all $b_j = 0$.

Write each $y_j$ and $x_i$ as:
$$y_j = b_{j1}x_1 + \cdots + b_{jn}x_n + B_j, \quad j=1,\dots,m,$$
$$x_i = a_{i0} + a_{i1}y_1 + \cdots + a_{im}y_m + A_i, \quad i=1,\dots,n,$$
where $b_{jk}, a_{ik} \in R$, and $B_j, A_i$ consist of monomials of degree $\ge 2$.

Substituting the expressions for $y_j$ into the expressions for $x_i$, the linear terms in $x_1,\dots,x_n$ on the right must match the left side $x_i$. This yields a matrix equation: the product of the $n \times m$ matrix $(a_{ik})$ (omitting the constant column $a_{i0}$) and the $m \times n$ matrix $(b_{jk})$ is the $n \times n$ identity matrix. By linear algebra over the ring $R$, this forces $m \geq n$.

If $m = n$, the matrices must be invertible, which forces the linear change of variables to be invertible, and by a degree argument the higher-order terms $B_j$ and $A_i$ must vanish, implying algebraic independence of the $y_j$.
