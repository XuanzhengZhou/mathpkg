---
role: proof
locale: en
of_concept: extreme-points-of-compact-convex-hull
source_book: gtm003
source_chapter: "10"
source_section: "Compact Convex Sets"
---

Let $x_0$ be an extreme point of $C$, and $V$ any closed convex $0$-neighborhood. There exist points $y_i \in A$ ($i = 1, \ldots, n$), with $A \subset \bigcup_i (y_i + V)$. Denote by $W_i$ the closed, convex hull of $A \cap (y_i + V)$. Since $W_i$ (which are subsets of $C$) are compact, by (10.2) so is the convex hull of their union which is, therefore, identical with $C$. Hence $x_0 = \sum_{i=1}^{n} \lambda_i w_i$, where $w_i \in W_i$, $\lambda_i \geq 0$ ($i = 1, \ldots, n$) and $\sum_{i=1}^{n} \lambda_i = 1$. $x_0$ being an extreme point of $C$, it follows that $x_0 = w_i$ for some $i$; hence $x_0 \in W_i \subset y_i + V$, and since $y_i \in A$, it follows that $x_0 \in A + V$. Since $V$ is an arbitrary member of a $0$-neighborhood base and $A$ is closed, it follows that $x_0 \in A$.
