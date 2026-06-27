---
role: proof
locale: en
of_concept: product-measurable-functions
source_book: gtm025
source_chapter: "3"
source_section: "11"
---

**Proof.** For $a > 0$, let $A_\beta = A$ if $a < \beta$, $\emptyset$ otherwise. Then
$$h^{-1}(]a, \infty[) = A_\beta \cup \{f = \infty, g > 0\} \cup \{f > 0, g = \infty\}$$
$$\cup \bigcup_{r > 0, r \in \mathbb{Q}} (\{f > r\} \cap \{g > a/r\}) \cup \bigcup_{r < 0, r \in \mathbb{Q}} (\{f < r\} \cap \{g < a/r\}).$$
All terms are in $\mathcal{A}$. Similar decompositions for $a \leq 0$. $\square$
