---
role: proof
locale: en
of_concept: equivalence-of-symplectic-inner-products
source_book: gtm023
source_chapter: "11"
source_section: "7"
---

The proof is presented as an exercise in the source text. The argument proceeds as follows:

Let $\Phi$ and $\Psi$ be two symplectic inner products on $E$. Choose a symplectic basis $\{a_i, b_i\}_{i=1}^n$ for $(E, \Phi)$ so that the matrix of $\Phi$ in this basis is $J = \begin{pmatrix} 0 & I \\ -I & 0 \end{pmatrix}$. Let $M$ be the matrix of $\Psi$ in the same basis. Since $\Psi$ is also a non-degenerate skew-symmetric bilinear form, $M$ is skew-symmetric and non-degenerate, so $M^{-1}$ exists and is also skew-symmetric.

The linear transformation $\varphi$ whose matrix in the symplectic basis is $S$, where $S$ satisfies $S^{\mathsf{T}} M S = J$, relates the two inner products. Writing $S = \begin{pmatrix} A & B \\ C & D \end{pmatrix}$ in block form and imposing the condition $S^{\mathsf{T}} J S = J$ (since $S$ is symplectic with respect to $\Phi$) together with $S^{\mathsf{T}} M S = J$ yields the relations $B^* = B$, $C^* = C$, and $D = -A^*$ (where $*$ denotes the appropriate transpose operation corresponding to the underlying field).

For the dimension formulas, the space of all linear transformations of $E$ has dimension $(2n)^2 = 4n^2$. A transformation with block matrix $\begin{pmatrix} A & B \\ C & D \end{pmatrix}$ is symplectic selfadjoint (i.e., preserves the symplectic form and is selfadjoint with respect to it) if and only if $B^* = B$, $C^* = C$, and $D = -A^*$. Counting free parameters: $A$ contributes $n^2$, $B$ (symmetric) contributes $\frac{n(n+1)}{2}$, $C$ (symmetric) contributes $\frac{n(n+1)}{2}$, and $D$ is determined by $A$. Total: $n^2 + n(n+1) = n(2n+1) = N_2$. Similarly, for symplectic skew transformations one obtains $N_1 = n(2n-1)$.
