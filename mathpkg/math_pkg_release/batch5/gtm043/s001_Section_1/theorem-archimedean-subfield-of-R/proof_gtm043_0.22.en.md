---
role: proof
locale: en
of_concept: theorem-archimedean-subfield-of-R
source_book: gtm043
source_chapter: "0"
source_section: "0.22"
---

Obviously, every subfield of $\mathbf{R}$ is archimedean.

Conversely, let $F$ be any archimedean field. Given $x < y$ in $F$, choose $n \in \mathbf{N}$ such that $n > 1/(y - x)$ (possible by the archimedean property), and let $m$ be the smallest integer $> nx$. Then
$$x < \frac{m}{n} < y.$$
This shows that $\mathbf{Q}$ is dense in $F$, so that every element of $F$ is uniquely determined by a Dedekind cut of $\mathbf{Q}$. Consequently, $F$ is embeddable in $\mathbf{R}$ in a unique way as an ordered set.

Now, if $r$ and $s$ belong to the ordered field $F$, and if $a, b, c$, and $d$ are rationals satisfying $a \leq r < b$ and $c \leq s < d$, then the inequalities $a + c \leq r + s < b + d$ and corresponding multiplicative estimates show that the embedding preserves the field operations. Hence $F$ is isomorphic to a subfield of $\mathbf{R}$.
