---
role: proof
locale: en
of_concept: closure-of-totally-bounded-is-totally-bounded
source_book: gtm036
source_chapter: ""
source_section: "F"
---

Let $B$ be totally bounded and let $U$ be a neighborhood of $0$. Choose a symmetric neighborhood $V$ of $0$ with $V + V \subset U$. Since $B$ is totally bounded, there exists a finite set $N \subset B$ such that $B \subset N + V$. For any $x \in \overline{B}$, there exists $b \in B \cap (x + V)$. Then $b \in n + V$ for some $n \in N$, so $x = (x - b) + (b - n) + n \in V + V + n \subset U + n$. Thus $\overline{B} \subset N + U$, proving that $\overline{B}$ is totally bounded.
