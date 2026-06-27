---
role: proof
locale: en
of_concept: normal-form-of-linear-mapping-matrix
source_book: gtm023
source_chapter: "3"
source_section: "4. Elementary transformations"
---

Let $a_v\ (v = 1, \dots, n)$ be a basis of $E$ such that the vectors $a_{r+1}, \dots, a_n$ form a basis of the kernel of $\varphi$. Then the vectors

$$b_\rho = \varphi(a_\rho) \quad (\rho = 1, \dots, r)$$

are linearly independent. Indeed, if $\sum_{\rho=1}^{r} \lambda^\rho b_\rho = 0$, then $\varphi(\sum_{\rho=1}^{r} \lambda^\rho a_\rho) = 0$, so $\sum_{\rho=1}^{r} \lambda^\rho a_\rho \in \ker \varphi$. But $\ker \varphi$ is spanned by $a_{r+1}, \dots, a_n$, and since $\{a_1, \dots, a_n\}$ is a basis, this forces $\lambda^\rho = 0$ for all $\rho = 1, \dots, r$.

Hence the system $b_1, \dots, b_r$ can be extended to a basis $(b_1, \dots, b_m)$ of $F$. It follows from the construction of the bases $a_v$ and $b_\mu$ that the matrix of $\varphi$ has the form (3.31), i.e.,

$$
\begin{bmatrix}
I_r & 0 \\
0 & 0
\end{bmatrix}
$$

where $I_r$ is the $r \times r$ identity matrix and $r = \operatorname{rank}(\varphi)$.
