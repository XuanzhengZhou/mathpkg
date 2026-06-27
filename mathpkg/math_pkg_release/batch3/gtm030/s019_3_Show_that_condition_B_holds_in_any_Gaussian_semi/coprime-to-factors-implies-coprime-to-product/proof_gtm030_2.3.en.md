---
role: proof
locale: en
of_concept: coprime-to-factors-implies-coprime-to-product
source_book: gtm030
source_chapter: "2"
source_section: "3"
---

By Lemma 3, $(a, b) \sim 1$ implies $(ac, bc) \sim c \cdot (a, b) \sim c$. Now assume $(a, c) \sim 1$. Then
$$1 \sim (a, c) \sim (a, (ac, bc)).$$
By Lemma 2 (associativity),
$$(a, (ac, bc)) \sim ((a, ac), bc).$$
Since $a \mid ac$, we have $(a, ac) \sim a$, so $((a, ac), bc) \sim (a, bc)$. Chaining the equivalences together gives $(a, bc) \sim 1$, as required.
