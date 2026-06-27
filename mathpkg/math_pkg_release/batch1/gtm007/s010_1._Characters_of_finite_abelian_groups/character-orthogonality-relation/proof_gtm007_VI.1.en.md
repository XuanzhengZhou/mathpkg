---
role: proof
locale: en
of_concept: character-orthogonality-relation
source_book: gtm007
source_chapter: "VI"
source_section: "§1. Characters of finite abelian groups"
---

For the first identity: if $\chi = 1$, every term is $1$, so the sum is $|G|$. If $\chi \neq 1$, choose $y \in G$ with $\chi(y) \neq 1$. Then
$$
\chi(y) \sum_{x \in G} \chi(x) = \sum_{x \in G} \chi(yx) = \sum_{x \in G} \chi(x)
$$
since multiplication by $y$ permutes $G$. Hence $(1-\chi(y))\sum_x \chi(x) = 0$, so $\sum_x \chi(x) = 0$.

The second identity follows by applying the first to the dual group $\hat{G}$ and using the bidual isomorphism (Proposition 3).
