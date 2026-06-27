---
role: proof
locale: en
of_concept: bijection-linear-transformations-matrices
source_book: gtm031
source_chapter: "II"
source_section: "3"
---

**Injectivity**: If $A \mapsto (\alpha)$, then $e_i A = \sum_j \alpha_{ij} f_j$. Since $A$ is uniquely determined by its action on the basis $(e_i)$, and the $\alpha_{ij}$ completely specify the images of all basis vectors, the mapping $A \mapsto (\alpha)$ is injective.

**Surjectivity**: Let $(\alpha)$ be any $n_1 \times n_2$ matrix. Define vectors $u_i = \sum_j \alpha_{ij} f_j$ for $i = 1, \dots, n_1$. Define a mapping $A$ on $\mathfrak{R}_1$ by linear extension: for $x = \sum_i \xi_i e_i$, set $xA = \sum_i \xi_i u_i$. Then:
- For $y = \sum_i \eta_i e_i$, $x + y = \sum_i (\xi_i + \eta_i)e_i \mapsto \sum_i (\xi_i + \eta_i)u_i = \sum_i \xi_i u_i + \sum_i \eta_i u_i = xA + yA$.
- $\alpha x = \sum_i (\alpha \xi_i)e_i \mapsto \sum_i (\alpha \xi_i)u_i = \alpha(\sum_i \xi_i u_i) = \alpha(xA)$.
- $e_i = 1 \cdot e_i \mapsto 1 \cdot u_i = u_i = \sum_j \alpha_{ij} f_j$.

Thus $A$ is linear and its matrix relative to the given bases is $(\alpha)$. Hence the mapping is surjective.
