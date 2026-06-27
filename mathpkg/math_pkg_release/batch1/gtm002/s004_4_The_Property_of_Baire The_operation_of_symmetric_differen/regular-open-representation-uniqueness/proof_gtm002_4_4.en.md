---
role: proof
locale: en
of_concept: regular-open-representation-uniqueness
source_book: gtm002
source_chapter: "4"
source_section: "4"
---
Suppose $A = G \triangle P = H \triangle Q$ where $G$ and $H$ are regular open and $P, Q$ are of first category. Then
$$G \triangle H = P \triangle Q$$
is of first category. But $G \triangle H$ is open (since the symmetric difference of two open sets is open), and the only open set of first category is the empty set (by the Baire category theorem, a nonempty open set is of second category). Therefore $G \triangle H = \emptyset$, so $G = H$, and consequently $P = Q$.

Moreover, if $G$ is regular open and $A = G \triangle P$, then for any other representation $A = H \triangle Q$ with $H$ open, we have $H \subset \bar{G}$. Since $G$ is regular open, $G = G^{-'-'} = \text{int}(\bar{G})$, so $H \subset \bar{G}$ implies $H \subset G$. Thus in the regular open representation the open set $G$ is maximal.
