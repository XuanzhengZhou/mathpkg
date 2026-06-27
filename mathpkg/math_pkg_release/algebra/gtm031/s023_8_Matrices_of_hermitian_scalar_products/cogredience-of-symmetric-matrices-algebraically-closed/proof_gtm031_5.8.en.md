---
role: proof
locale: en
of_concept: cogredience-of-symmetric-matrices-algebraically-closed
source_book: gtm031
source_chapter: "5"
source_section: "8"
---

By Theorem 3, for any symmetric scalar product $g(x, y)$ there exists a basis $(u_1, \cdots, u_n)$ such that

$$g(u_i, u_j) = \delta_{ij} \beta_i, \quad \beta_i \neq 0 \text{ for } i = 1, \cdots, r,$$

where $r$ is the rank of the matrix $\operatorname{diag}\{\beta_1, \cdots, \beta_n\}$ of $g$, and $r$ is the common rank of all matrices of this scalar product. We may replace $u_i$ by $v_i = \gamma_i u_i$ with $\gamma_i \neq 0$, after which the matrix becomes $\operatorname{diag}\{\beta_1', \cdots, \beta_n'\}$ where $\beta_i' = \gamma_i^2 \beta_i$. Thus any $\beta_i$ can be replaced by $\beta_i' = \gamma_i^2 \beta_i$.

Now suppose $\Phi$ is algebraically closed. Then every element of $\Phi$ is a square; for each $\beta_i \neq 0$, choose $\gamma_i = \beta_i^{-1/2}$ (i.e., $\gamma_i^2 = \beta_i^{-1}$). Then $\beta_i' = \gamma_i^2 \beta_i = 1$. Hence the matrix of $g$ relative to the new basis is

$$\operatorname{diag}\{1, \cdots, 1, 0, \cdots, 0\}$$

with exactly $r$ ones on the diagonal. This matrix is completely determined by the rank $r$. Therefore any two symmetric matrices in $\Phi_n$ are cogredient if and only if they have the same rank.
