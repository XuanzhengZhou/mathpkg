---
role: proof
locale: en
of_concept: antisymmetry-double-associator
source_book: gtm006
source_chapter: "6"
source_section: "7. The Skornyakov-San Soucie Theorem"
---

By (9), $0 = [[a, b + c], a, b + c]$. Expanding by linearity and applying (9):
$$\begin{aligned}
0 &= [[a, b + c], a, b] + [[a, b + c], a, c] \\
&= [[a, b], a, b] + [[a, c], a, b] + [[a, b], a, c] + [[a, c], a, c] \\
&= [[a, c], a, b] + [[a, b], a, c].
\end{aligned}$$
The first and fourth terms vanish by (9). Thus $[[a, b], a, c] = -[[a, c], a, b]$. $\square$
