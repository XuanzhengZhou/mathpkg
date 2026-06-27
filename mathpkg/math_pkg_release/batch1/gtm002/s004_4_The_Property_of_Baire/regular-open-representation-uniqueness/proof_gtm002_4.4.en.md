---
role: proof
locale: en
of_concept: regular-open-representation-uniqueness
source_book: gtm002
source_chapter: "4"
source_section: "4. The Property of Baire"
---

If $A = G \triangle P$ with $G$ open and $P$ of first category, then $G^{-'-'}$ is regular open. Since $G^{-'-'} - G$ is nowhere dense, we have $A = G^{-'-'} \triangle P'$ with $P'$ of first category, establishing existence.

For uniqueness, suppose $A = G \triangle P = H \triangle Q$ with $G$ and $H$ regular open. Then $G \triangle H = P \triangle Q$ is of first category. Since $G \triangle H$ is open (being the symmetric difference of two open sets), it must be empty, for a non-empty open set cannot be of first category. Hence $G \triangle H = \emptyset$, so $G = H$. Consequently $P = Q$.

Alternatively, one can argue that $H \subset \bar{G}$, and therefore $H \subset G^{-'-'} = G$. Symmetrically, $G \subset H$, so $G = H$ and $P = Q$.
