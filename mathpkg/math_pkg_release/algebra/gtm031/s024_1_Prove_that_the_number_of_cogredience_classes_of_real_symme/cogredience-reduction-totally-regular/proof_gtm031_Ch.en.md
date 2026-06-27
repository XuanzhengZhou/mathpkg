---
role: proof
locale: en
of_concept: cogredience-reduction-totally-regular
source_book: gtm031
source_chapter: ""
source_section: "Witt's Theorem"
---

Let $\mathfrak{S}$ be a maximal totally isotropic subspace of $\mathfrak{R}$. Write $\mathfrak{S} = [y_1, \dots, y_\nu]$ where the $y_i$ are linearly independent. Determine a totally isotropic space $\mathfrak{V} = [v_1, \dots, v_\nu]$ such that $\mathfrak{X} = \mathfrak{S} + \mathfrak{V} = \mathfrak{S} \oplus \mathfrak{V}$ and such that the matrix of $g$ relative to the basis $(y_1, \dots, y_\nu, v_1, \dots, v_\nu)$ of $\mathfrak{X}$ is $\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$. 

Since $\mathfrak{S}$ is maximal totally isotropic and $\mathfrak{R} = \mathfrak{S} \oplus \mathfrak{V} \oplus \mathfrak{X}^\perp$, the scalar product $g$ is totally regular in $\mathfrak{X}^\perp$. Choosing a basis for $\mathfrak{R}$ appropriately gives the matrix form $\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} \oplus B$ where $B$ is the matrix of $g$ restricted to $\mathfrak{X}^\perp$.

For the converse: if a matrix has this form with $B$ totally regular and $(y_1, \dots, y_\nu, v_1, \dots, v_\nu, z_1, \dots, z_{n-2\nu})$ is a corresponding basis, then $\mathfrak{S} = [y_1, \dots, y_\nu]$ is maximal totally isotropic. Any two maximal totally isotropic subspaces have the same dimension, so the decomposition is essentially unique up to equivalence of the $B$ parts.
