---
role: proof
locale: en
of_concept: proper-filter-boolean-algebra-iff-filter-associated-partial-order
source_book: gtm008
source_chapter: "5"
source_section: "Partial Order Structures and Topological Spaces"
---

Let $F$ be a proper filter for $B$. Then $0 \notin F$, i.e., $F \subseteq B - \{0\}$. If $x, y \in F$ then $xy \in F$ and hence there exists a $z \in F$, namely $xy$, such that $z \leq x$ and $z \leq y$. Thus $F$ is strongly compatible. Moreover, if $x \in F$ and $x \leq y$ then $xy = x \in F$, so by the filter property $y = x + y \in F$, establishing that $F$ is upward hereditary. Therefore $F$ is a filter for $P$.

Conversely, let $F$ be a filter for $P$. If $x, y \in F$ then there is a $z \in F$ such that $z \leq x$ and $z \leq y$. Hence $z \leq xy$, and since $F$ is upward hereditary, $xy \in F$. Furthermore, since $0 \notin P$, it follows that $0 \notin F$. Thus $F$ is a proper filter for $B$.
