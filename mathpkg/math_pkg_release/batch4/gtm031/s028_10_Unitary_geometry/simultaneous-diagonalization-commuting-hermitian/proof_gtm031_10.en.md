---
role: proof
locale: en
of_concept: simultaneous-diagonalization-commuting-hermitian
source_book: gtm031
source_chapter: "10"
source_section: "10. Unitary geometry"
---
The proof follows the same line of argument as in the Euclidean case. Using Theorem 13, each individual hermitian (or skew-hermitian) matrix in the commuting set can be diagonalized. Since the matrices commute, the eigenspaces of one are invariant under the others, allowing a common refinement of the diagonalizing bases. The extension to normal matrices follows because a matrix is normal if and only if it can be decomposed as $A = H_1 + iH_2$ with $H_1, H_2$ commuting hermitian matrices. For unitary matrices, the condition that characteristic roots have absolute value 1 follows from: if $yA = \rho y$ with $A$ unitary, then $|\rho|^2(y, y) = (yA, yA) = (yA A', y) = (y, y)$, hence $|\rho|^2 = 1$.
