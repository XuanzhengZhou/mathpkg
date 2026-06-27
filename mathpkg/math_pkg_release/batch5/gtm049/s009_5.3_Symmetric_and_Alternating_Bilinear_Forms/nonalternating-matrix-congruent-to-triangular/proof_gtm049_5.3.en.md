---
role: proof
locale: en
of_concept: nonalternating-matrix-congruent-to-triangular
source_book: gtm049
source_chapter: "5"
source_section: "5.3"
---

**PROOF.** By Theorem 4, $V = A_1 \oplus \cdots \oplus A_r \oplus V^\perp$ where each $A_i = [a_i]$ is one-dimensional non-degenerate and $\sigma(A_i, A_j) = 0$ for $i < j$. With respect to the ordered basis $(a_1, \ldots, a_r, a_{r+1}, \ldots, a_n)$ where $(a_{r+1}, \ldots, a_n)$ is a basis of $V^\perp$, the matrix of $\sigma$ has zeros above the diagonal (since $\sigma(a_i, a_j) = 0$ for $i < j$) and the rows beyond $r$ are identically zero. Thus the matrix is lower triangular.
