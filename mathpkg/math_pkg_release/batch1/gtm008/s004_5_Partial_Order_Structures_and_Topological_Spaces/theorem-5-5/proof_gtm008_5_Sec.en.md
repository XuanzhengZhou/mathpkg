---
role: proof
locale: en
of_concept: theorem-5-5
source_book: gtm008
source_chapter: "5"
source_section: "5 Partial Order Structures and Topological Spaces

In the work"
---
Let $F$ be a proper filter for $B$. Then $0 \notin F$ i.e., $F \subseteq B - \{0\}$. If $x, y \in F$ then $xy \in F$ and hence there exists a $z \in F$, namely $xy$, such that $z \leq x$ and $z \leq y$. Thus $F$ is a filter for $P$.

Conversely let $F$ be a filter for $P$. If $x, y \in F$ then there is a $z \in F$ such that $z \leq x$ and $z \leq y$. Therefore $z \leq xy$ and since $F$ is upward hereditary $xy \in F$. Furthermore since $0 \notin P$ it follows that $0 \notin F$ i.e., $F$ is a proper filter for $B$.
