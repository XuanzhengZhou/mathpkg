---
role: proof
locale: en
of_concept: lemma-point-line-coordinate-incidence
source_book: gtm006
source_chapter: "II"
source_section: "3"
---

The point $\langle x e_1 + y e_2 + e_3 \rangle$ is on the line joining $\langle m e_2 + e_1 \rangle$ to $\langle b e_2 + e_3 \rangle$ if and only if the vector $x e_1 + y e_2 + e_3$ is a linear combination of $m e_2 + e_1$ and $b e_2 + e_3$.

Suppose $x e_1 + y e_2 + e_3 = c (m e_2 + e_1) + d (b e_2 + e_3)$. Equating coefficients of $e_3$ gives $d = 1$. Equating coefficients of $e_1$ gives $c = x$. Then equating coefficients of $e_2$ yields
$$y = c m + d b = x m + b.$$

Conversely, if $y = x m + b$, then
$$x e_1 + y e_2 + e_3 = x e_1 + (x m + b) e_2 + e_3 = x (m e_2 + e_1) + (b e_2 + e_3),$$
so the point lies on the line. $\square$
