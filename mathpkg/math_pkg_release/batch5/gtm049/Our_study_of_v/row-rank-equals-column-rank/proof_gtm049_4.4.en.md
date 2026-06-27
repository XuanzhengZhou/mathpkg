---
role: proof
locale: en
of_concept: row-rank-equals-column-rank
source_book: gtm049
source_chapter: "IV"
source_section: "4.4"
---

First proof (using linear mappings): From the symmetry of the matrix $PAQ = \begin{pmatrix} I_r & 0 \\ 0 & 0 \end{pmatrix}$, we have
$$
\text{row rank of } A = \text{row rank of } PAQ = \text{column rank of } Q^t A^t P^t.
$$
Since $P, Q$ are invertible, their transposes are also invertible, and the result follows.

Alternative proof (independent of linear mappings): Let $r, c$ be the row and column ranks of $A$. Without loss of generality the first $r$ rows of $A$ are linearly independent and all rows are linearly dependent on the first $r$. Thus there exist scalars $x_{ik}$ such that
$$
a_{ij} = \sum_{k=1}^{r} x_{ik} a_{kj} \quad \text{for } i = 1, \ldots, m \text{ and } j = 1, \ldots, n.
$$
Writing this as a matrix factorization shows each column of $A$ depends linearly on the $r$ columns of $(x_{ik})$, so $c \leq r$. A symmetric argument gives $r \leq c$, hence $r = c$.
