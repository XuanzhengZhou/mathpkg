---
role: proof
locale: en
of_concept: dual-of-space-of-continuous-linear-maps-under-simple-convergence
source_book: gtm003
source_chapter: "IV"
source_section: "4"
---

If $v = \sum_i x_i \otimes y_i' \in E \otimes F'$, the mapping $v \mapsto f$ where $f(u) = \sum_i \langle u x_i, y_i' \rangle$ is a linear map of $E \otimes F'$ into $\mathcal{L}_s(E, F)'$. This map is injective (biunivocal), since the bilinear form $(v, u) \mapsto f(u)$ places even the subspace $E' \otimes F$ of $\mathcal{L}(E, F)$ in separated duality with $E \otimes F'$ (Section 1, Example 4).

To show surjectivity: Since $\mathcal{L}_s(E, F)$ is a subspace of the product space $F^E$ (with the product topology of simple convergence), every continuous linear form $g \in \mathcal{L}_s(E, F)'$ is the restriction of a continuous linear form on $F^E$. By Theorem 4.3, the dual of $F^E$ consists of finite sums $\sum_i \langle \cdot, y_i' \rangle$ evaluated at finitely many points $x_i \in E$. Hence $g$ is of the form
$$u \mapsto g(u) = \sum_i \langle u x_i, y_i' \rangle$$
for suitable finite subsets $\{x_i\} \subset E$ and $\{y_i'\} \subset F'$, which corresponds to the tensor $\sum_i x_i \otimes y_i'$.
