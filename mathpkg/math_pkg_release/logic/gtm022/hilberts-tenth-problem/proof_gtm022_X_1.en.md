---
role: proof
locale: en
of_concept: "hilberts-tenth-problem"
source_book: gtm022
source_chapter: "X"
source_section: "1"
---
Proof. Let $E$ be a recursively enumerable but non-recursive subset of $\mathbb{N}$. By the MRDP Theorem, $E$ is diophantine, so there is a polynomial $P$ such that $x \in E$ iff $(\exists y_1, \ldots, y_m) P(x, y_1, \ldots, y_m) = 0$. If there were a decision procedure for Diophantine equations, one could decide membership in $E$ by checking $P(n, y_1, \ldots, y_m) = 0$, contradicting the non-recursiveness of $E$. $\square$
