---
role: proof
locale: en
of_concept: cubics-up-to-seven-base-points
source_book: gtm052
source_chapter: "V"
source_section: "4"
---

It suffices to consider the case $r = 7$. We first show that if $P_1, \ldots, P_7$ are all ordinary points, then $\mathfrak{d}$ has no unassigned ordinary base points. For any point $Q$ not equal to any $P_i$, we exhibit a cubic curve containing $P_1, \ldots, P_7$ but not $Q$.

**Case 1.** Suppose three of the points, say $P_1, P_2, P_3$, lie on a line $L^*$ with $Q$. Since no four are collinear, we may assume $P_4, P_5, P_6$ are not collinear. Then the conic $\Gamma_{12456}$ through $P_1, P_2, P_4, P_5, P_6$, together with the line $L_{37}$ through $P_3$ and $P_7$, forms a cubic containing $P_1, \ldots, P_7$ but not $Q$. Indeed, if $Q \in \Gamma_{12456}$, then this conic would contain the line $L^*$, making it reducible and forcing $P_4, P_5, P_6$ collinear -- contradiction. If $Q \in L_{37}$, then $P_7 \in L^*$, so four points would be collinear -- contradiction.

**Case 2.** No set of three points containing $Q$ is collinear. In this case one constructs a suitable cubic through $P_1, \ldots, P_7$ avoiding $Q$ using conics and lines in an analogous fashion. The argument extends to the case where $P_2$ is infinitely near $P_1$ by similar geometric reasoning.
