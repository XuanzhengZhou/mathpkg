---
role: proof
locale: en
of_concept: skew-symmetric-operators-cross-products-3d
source_book: gtm060
source_chapter: "6"
source_section: "26"
---

The skew-symmetric operators from $\mathbb{R}^3$ to $\mathbb{R}^3$ form a linear space. Its dimension is 3, since a skew-symmetric $3 \times 3$ matrix is determined by its three elements below the diagonal (the diagonal entries are zero and the upper triangle follows by antisymmetry).

The operator of vector multiplication by $\omega$, defined as $q \mapsto [\omega, q]$, is linear and skew-symmetric. The operators of vector multiplication by all possible vectors $\omega$ in three-space form a linear subspace of the space of all skew-symmetric operators. The dimension of this subspace is equal to 3, since the map $\omega \mapsto [\omega, \cdot]$ is injective.

Therefore, the subspace of vector multiplications coincides with the space of all skew-symmetric operators. In Cartesian coordinates, the operator $A$ is given by the antisymmetric matrix:

$$A = \begin{bmatrix}
0 & -\omega_3 & \omega_2 \\
\omega_3 & 0 & -\omega_1 \\
-\omega_2 & \omega_1 & 0
\end{bmatrix},$$

with the vector $\omega = \omega_1e_1 + \omega_2e_2 + \omega_3e_3$. The vector $\omega$ is uniquely determined since the three independent matrix entries uniquely determine the three components of $\omega$.
