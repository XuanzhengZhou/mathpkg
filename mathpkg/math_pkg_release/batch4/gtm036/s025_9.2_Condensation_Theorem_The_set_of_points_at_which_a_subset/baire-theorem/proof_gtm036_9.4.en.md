---
role: proof
locale: en
of_concept: baire-theorem
source_book: gtm036
source_chapter: "9"
source_section: "9.2"
---

Suppose $A$ is the union of a countable number of nowhere dense sets: $A = \bigcup \{F_n : n = 1, 2, \cdots\}$. Since $F_1$ is nowhere dense, the open set $A^i \setminus F_1^{-}$ is non-void, and it follows that there is a closed sphere $V_1$ of radius at most $1$ such that $V_1 \subset A^i \setminus F_1^{-}$. Recursively, select a closed sphere $V_n$ of radius at most $2^{-n}$ such that $V_n \subset (V_{n-1})^i \setminus F_n^{-}$. This selection is possible because each $F_n$ is nowhere dense. The intersection of the sets $V_n$ is non-void, because $A$ is complete, and a point of this intersection is clearly a member of $A$ which belongs to no $F_n$. This is a contradiction.
