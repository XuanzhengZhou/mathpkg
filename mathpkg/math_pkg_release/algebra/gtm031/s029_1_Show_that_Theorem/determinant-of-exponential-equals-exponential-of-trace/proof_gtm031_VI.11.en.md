role: proof
locale: en
of_concept: determinant-of-exponential-equals-exponential-of-trace
source_book: gtm031
source_chapter: "VI"
source_section: "11"
---
Using the formula for the matrix of $\exp A$ in the classical canonical form, a typical diagonal block has the form

$$\begin{bmatrix}
\exp \rho \\
\exp \rho & \exp \rho \\
\frac{\exp \rho}{2!} & \exp \rho & \exp \rho \\
\cdot & \cdot & \cdot & \cdot
\end{bmatrix}.$$

Since each such diagonal block is lower triangular with $\exp \rho$ on the diagonal, its determinant is simply $(\exp \rho)^{e}$ where $e$ is the size of the block. Summing over all blocks and all characteristic roots, we find that

$$\det (\exp A) = \prod_{i=1}^{n} \exp \rho_i = \exp(\rho_1 + \rho_2 + \cdots + \rho_n) = \exp(\Sigma \rho_i),$$

where $\rho_1, \rho_2, \cdots, \rho_n$ are the $n$ characteristic roots of $A$ (counted with multiplicity). Since the trace of $A$ equals the sum of its characteristic roots, $\operatorname{tr} A = \sum_{i=1}^{n} \rho_i$, we conclude that

$$\det (\exp A) = \exp (\operatorname{tr} A).$$
