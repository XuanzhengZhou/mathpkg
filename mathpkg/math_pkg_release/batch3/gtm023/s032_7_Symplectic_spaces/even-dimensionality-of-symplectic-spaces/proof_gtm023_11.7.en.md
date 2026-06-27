---
role: proof
locale: en
of_concept: even-dimensionality-of-symplectic-spaces
source_book: gtm023
source_chapter: "11"
source_section: "7"
---

The proof is left as an exercise to the reader in the source text. The argument proceeds as follows:

($\Rightarrow$) Suppose a symplectic inner product $\langle\, , \,\rangle$ exists on the $m$-dimensional space $E$. The bilinear form is represented by a skew-symmetric matrix $S$ of size $m \times m$ relative to any basis. Since $\langle\, , \,\rangle$ is non-degenerate, $\det S \neq 0$. A skew-symmetric matrix of odd dimension always has zero determinant (since $S^{\mathsf{T}} = -S$ implies $\det S = \det(-S) = (-1)^m \det S$, and for odd $m$ this forces $\det S = 0$). Hence $m$ must be even, $m = 2n$.

($\Leftarrow$) If $m = 2n$, choose a basis $\{a_1, \ldots, a_n, b_1, \ldots, b_n\}$ and define $\langle a_i, a_j \rangle = 0$, $\langle b_i, b_j \rangle = 0$, $\langle a_i, b_j \rangle = \delta_{ij}$. Extending bilinearly yields a non-degenerate skew-symmetric bilinear form on $E$.
