---
role: proof
locale: en
of_concept: baire-property-closed-representation
source_book: gtm002
source_chapter: "4"
source_section: "4. The Property of Baire"
---

If $A = G \triangle P$, with $G$ open and $P$ of first category, then $N = \bar{G} - G$ is a nowhere dense closed set, and $Q = N \triangle P$ is of first category. Let $F = \bar{G}$. Then

$$A = G \triangle P = (\bar{G} \triangle N) \triangle P = \bar{G} \triangle (N \triangle P) = F \triangle Q.$$

Conversely, if $A = F \triangle Q$, where $F$ is closed and $Q$ is of first category, let $G$ be the interior of $F$. Then $N = F - G$ is nowhere dense, $P = N \triangle Q$ is of first category, and

$$A = F \triangle Q = (G \triangle N) \triangle Q = G \triangle (N \triangle Q) = G \triangle P,$$

which exhibits $A$ as the symmetric difference of an open set and a set of first category.
