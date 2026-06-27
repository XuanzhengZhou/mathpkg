---
role: proof
locale: en
of_concept: decomposition-of-minkowski-space-under-lorentz-transformation
source_book: gtm023
source_chapter: "Chapter 13: Minkowski Space"
source_section: "II. The minimum polynomial is completely reducible"
---

The proof proceeds by case analysis on the minimum polynomial $\mu$ of $\varphi$.

\textbf{Type I:} If the minimum polynomial is completely reducible and all its roots equal $1$, then, as argued in the earlier part of the classification (not fully reproduced in this section), $\varphi$ is diagonalizable with all eigenvalues $1$, hence $\varphi = \iota$. The space $E$ decomposes as a direct sum of $1$-dimensional eigenspaces, making it completely reducible.

\textbf{Type II:} If $\mu$ is completely reducible and not all roots equal $1$, the analysis of this section shows that $\varphi$ has eigenvalues $\lambda \neq 1$ and $1/\lambda$. The corresponding eigenvectors span a pseudo-Euclidean plane $F$ of index $1$. The orthogonal complement $F^\perp$ is a Euclidean plane on which $\varphi$ acts as $\pm \iota$. Thus $E = F \oplus F^\perp$ is the direct sum of an invariant pseudo-Euclidean plane and an invariant Euclidean plane. The irreducibility of each plane follows from the eigenvalue structure: $F$ is irreducible unless the induced mapping is $\iota$ (which would mean $\lambda = 1$, contradicting $\lambda \neq 1$), and $F^\perp$ is irreducible as a Euclidean plane under a rotation of angle $0$ or $\pi$.

\textbf{Type III:} If $\mu = (t-1)^k$ with $3 \leq k \leq 4$, the analysis above shows the existence of a light-like eigenvector $e$. The $1$-dimensional subspace $\langle e \rangle$ is not space-like (it lies on the light cone), but there exists a space-like $1$-dimensional stable subspace (corresponding to the Euclidean part of the decomposition). The complementary $3$-dimensional subspace $E_1 = e^\perp$ has index $2$ and carries an irreducible action of $\varphi$ (for $k = 3$ or $4$). Thus $E$ decomposes as the direct sum of a $1$-dimensional space-like eigenspace and an irreducible $3$-dimensional subspace of index $2$.

The three types are mutually exclusive and exhaustive, completing the classification.
