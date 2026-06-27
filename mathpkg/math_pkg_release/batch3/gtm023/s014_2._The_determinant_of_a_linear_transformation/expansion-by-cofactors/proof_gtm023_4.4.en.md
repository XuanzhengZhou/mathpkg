---
role: proof
locale: en
of_concept: expansion-by-cofactors
source_book: gtm023
source_chapter: "4"
source_section: "4"
---

From the relations (4.35) and (4.30) in the text, the cofactor matrix $\beta_j^i$ satisfies the expansion formula (4.38):

$$\det A = \sum_j \alpha_i^j \beta_j^i \quad (i = 1, \ldots, n).$$

It is shown in Section 4.14 that $\beta_j^i = (-1)^{i+j} \det S_i^j$, where $S_i^j$ is the $(n-1) \times (n-1)$-matrix obtained by deleting the $i$-th row and $j$-th column. Substituting this into the expansion formula yields:

$$\det A = \sum_j (-1)^{i+j} \alpha_i^j \det S_i^j.$$

The expansion with respect to the $j$-th column follows by the same argument applied to the transposed matrix and using the fact that $\det A = \det A^*$.
