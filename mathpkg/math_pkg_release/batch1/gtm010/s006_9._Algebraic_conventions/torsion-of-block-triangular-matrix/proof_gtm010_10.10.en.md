---
role: proof
locale: en
of_concept: torsion-of-block-triangular-matrix
source_book: gtm010
source_chapter: "10"
source_section: "10"
---

The middle matrix $\begin{pmatrix} A & X \\ 0 & B \end{pmatrix}$ can be decomposed:
$$\begin{pmatrix} A & X \\ 0 & B \end{pmatrix} = \begin{pmatrix} A & 0 \\ 0 & I \end{pmatrix} \begin{pmatrix} I & A^{-1}X \\ 0 & B \end{pmatrix}$$
and the second factor is equivalent to $\begin{pmatrix} I & 0 \\ 0 & B \end{pmatrix}$ via row operations. Then
$$\tau \begin{pmatrix} A & X \\ 0 & B \end{pmatrix} = \tau \begin{pmatrix} A & 0 \\ 0 & B \end{pmatrix} = \tau(A) + \tau \begin{pmatrix} I_n & 0 \\ 0 & B \end{pmatrix}.$$
By row/column interchanges (II_R, II_C), $\begin{pmatrix} I_n & 0 \\ 0 & B \end{pmatrix} \sim \begin{pmatrix} B & 0 \\ 0 & I_n \end{pmatrix}$, giving $\tau(A) + \tau(B)$.
