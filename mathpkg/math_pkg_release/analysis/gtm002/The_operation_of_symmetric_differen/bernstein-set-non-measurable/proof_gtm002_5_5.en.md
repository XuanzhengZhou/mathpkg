---
role: proof
locale: en
of_concept: bernstein-set-non-measurable
source_book: gtm002
source_chapter: "5"
source_section: "5. Non-Measurable Sets"
---
Let $A$ be any measurable subset of $B$. Any closed set $F$ contained in $A$ must be countable (otherwise $F$ would be an uncountable closed set contained in $B$, contradicting the definition of a Bernstein set). Hence $m(F) = 0$ for every closed subset $F$ of $A$. By the regularity of Lebesgue measure, $m(A) = 0$. The same argument applies to any measurable subset of $B'$. Therefore every measurable subset of $B$ or $B'$ is a nullset. In particular, if $B$ itself were measurable, we would have $m(B) = 0$ and $m(B') = 0$, implying $m(\mathbb{R}) = 0$, a contradiction.

Similarly, let $A$ be a subset of $B$ having the property of Baire. Then $A = G \triangle P$ with $G$ open and $P$ of first category. If $G$ is non-empty, then $G$ contains an uncountable closed set $F$ (e.g., a closed interval). Then $F \cap A$ differs from $F \cap G$ by a set of first category, so $F \cap A$ is not of first category in $F$, contradicting that $F$ is uncountable closed and therefore contains points of $B'$ (which are not in $A$). Hence $G$ must be empty, and $A = P$ is of first category. The same argument applies to subsets of $B'$.
