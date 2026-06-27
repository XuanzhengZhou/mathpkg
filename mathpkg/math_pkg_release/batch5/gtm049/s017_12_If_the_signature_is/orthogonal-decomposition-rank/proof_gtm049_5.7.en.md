---
role: proof
locale: en
of_concept: orthogonal-decomposition-rank
source_book: gtm049
source_chapter: "5"
source_section: "7"
---

Rank 0 is always possible (the trivial case). Assume $\operatorname{rank} \sigma = r \geq 1$. Let $V^\perp$ be the radical of $\sigma$. Since $\sigma$ induces a non-degenerate form on $V/V^\perp$, we can choose a subspace $M$ with $\dim M = r$ such that $V = M \oplus V^\perp$ and $\sigma_M$ is non-degenerate. By the Gram-Schmidt-like diagonalization process for symmetric bilinear forms (assuming the characteristic is not 2, which is implicit in the context of real quadrics), we can choose a basis of $M$ such that $\sigma_M$ is represented by a diagonal matrix with non-zero entries $a_0, \ldots, a_{r-1}$. The quadric $Q$ is then given by $a_0 X_0^2 + \cdots + a_{r-1} X_{r-1}^2 = 0$ in suitable projective coordinates.
