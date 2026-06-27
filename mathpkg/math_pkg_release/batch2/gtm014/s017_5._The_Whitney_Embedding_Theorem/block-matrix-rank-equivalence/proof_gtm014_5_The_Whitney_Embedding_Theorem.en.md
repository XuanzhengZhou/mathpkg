---
role: proof
locale: en
of_concept: block-matrix-rank-equivalence
source_book: gtm014
source_chapter: "5"
source_section: "The Whitney Embedding Theorem"
---

The matrix

$$T = \begin{pmatrix} I_k & 0 \\ -CA^{-1} & I_{m-k} \end{pmatrix}$$

is an $m \times m$ invertible matrix. Multiplying on the left by $T$ performs a row operation that eliminates the lower-left block $C$. Since $T$ is invertible, this operation preserves rank:

$$\operatorname{rank} S = \operatorname{rank} TS = \operatorname{rank} \begin{pmatrix} A & B \\ 0 & D - CA^{-1}B \end{pmatrix}.$$

Because $A$ is a $k \times k$ invertible matrix, its $k$ columns are linearly independent, so the block-triangular matrix has rank exactly $k$ if and only if the lower-right block $D - CA^{-1}B$ is the zero matrix. $\square$
