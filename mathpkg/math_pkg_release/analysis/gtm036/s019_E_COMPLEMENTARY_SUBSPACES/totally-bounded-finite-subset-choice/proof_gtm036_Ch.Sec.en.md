---
role: proof
locale: en
of_concept: totally-bounded-finite-subset-choice
source_book: gtm036
source_chapter: ""
source_section: "F"
---

Given a neighborhood $U$ of $0$, choose a symmetric neighborhood $V$ with $V + V \subset U$. Since $B$ is totally bounded, there exists a finite set $M$ such that $B \subset M + V$. For each $m \in M$ such that $(m + V) \cap B \neq \emptyset$, choose a point $b_m \in B \cap (m + V)$. Let $N = \{b_m : (m + V) \cap B \neq \emptyset\}$. Then $N \subset B$ is finite, and for any $b \in B$, there exists $m \in M$ with $b \in m + V$. Since $(m + V) \cap B \neq \emptyset$, we have $b_m \in N$, and $b - b_m = (b - m) + (m - b_m) \in V + V \subset U$. Thus $b \in b_m + U \subset N + U$, so $B \subset N + U$.
