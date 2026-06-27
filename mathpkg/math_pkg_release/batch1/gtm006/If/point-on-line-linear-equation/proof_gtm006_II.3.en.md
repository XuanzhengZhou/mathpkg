---
role: proof
locale: en
of_concept: point-on-line-linear-equation
source_book: gtm006
source_chapter: "II"
source_section: "3"
---

The point $P = \langle x e_1 + y e_2 + e_3 \rangle$ lies on the line joining $Q = \langle m e_2 + e_1 \rangle$ to $R = \langle b e_2 + e_3 \rangle$ if and only if the vector $x e_1 + y e_2 + e_3$ is a linear combination of $m e_2 + e_1$ and $b e_2 + e_3$. Suppose

$$x e_1 + y e_2 + e_3 = c(m e_2 + e_1) + d(b e_2 + e_3).$$

Equating coefficients of $e_3$ on both sides gives $1 = d$. Equating coefficients of $e_1$ gives $x = c$. Equating coefficients of $e_2$ then yields $y = cm + db = xm + b$ as required.

Conversely, if $y = xm + b$, then

$$x e_1 + y e_2 + e_3 = x(m e_2 + e_1) + (b e_2 + e_3),$$

showing that the vector is indeed a linear combination of $m e_2 + e_1$ and $b e_2 + e_3$, so $P$ lies on the line $QR$. $\square$
