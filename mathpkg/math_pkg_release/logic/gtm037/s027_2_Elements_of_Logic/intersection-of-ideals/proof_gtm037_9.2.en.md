---
role: proof
locale: en
of_concept: intersection-of-ideals
source_book: gtm037
source_chapter: "9"
source_section: "2"
---

Let $\{I_j : j \in J\}$ be a nonempty family of ideals of $\mathfrak{A}$. Let $K = \bigcap_{j \in J} I_j$.

First, $K$ is nonempty since $0 \in I_j$ for all $j$, hence $0 \in K$.

If $x \leq y$ and $y \in K$, then $y \in I_j$ for all $j$. Since each $I_j$ is an ideal, $x \in I_j$ for all $j$, so $x \in K$.

If $x, y \in K$, then $x, y \in I_j$ for all $j$. Since each $I_j$ is an ideal, $x + y \in I_j$ for all $j$, so $x + y \in K$.

Thus $K$ is an ideal. The proof for filters is analogous.
