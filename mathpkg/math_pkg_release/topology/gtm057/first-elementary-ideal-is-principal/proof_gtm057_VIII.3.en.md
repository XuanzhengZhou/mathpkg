---
role: proof
locale: en
of_concept: first-elementary-ideal-is-principal
source_book: gtm057
source_chapter: "VIII"
source_section: "3"
---

Let $(\mathbf{x} : \mathbf{r})$ be an over presentation with $n$ generators and $n-1$ relators. By Theorem (1.1) of Chapter VIII, all generators are mapped to the same element under the abelianizer, so condition (3.6) of Chapter VIII holds. Theorem (3.7) then asserts that the Alexander matrix $A$ of $(\mathbf{x} : \mathbf{r})$ is equivalent to the matrix obtained by replacing any column of $A$ with a column of zeros.

Since $A$ is an $(n-1) \times n$ matrix, after replacing one column with zeros, at most one $(n-1) \times (n-1)$ submatrix can have a non-zero determinant (the one omitting the zeroed column). Thus all $(n-1) \times (n-1)$ determinants are associates, and the ideal they generate is principal. Since equivalent matrices define the same elementary ideals, $E_1$ is principal.

By Theorem (3.2) of Chapter VIII, the knot polynomial $\Delta_1$ is the greatest common divisor of all $(n-1) \times (n-1)$ subdeterminants. When $E_1$ is principal, $\Delta_1$ is any generator of $E_1$, and $E_1 = (\Delta_1)$.
