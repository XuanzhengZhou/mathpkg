---
role: proof
locale: en
of_concept: properties-of-open-sets
source_book: gtm011
source_chapter: "II"
source_section: "1"
---
The proof follows directly from the definition of an open set. For (a), $X$ is open because $B(x; \epsilon) \subset X$ for any $\epsilon > 0$ and any $x \in X$, and $\emptyset$ is vacuously open. For (b), if $x \in \bigcap_{k=1}^n G_k$, then for each $k$ there exists $\epsilon_k > 0$ such that $B(x; \epsilon_k) \subset G_k$. Taking $\epsilon = \min\{\epsilon_1, \ldots, \epsilon_n\} > 0$ gives $B(x; \epsilon) \subset \bigcap_{k=1}^n G_k$. For (c), if $x \in \bigcup_{i \in I} G_i$, then $x \in G_{i_0}$ for some $i_0$, so there exists $\epsilon > 0$ with $B(x; \epsilon) \subset G_{i_0} \subset \bigcup_{i \in I} G_i$.
