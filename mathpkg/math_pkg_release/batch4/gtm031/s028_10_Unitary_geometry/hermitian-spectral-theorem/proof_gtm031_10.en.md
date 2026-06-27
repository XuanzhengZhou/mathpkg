---
role: proof
locale: en
of_concept: hermitian-spectral-theorem
source_book: gtm031
source_chapter: "10"
source_section: "10. Unitary geometry"
---
The proof follows the Euclidean case. Let $A$ be a hermitian linear transformation and let $\rho$ be a root of its characteristic polynomial. Since $A$ is hermitian, $\rho$ is real. There exists an eigenvector $y$ with $yA = \rho y$, and we may normalize so that $(y, y) = 1$. One can find a unitary basis that includes $y$. With respect to this basis, the matrix of $A$ has a block diagonal form, and by induction we obtain a unitary basis relative to which the matrix of $A$ is $\operatorname{diag}\{\rho_1, \rho_2, \cdots, \rho_n\}$ with real $\rho_i$. Translating to matrix language, if $(\alpha)$ is the original matrix of $A$ relative to some unitary basis, then the change-of-basis matrix $(\sigma)$ to the diagonalizing basis is unitary and satisfies $(\sigma)(\alpha)(\sigma)^{-1} = \operatorname{diag}\{\rho_1, \rho_2, \cdots, \rho_n\}$.
