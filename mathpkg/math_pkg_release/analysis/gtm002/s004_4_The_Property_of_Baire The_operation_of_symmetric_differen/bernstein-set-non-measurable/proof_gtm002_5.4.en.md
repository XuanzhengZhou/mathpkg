---
role: proof
locale: en
of_concept: bernstein-set-non-measurable
source_book: gtm002
source_chapter: "5"
source_section: "Non-Measurable Sets"
---

**Proof.** Let $A$ be any measurable subset of $B$. Any closed set $F$ contained in $A$ must be countable, for if $F$ were uncountable, then $F$ would be an uncountable closed set, and by definition of a Bernstein set, $B'$ would intersect $F$. But $F \subset A \subset B$, so $B' \cap F = \emptyset$ unless $F$ is empty or countable. Hence $m(F) = 0$ for every closed $F \subset A$, and therefore $m(A) = 0$. Thus every measurable subset of $B$ is a nullset. By complementation, the same holds for $B'$. In particular, $B$ itself cannot be measurable unless it is a nullset, but then $B'$ would have full measure, contradicting that every measurable subset of $B'$ is also a nullset.

Similarly, if $A$ is a subset of $B$ having the property of Baire, then $A = G \triangle P$ where $G$ is open and $P$ is of first category. If $G$ is non-empty, then $G$ contains an uncountable closed set (in fact, a perfect set), which must intersect $B'$. This contradicts $G \cap B' \subset P$ being of first category (since any non-empty open set is of second category). Hence $G = \emptyset$ and $A$ is of first category. The same argument applies to $B'$. $\square$
