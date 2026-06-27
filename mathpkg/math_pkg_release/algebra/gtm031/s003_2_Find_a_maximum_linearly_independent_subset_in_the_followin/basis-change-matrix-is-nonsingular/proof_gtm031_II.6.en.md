---
role: proof
locale: en
of_concept: basis-change-matrix-is-nonsingular
source_book: gtm031
source_chapter: "II"
source_section: "6"
---

Let $(\alpha)$ be the matrix of the ordered basis $(f_1, f_2, \ldots, f_n)$ relative to $(e_1, e_2, \ldots, e_n)$, so that $f_j = \sum_i \alpha_{ij} e_i$. Let $(\beta)$ be the matrix of $(e_1, e_2, \ldots, e_n)$ relative to $(f_1, f_2, \ldots, f_n)$, so that $e_i = \sum_k \beta_{ki} f_k$. Substituting the expression for $f_k = \sum_j \alpha_{jk} e_j$ into $e_i = \sum_k \beta_{ki} f_k$, we obtain

$$e_i = \sum_k \beta_{ki} \left( \sum_j \alpha_{jk} e_j \right) = \sum_j \left( \sum_k \beta_{ki} \alpha_{jk} \right) e_j.$$

Since the $e_i$ form a basis, the coefficient of $e_j$ in the expansion of $e_i$ must be $1$ when $i = j$ and $0$ otherwise. Hence $\sum_k \alpha_{jk} \beta_{ki} = \delta_{ji}$, which means $(\alpha)(\beta) = 1$. Reversing the roles of the two bases gives $(\beta)(\alpha) = 1$. Therefore $(\alpha)$ is non-singular with inverse $(\beta)$. Equivalently, the matrix of $(e_i)$ relative to $(f_i)$ is the inverse of the matrix of $(f_i)$ relative to $(e_i)$.
