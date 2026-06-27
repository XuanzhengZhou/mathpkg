---
role: proof
locale: en
of_concept: canonical-form-of-bilinear-form
source_book: gtm031
source_chapter: "Bilinear Forms"
source_section: "1. Bilinear forms"
---

Let $(\beta)$ be the $n \times n'$ matrix of $g$ relative to any bases of $\mathfrak{R}$ and $\mathfrak{R}'$. By elementary row and column operations, the matrix $(\beta)$ can be reduced to the form

$$\begin{pmatrix} I_r & 0 \\ 0 & 0 \end{pmatrix}$$

where $I_r$ is the $r \times r$ identity matrix and $r$ is the rank of $(\beta)$. Each elementary row operation corresponds to a change of basis in $\mathfrak{R}$, and each elementary column operation corresponds to a change of basis in $\mathfrak{R}'$. Specifically, if we apply the sequence of row operations encoded by an invertible matrix $(\mu)$ and column operations encoded by an invertible matrix $(\nu)$, then the matrix of $g$ relative to the new bases is $(\mu)(\beta)(\nu) = \begin{pmatrix} I_r & 0 \\ 0 & 0 \end{pmatrix}$. Letting $(u_1, \dots, u_n)$ be the basis of $\mathfrak{R}$ corresponding to $(\mu)$ and $(v_1', \dots, v_{n'}')$ be the basis of $\mathfrak{R}'$ corresponding to $(\nu)$, we obtain

$$g(u_i, v_j') = \delta_{ij} \quad \text{for} \quad i, j = 1, \dots, r,$$

$$g(u_i, v_j') = 0 \quad \text{if} \quad i > r \;\text{or}\; j > r.$$

The integer $r$ is the rank (row or column) of $(\beta)$, which is an invariant of the bilinear form $g$.
