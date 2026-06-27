---
role: proof
locale: en
of_concept: euler-characteristic-additivity-theorem
source_book: gtm047
source_chapter: "21"
source_section: "21"
---

Let $V_1, E_1, F_1$ be the vertex, edge, and face counts of $K_1$, and $V_2, E_2, F_2$ those of $K_2$. Let $V_J, E_J$ be the vertex and edge counts of the polygon $J$. In $K_1 \cup K_2$, the total vertex count is $V_1 + V_2 - V_J$, the total edge count is $E_1 + E_2 - E_J$, and the total face count is $F_1 + F_2$ (since $J$ is $1$-dimensional). Therefore
$$
\chi(K_1 \cup K_2) = (V_1 + V_2 - V_J) - (E_1 + E_2 - E_J) + (F_1 + F_2) = \chi(K_1) + \chi(K_2) - \chi(J).
$$
Since $J$ is a polygon, $V_J = E_J$, so $\chi(J) = V_J - E_J = 0$. Thus $\chi(K_1 \cup K_2) = \chi(K_1) + \chi(K_2)$.
