---
role: proof
locale: en
of_concept: kronecker-product-matrix-multiplication-rule
source_book: gtm031
source_chapter: "7"
source_section: "4"
---

This rule follows directly from the corresponding identity for linear transformations. For linear transformations $A, C \in \mathfrak{L}(\Re, \Re)$ and $B, D \in \mathfrak{L}(\mathfrak{S}, \mathfrak{S})$, we have

$$(A \times B)(C \times D) = AC \times BD.$$

Indeed, for any $x \in \Re$ and $y \in \mathfrak{S}$,

$$(A \times B)(C \times D)(x \times y) = (A \times B)(Cx \times Dy) = A(Cx) \times B(Dy) = (AC)x \times (BD)y = (AC \times BD)(x \times y).$$

Taking matrices relative to the lexicographically ordered basis $e_i \times f_j$ of $\Re \times \mathfrak{S}$, the matrix of $A \times B$ is $(\alpha) \times (\beta)$, the matrix of $C \times D$ is $(\gamma) \times (\delta)$, the matrix of $AC$ is $(\alpha)(\gamma)$, and the matrix of $BD$ is $(\beta)(\delta)$. The identity of linear transformations therefore yields the matrix identity

$$((\alpha) \times (\beta))((\gamma) \times (\delta)) = (\alpha)(\gamma) \times (\beta)(\delta).$$
