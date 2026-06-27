---
role: proof
locale: en
of_concept: filter-equivalence-boolean-algebra-partial-order
source_book: gtm008
source_chapter: "5"
source_section: "Partial Order Structures and Topological Spaces"
---

**Proof.** Let $F$ be a proper filter for $B$. Then $0 \notin F$, i.e., $F \subseteq B - \{0\}$. If $x, y \in F$ then $xy \in F$ and hence there exists a $z \in F$, namely $xy$, such that $z \leq x$ and $z \leq y$. Thus $F$ is strongly compatible. Also $F$ is upward hereditary as a filter of $B$, so $F$ is a filter for $\mathcal{P}$.

Conversely, let $F$ be a filter for $\mathcal{P}$. If $x, y \in F$ then there is a $z \in F$ such that $z \leq x$ and $z \leq y$. Therefore $z \leq xy$ and since $F$ is upward hereditary, $xy \in F$. Furthermore, since $0 \notin P$, it follows that $0 \notin F$, i.e., $F$ is a proper filter for $B$. $\square$
