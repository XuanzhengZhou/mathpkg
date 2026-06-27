---
role: proof
locale: en
of_concept: discriminant-zero-independent-of-basis
source_book: gtm028
source_chapter: "I"
source_section: "11"
---
Let $d = d(\omega_1, \dots, \omega_n)$ be the discriminant of one basis and $d' = d(\omega'_1, \dots, \omega'_n)$ be the discriminant of another basis. By the change-of-basis formula, $d' = d \cdot (\det A)^2$ where $A$ is the transition matrix.

If $d = 0$, then $d' = 0 \cdot (\det A)^2 = 0$. Since $A$ is invertible (it is a transition matrix between two bases), $\det A \neq 0$, and the converse also holds: $d' = 0$ implies $d = 0$.

Thus the property of having zero discriminant is basis-independent.
