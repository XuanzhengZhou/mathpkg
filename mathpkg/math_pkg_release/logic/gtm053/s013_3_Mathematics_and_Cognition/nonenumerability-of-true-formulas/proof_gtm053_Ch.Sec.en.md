---
role: proof
locale: en
of_concept: nonenumerability-of-true-formulas
source_book: gtm053
source_chapter: "VII"
source_section: "3"
---

(a) The formula $\neg P(x)$ is $R_1 * \cdots * R_{S+1}$ where $x$ does not occur in the $R_i$. Substituting the numeral $\bar{n}$ produces a formula whose Godel number is a recursive function of $n$, because juxtaposition and $n \mapsto \bar{n}$ are recursive.
(b) If the set were enumerable, its preimage under the recursive function in (a) would be enumerable. But this preimage is the complement of $E$ (since $\neg P(\bar{n})$ is true iff $n \notin E$), which is not enumerable because $E$ is undecidable.
