---
role: proof
locale: en
of_concept: iwasawa-structure-theorem-matrix-form
source_book: gtm059
source_chapter: "5"
source_section: "Iwasawa Theory and Ideal Class Groups"
---

By the Weierstrass preparation theorem, every element of $\Lambda = \mathbb{Z}_p[[X]]$ can be written as $p^\mu \cdot u(X) \cdot f(X)$ where $u(X)$ is a unit in $\Lambda$ and $f(X)$ is a distinguished polynomial. Using this, we define the degree of a non-zero element of $\Lambda$ as the degree of its distinguished polynomial factor (or $\infty$ if the element is divisible by $p$).

Let $\deg(R)$ denote the minimal degree among non-zero entries of $R$, and let $\deg^{\text{OP}}(R)$ be the minimal degree achievable by admissible row and column operations. The proof proceeds by induction on $\deg^{\text{OP}}(R)$.

By applying admissible operations, we may assume that an entry of minimal degree $\deg^{\text{OP}}(R)$ appears in position $(1,1)$. Using the Euclidean algorithm in $\mathbb{Z}_p[X]$ (via the division algorithm for distinguished polynomials), we can eliminate all other entries in the first row and first column, obtaining a matrix with the distinguished polynomial $f_1$ in position $(1,1)$ and zeros elsewhere in the first row and column.

Repeating this process on the submatrix obtained by deleting the first row and column, and using the fact that $\Lambda$ is a unique factorization domain modulo units, we obtain divisibility relations between successive distinguished polynomials. The process terminates after finitely many steps because the degree strictly decreases at each stage, yielding the diagonal form with $f_1 \mid f_2 \mid \cdots \mid f_r$.
