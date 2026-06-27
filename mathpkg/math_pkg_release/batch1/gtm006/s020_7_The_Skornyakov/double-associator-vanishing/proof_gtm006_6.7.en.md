---
role: proof
locale: en
of_concept: double-associator-vanishing
source_book: gtm006
source_chapter: "6"
source_section: "7. The Skornyakov-San Soucie Theorem"
---

Let $p = [a, a, b]$ and $q = [a, b]$. Consider $s = [[q, a, b]]$. By (7), $p \in A(a, b)$ and $q = [1, a, b]$ also satisfies relevant associator properties. Computing $h(q, s, a, b)$:

$$\begin{aligned}
0 &= h(q, s, a, b) = [qs, a, b] + [q, s, q] - q[s, a, b] - [q, a, b] s \\
&= -(qs)q + (qs)q - q(sq) + q(sq) - s^2.
\end{aligned}$$

The terms cancel pairwise: $[qs, a, b] = -(qs)q$ (by definition of $A$), $[q, s, q] = (qs)q$, $-q[s, a, b] = -q(sq)$, and $-[q, a, b]s = q(sq)$. Thus $s^2 = 0$, and since $D$ is a division ring, $s = 0$. Hence $[[a, b], a, b] = 0$. $\square$
