---
role: proof
locale: en
of_concept: dimension-theorem-basis
source_book: gtm049
source_chapter: "I"
source_section: "1.4"
---

(1) By the Exchange Lemma, if $\{a_1, \ldots, a_r\}$ and $\{b_1, \ldots, b_s\}$ are bases of $V$, then $s \leq r$ and $r \leq s$. Hence $r = s$.

(2) If $\{b_1, \ldots, b_s\}$ is a basis then it is clearly a minimal spanning set and a maximal linearly independent set. Conversely, any minimal spanning set must be linearly independent (otherwise a dependence relation allows removal of one vector while still spanning), hence is a basis. Any maximal linearly independent set must span $V$ (otherwise a vector outside its span could be adjoined while preserving independence), hence is a basis.

(3) Given a linearly independent set $S$, we can extend it stepwise by adjoining vectors not in its span until it becomes a maximal linearly independent set, which by (2) is a basis.
