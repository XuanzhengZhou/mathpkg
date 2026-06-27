---
role: proof
locale: en
of_concept: regular-cardinal-subtheory
source_book: gtm026
source_chapter: "5"
source_section: "5.16"
---

To deal with $M$-complete semilattices it seems natural to "truncate" $\mathbf{T}$ at $M$ by defining $XT_M = \{A \subset X : A \text{ has cardinal} < M\}$. Is $T_M$ a subtheory of $\mathbf{T}$ in the sense of 3.20? Since every singleton subset is in $XT_M$ the condition on $\eta$ is true. There is a problem, however, with staying closed under composition. Given $\alpha: A \longrightarrow BT$ and $\beta: B \longrightarrow CT$ then $(\alpha \circ \beta)_a = \cup\{b\beta : b \in a\alpha\}$. If $\alpha$ factors through $BT_M$ (i.e., $a\alpha$ has cardinal $< M$) and $\beta$ factors through $CT_M$ (i.e., each $b\beta$ has cardinal $< M$) we would hope that $(\alpha \circ \beta)_a$ also has cardinal $< M$. A moment's thought shows that this condition amounts to a rewording of the definition of a regular cardinal.

Thus $M$ is a regular cardinal if and only if $T_M$ is a subtheory of $\mathbf{T}$.
