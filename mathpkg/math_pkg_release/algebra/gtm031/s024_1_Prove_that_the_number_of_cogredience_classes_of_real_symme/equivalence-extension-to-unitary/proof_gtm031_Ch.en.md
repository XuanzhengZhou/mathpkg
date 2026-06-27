---
role: proof
locale: en
of_concept: equivalence-extension-to-unitary
source_book: gtm031
source_chapter: ""
source_section: "Witt's Theorem"
---

Consider an arbitrary subspace $\mathfrak{S}$ of $\mathfrak{R}$. Let $(y_1, \dots, y_m)$ be a basis for $\mathfrak{S}$ where $[y_1, \dots, y_\nu]$ is the radical of $\mathfrak{S}$. We can find vectors $v_1, \dots, v_\nu$ such that $g(y_j, v_j) = 1$, $g(y_i, v_j) = 0$ otherwise, and $g(v_j, v_k) = 0$. Let $\mathfrak{B} = [v_1, \dots, v_\nu]$. Then $\mathfrak{B} \cap \mathfrak{S} = 0$ and the matrix of $g$ on $\mathfrak{S} + \mathfrak{B}$ is non-singular, so $\mathfrak{S} + \mathfrak{B}$ is not isotropic.

Now let $U$ be an equivalence of $\mathfrak{S}$ onto $\mathfrak{S}U$. The radical of $\mathfrak{S}U$ is $[y_1U, \dots, y_\nu U]$. Find $\bar{v}_1, \dots, \bar{v}_\nu$ with corresponding properties for $\mathfrak{S}U$. The linear transformation sending $v_j$ to $\bar{v}_j$ and coinciding with $U$ on $\mathfrak{S}$ is an equivalence of $\mathfrak{S} + \mathfrak{B}$ onto $\mathfrak{S}U + \bar{\mathfrak{B}}$. Since $\mathfrak{S} + \mathfrak{B}$ is non-isotropic, Witt's theorem extends this to a $g$-unitary transformation of $\mathfrak{R}$.
