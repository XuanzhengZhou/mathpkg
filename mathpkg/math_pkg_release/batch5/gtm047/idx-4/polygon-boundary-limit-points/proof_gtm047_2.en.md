---
role: proof
locale: en
of_concept: polygon-boundary-limit-points
source_book: gtm047
source_chapter: "2"
source_section: "Separation Properties of Polygons in R^2"
---

Let $F = \operatorname{Fr} I = \overline{I} - I$ (by Theorem 4, since $I$ is open). Then $F$ separates $\mathbf{R}^2$:
$$\mathbf{R}^2 - F = I \cup (\mathbf{R}^2 - \overline{I}),$$
and the sets on the right are disjoint, open, and nonempty; $\mathbf{R}^2 - \overline{I}$ contains $E$; $F \subset J$, and $F$ is closed.

If $F \neq J$, then $F$ lies in a broken line $B \subset J$. Now
$$\mathbf{R}^2 - B = I \cup [\mathbf{R}^2 - (I \cup B)].$$

But by Theorem 3, no broken line separates $\mathbf{R}^2$, so $\mathbf{R}^2 - B$ is connected -- a contradiction. Therefore $F = J$, and every point of $J$ is a limit point of $I$. A symmetric argument shows that every point of $J$ is also a limit point of $E$. $\square$
