---
role: proof
locale: en
of_concept: witt-theorem
source_book: gtm031
source_chapter: ""
source_section: "Quaternionic Hermitian Forms / Witt's Theorem"
---

It suffices to prove the result for $\dim \mathfrak{S}_1 = 1$; for, if it is known in this case, then we can use induction on $\dim \mathfrak{S}_1$ as follows. We choose a vector $u_1$ in $\mathfrak{S}_1$ such that $[u_1]$ is not isotropic (Lemma to Theorem 3). Then $\mathfrak{S}_1 = [u_1] \oplus \mathfrak{U}_1$ where $\mathfrak{U}_1 \subseteq [u_1]^\perp$. Using the equivalence of $\mathfrak{S}_1$ and $\mathfrak{S}_2$, we can write $\mathfrak{S}_2 = [u_2] \oplus \mathfrak{U}_2$ where $\mathfrak{U}_2 \subseteq [u_2]^\perp$, $[u_1]$ and $[u_2]$ are equivalent and $\mathfrak{U}_1$ and $\mathfrak{U}_2$ are equivalent. Then $[u_1]^\perp = \mathfrak{U}_1 \oplus \mathfrak{S}_1^\perp$ and $[u_2]^\perp = \mathfrak{U}_2 \oplus \mathfrak{S}_2^\perp$ are equivalent under a transformation $U$. Hence $[u_2]^\perp = \mathfrak{U}_2 \oplus \mathfrak{S}_2^\perp = \mathfrak{U}_1 U \oplus \mathfrak{S}_1^\perp U$. Now $\mathfrak{U}_2$ and $\mathfrak{U}_1 U$ are equivalent and $\mathfrak{U}_1 U$ and $\mathfrak{S}_1^\perp U$ are orthogonal. Since $\dim \mathfrak{U}_1 U < \dim \mathfrak{S}_1$ and $\mathfrak{U}_1$ is not isotropic, we can assume that $\mathfrak{S}_1^\perp U$ and $\mathfrak{S}_2^\perp$ are equivalent.

For the case $\dim \mathfrak{S}_1 = 1$: Let $M$ be the given equivalence and write $\mathfrak{S}_2 = [u_2]$. Since $\mathfrak{S}_1$ is not isotropic, $\mathfrak{R} = [u_1] \oplus [u_1]^\perp$. Let $[u_1]^\perp = \mathfrak{T}$. We need to show there exists a $g$-unitary extension. For the general case where $\mathfrak{S}$ may be isotropic, one first embeds $\mathfrak{S}$ into a non-isotropic subspace $\mathfrak{S} + \mathfrak{B}$ as described in the construction with basis $(y_1, \dots, y_m, v_1, \dots, v_\nu)$, and then applies the non-isotropic case.

For the isotropic case with $\dim \mathfrak{R} = 2$, $\dim \mathfrak{S}_1 = 1$: Both $[u_1, u_2, t] \cap [u_1]^\perp$ and $[u_1, u_2, t] \cap [u_2]^\perp$ are non-isotropic two-dimensional spaces that contain an isotropic one-dimensional subspace $[w]$. In a space of this type we can select a basis relative to which the matrix is $\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$. To see this, choose $q$ so that $g(w, q) = 1 = g(q, w)$ and set $z = q + \lambda w$. Then $g(z, w) = 1 = g(w, z)$ and $g(z, z) = g(q, q) + \lambda + \bar{\lambda}$. By Axiom S we can choose $\lambda$ so that $g(z, z) = 0$, giving a matrix of the required form. It follows that the two subspaces are equivalent, completing the reduction and the proof.
