---
role: proof
locale: en
of_concept: idempotent-matrix-form
source_book: gtm031
source_chapter: "2"
source_section: "12"
---

If $E_1$ is idempotent, then $E_2 = 1 - E_1$ satisfies $E_2^2 = (1-E_1)^2 = 1 - 2E_1 + E_1^2 = 1 - E_1 = E_2$, so $E_2$ is also idempotent. Moreover $E_1 E_2 = E_1(1-E_1) = E_1 - E_1^2 = 0$ and similarly $E_2 E_1 = 0$, so $E_1$ and $E_2$ are orthogonal. Since $E_1 + E_2 = 1$, they form a supplementary set. By the theorem on supplementary orthogonal projections, there exists a basis $(f_1, \ldots, f_n)$ of $\mathfrak{R}$ such that the matrix of $E_1$ relative to this basis has the diagonal form with $1$'s corresponding to the basis vectors spanning $\mathfrak{R}E_1$ (the rank space) and $0$'s corresponding to the basis vectors spanning $\mathfrak{R}E_2$ (the null space). The number of $1$'s is $\dim(\mathfrak{R}E_1) = \operatorname{Rank} E_1$.
