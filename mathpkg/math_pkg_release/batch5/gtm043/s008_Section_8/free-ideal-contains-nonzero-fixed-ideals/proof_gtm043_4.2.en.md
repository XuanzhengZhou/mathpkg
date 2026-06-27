---
role: proof
locale: en
of_concept: free-ideal-contains-nonzero-fixed-ideals
source_book: gtm043
source_chapter: "4"
source_section: "4.2"
---

Since $I$ is free, it is nonzero; hence $I$ contains a nonzero function $f$.

**Case 1:** $Z(f) \neq \emptyset$. Then $h = f$ is a nonzero element of $I$ with nonempty zero-set, and by the proposition on principal ideals, $(h)$ is a nonzero fixed ideal contained in $I$.

**Case 2:** $Z(f) = \emptyset$. Since $f$ is nonvanishing, it attains some value $r \neq 0$ (if $X$ is nonempty; otherwise the statement is vacuous). Define $h = f \cdot (f - r)$. Then $h \in I$ because $I$ is an ideal and $f \in I$. Moreover $h$ is nonzero since $f$ is nonvanishing and $f - r$ is not identically zero (it vanishes precisely on $Z(f-r) \neq \emptyset$ because $f$ assumes $r$). The zero-set $Z(h) = Z(f) \cup Z(f-r) = Z(f-r) \neq \emptyset$, so $h$ is a nonzero element of $I$ with nonempty zero-set. Hence $(h)$ is a nonzero fixed ideal contained in $I$.

In both cases, $I$ contains a nonzero fixed ideal. The argument works identically in $C(X)$ and $C^*(X)$.
