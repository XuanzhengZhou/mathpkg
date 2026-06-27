---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Matrix inequalities of the form $A \geq B$ or $B \leq A$ are preserved when both sides of the inequality are multiplied by a non-negative matrix. Inequalities of the form $A > B$ or $B < A$ are preserved when both sides are multiplied by a positive matrix, provided the products have all entries finite.

Next we consider the problem of "block multiplication" of matrices. The picture we have in mind is the following decomposition of the matrices involved in a product:

$$\begin{pmatrix} A_1 & A_2 \\ A_3 & A_4 \end{pmatrix} \begin{pmatrix} B_1 & B_2 \\ B_3 & B_4 \end{pmatrix} = \begin{pmatrix} C_1 & C_2 \\ C_3 & C_4 \end{pmatrix}.$$

More specifically, let $K, M,$ and $N$ be index sets and let $K', M',$ and $N'$, respectively, be non-empty subsets of the index sets. Impose orderings on $K, M,$ and $N$ so that the elements of $K', M',$ and $N'$ precede the other elements, which comprise the complementary sets $\tilde{K}', \tilde{M}',$ and $\tilde{N}'$. Let $A, B,$ and $C$ be matrices such that

(1) $A$ is defined on $K$ and $M$,
(2) $B$ is defined on $M$ and $N$, and
(3) $AB = C$ is well defined.

Let matrices $A_1, A_2, A_3,$ and $A_4$ be defined as the restriction of the function $A$ to the sets

(1) $K'$ and $M'$ for $A_1$
(2) $K'$ and $\tilde{M}'$ for $A_2$
(3) $\tilde

multiply as if they were entries themselves. Its proof depends on the fact that matrix multiplication is defined independently of any ordering on the index sets.
