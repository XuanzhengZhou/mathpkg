---
role: proof
locale: en
of_concept: disjoint-closed-sets-additivity
source_book: gtm002
source_chapter: "3"
source_section: "3. Lebesgue Measure in r-Space"
---

This follows from Lemma 3.4 by induction on $n$. Lemma 3.4 states that if $F_1$ and $F_2$ are disjoint bounded closed sets, then $m^*(F_1 \cup F_2) = m^*(F_1) + m^*(F_2)$. The induction step is straightforward: assuming the result holds for $n-1$ sets, apply Lemma 3.4 to the disjoint bounded closed sets $\bigcup_{i=1}^{n-1} F_i$ and $F_n$.
