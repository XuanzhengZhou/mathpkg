---
role: proof
locale: en
of_concept: satisfiability-theorem-pred
source_book: gtm022
source_chapter: "IV"
source_section: "4"
---

Construct inductively $V^* = \bigcup_i V_i$ and $A^* = \bigcup_i A_i$ where $V_{i+1}$ adds new variables $t_p^{(i)}$ for each existential formula $(\exists x)q(x) \in A_i$, and $A_{i+1}$ adds $q(t_p^{(i)})$. The resulting $A^*$ is maximal consistent and has witnesses for all existential formulas. Then build a model with universe $V^*$ modulo the relation $x \sim y$ iff $\mathcal{I}(x, y) \in A^*$, and interpret relation symbols according to membership in $A^*$.
