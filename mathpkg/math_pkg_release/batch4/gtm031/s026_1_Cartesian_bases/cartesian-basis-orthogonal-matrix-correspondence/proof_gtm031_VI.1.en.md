---
role: proof
locale: en
of_concept: cartesian-basis-orthogonal-matrix-correspondence
source_book: gtm031
source_chapter: "VI"
source_section: "1"
---

Let $(v_1, \ldots, v_n)$ be a fixed Cartesian basis, so $(v_i, v_j) = \delta_{ij}$.

($\Rightarrow$) Let $(u_1, \ldots, u_n)$ be any Cartesian basis with $u_i = \sum_j \sigma_{ij} v_j$. The matrix of the scalar product $(x, y)$ relative to $(u_1, \ldots, u_n)$ is the identity matrix $1$. Since $(u_1, \ldots, u_n)$ is related to $(v_1, \ldots, v_n)$ by the matrix $(\sigma)$, the matrix of $(x, y)$ relative to $(v_1, \ldots, v_n)$ transforms as $(\sigma) 1 (\sigma)' = (\sigma)(\sigma)'$. But relative to the Cartesian basis $(v_1, \ldots, v_n)$, the matrix of $(x, y)$ is also $1$. Hence $(\sigma)(\sigma)' = 1$, so $(\sigma)$ is orthogonal.

($\Leftarrow$) Conversely, let $(\sigma)$ be any orthogonal matrix and define $u_i = \sum_j \sigma_{ij} v_j$. Then the matrix of $(x, y)$ relative to $(u_1, \ldots, u_n)$ is $(\sigma) 1 (\sigma)' = (\sigma)(\sigma)' = 1$. Hence $(u_i, u_j) = \delta_{ij}$, so the $u$'s form a Cartesian basis.

Thus the correspondence $(\sigma) \leftrightarrow (u_1, \ldots, u_n)$ is a bijection between $n \times n$ orthogonal matrices and Cartesian bases.
