---
role: proof
locale: en
of_concept: con-is-closure
source_book: gtm022
source_chapter: "II"
source_section: "3"
---

All three properties follow directly from the definition of $\operatorname{Con}(A)$. For (i), if $p \in A$, then any valuation making all of $A$ true makes $p$ true. For (ii), any valuation making all of $A_2$ true also makes all of $A_1$ true. For (iii), if $p \in \operatorname{Con}(\operatorname{Con}(A))$, then $v(p) = 1$ whenever $v(\operatorname{Con}(A)) \subseteq \{1\}$. But $v(A) \subseteq \{1\}$ implies $v(\operatorname{Con}(A)) \subseteq \{1\}$ by definition, so $v(p) = 1$, giving $\operatorname{Con}(\operatorname{Con}(A)) \subseteq \operatorname{Con}(A)$. The reverse inclusion follows from (i).
