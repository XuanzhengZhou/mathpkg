---
role: proof
locale: en
of_concept: hilberts-tenth-problem-unsolvable
source_book: gtm022
source_chapter: "X"
source_section: "1"
---

Suppose there is an algorithm deciding solvability of Diophantine equations. Since every recursively enumerable set $E$ is diophantine, there is a polynomial $P$ such that $x \in E$ iff $(\exists y_1, \ldots, y_m) P(x, y_1, \ldots, y_m) = 0$. The algorithm would then decide membership in $E$, making $E$ recursive. But there exist recursively enumerable sets that are not recursive (e.g., the Halting Problem). Contradiction.
