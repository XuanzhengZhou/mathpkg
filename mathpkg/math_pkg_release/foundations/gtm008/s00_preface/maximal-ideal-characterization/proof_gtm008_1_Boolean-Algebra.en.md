---
role: proof
locale: en
of_concept: maximal-ideal-characterization
source_book: gtm008
source_chapter: "1"
source_section: "Boolean Algebra"
---

**Proof.** If $b \in |B|$ and both $b \in I$ and $-b \in I$, then $1 = b + (-b) \in I$, contradicting that $I$ is proper. So at most one holds.

If $I$ is maximal, suppose there exists $b$ such that $b \notin I$ and $-b \notin I$. Define $J = \{x + y \mid x \leq b \land y \in I\}$. Then $J$ is an ideal properly containing $I$ (since $b = b + 0 \in J$), and $J \neq |B|$ (since $-b \notin J$, otherwise $-b = x + y$ with $x \leq b$, $y \in I$ gives the contradiction $-b = (-b)(-b) = (x+y)(-b) = y(-b) \in I$). This contradicts maximality of $I$. Thus $(\forall b)[b \in I \lor -b \in I]$.

Conversely, if $I \subseteq J$ with $J$ a proper ideal, then $(\exists b \in J)[b \notin I]$. Hence $-b \in I \subseteq J$, so $1 = b + (-b) \in J$, contradicting $J$ proper. Thus $I$ is maximal.
