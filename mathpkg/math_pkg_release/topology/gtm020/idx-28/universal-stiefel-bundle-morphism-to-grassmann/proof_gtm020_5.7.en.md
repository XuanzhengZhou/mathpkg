---
role: proof
locale: en
of_concept: universal-stiefel-bundle-morphism-to-grassmann
source_book: gtm020
source_chapter: "5"
source_section: "7"
---

For $a \in U_F(k)$, let $(v_1, \ldots, v_k)a = (v'_1, \ldots, v'_k)$ and $a y = y'$, where $y'_m = \sum_j a_{m,j} y_j$. Then the image under $f$ of the transformed data is

$$(\langle v'_1, \ldots, v'_k \rangle, \; \sum_m y'_m v_m) = (\langle v_1, \ldots, v_k \rangle, \; \sum_{m,j} a_{m,j} y_j v_m).$$

On the other hand, computing $\sum_j y_j v'_j$ we have $v'_j = \sum_i v_i a_{i,j}$, so

$$\sum_j y_j v'_j = \sum_{i,j} y_j v_i a_{i,j} = \sum_{i,j} a_{i,j} y_j v_i.$$

Since $a \in U_F(k)$, we have $a_{i,j} = a_{j,i}$ in the orthogonal case and appropriate relations in the unitary/symplectic cases, and the two sums match. Hence $f$ is well-defined on the quotient by the $U_F(k)$-action.
