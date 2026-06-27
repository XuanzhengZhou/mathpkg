---
role: proof
locale: en
of_concept: simultaneous-block-diagonalization-commutative-symmetric-skew
source_book: gtm031
source_chapter: "VI"
source_section: "6"
---

By the theory of orthogonally completely reducible sets, since each $A \in \Omega$ is either symmetric or skew (hence $A' = \pm A$ commutes with every element), we can decompose $\mathfrak{R}$ as a direct sum of mutually orthogonal irreducible subspaces $\mathfrak{S}_i$ relative to $\Omega$.

By Theorem 6, each $\mathfrak{S}_i$ is either one-dimensional or two-dimensional. Moreover, the proof of Theorem 6 shows that the symmetric transformations in $\Omega$ are scalar multiplications in each $\mathfrak{S}_i$, and that the skew transformations are multiples of a particular one.

If we choose Cartesian bases in the $\mathfrak{S}_i$, we obtain a Cartesian basis for $\mathfrak{R}$ relative to which the matrices of all $A \in \Omega$ have the stated block diagonal form. In a one-dimensional $\mathfrak{S}_i$, the matrix of any $A$ is simply a scalar $(\beta_i)$. In a two-dimensional $\mathfrak{S}_i$, the symmetric transformations contribute scalar blocks and the skew transformations contribute blocks of the form $\begin{bmatrix} 0 & \epsilon_i \\ -\epsilon_i & 0 \end{bmatrix}$. Since every $A$ is either symmetric or skew, its matrix in each block is either a scalar or a skew $2 \times 2$ block as stated.

In matrix terms, the passage from the original basis to the Cartesian basis thus obtained is given by an orthogonal matrix $(\sigma)$, yielding the simultaneous block diagonalization.
