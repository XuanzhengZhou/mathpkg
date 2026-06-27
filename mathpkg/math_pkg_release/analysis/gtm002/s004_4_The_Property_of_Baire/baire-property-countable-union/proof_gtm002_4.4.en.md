---
role: proof
locale: en
of_concept: baire-property-countable-union
source_book: gtm002
source_chapter: "4"
source_section: "4. The Property of Baire"
---

Let $A_i = G_i \triangle P_i$ ($i = 1, 2, \ldots$) be any sequence of sets having the property of Baire. Put $G = \bigcup G_i$, $P = \bigcup P_i$, and $A = \bigcup A_i$. Then $G$ is open, $P$ is of first category (as a countable union of first category sets), and

$$G - P \subset A \subset G \cup P.$$

Hence $G \triangle A \subset P$ is of first category, and

$$A = G \triangle (G \triangle A)$$

has the property of Baire. This result, together with Theorem 4.2, shows that the class in question is a $\sigma$-algebra. It is evidently the smallest $\sigma$-algebra that includes all open sets and all sets of first category.
