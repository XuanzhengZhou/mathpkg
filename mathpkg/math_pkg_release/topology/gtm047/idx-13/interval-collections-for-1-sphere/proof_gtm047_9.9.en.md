---
role: proof
locale: en
of_concept: interval-collections-for-1-sphere
source_book: gtm047
source_chapter: "9"
source_section: "9"
---

Every $G_i$ is a finite collection. Under the conditions for $G_1$, there is an $H_1$ satisfying (1) and (2). If the elements of $H_1$ are sufficiently short, then $H_1$ will also satisfy (3). Now proceed recursively to define $H_2, H_3, \ldots$. At each stage, in forming $H_{i+1}$, we retain the intervals which already appear in $H_i$, and then make the new intervals sufficiently short so that (3) and (4) are satisfied. $\square$

The existence of $H_1$ follows from Theorem 2 (linear accessibility density): for each endpoint $v$ of an arc $g \in G_1$, choose a sufficiently short linear interval $vv'$ into $I$. By making these intervals short enough and choosing endpoints consistently (one per arc endpoint), conditions (1)-(3) are satisfied. The recursive construction preserves intervals from $H_i$ and adds new, shorter intervals from newly introduced endpoints, ensuring the nesting condition (4).
