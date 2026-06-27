---
role: proof
locale: en
of_concept: "henkin-witness-lemma"
source_book: gtm022
source_chapter: "IV"
source_section: "4"
---
Proof. If $A \cup \{q(t)\} \vdash F$, then by the Deduction Theorem $A \vdash q(t) \Rightarrow F = \sim q(t)$. By Generalisation (since $t$ not in $A$), $A \vdash (\forall t)\sim q(t) = \sim(\exists t)q(t)$. But $p = (\exists x)q(x) \in A$, so $A$ would prove both $(\exists t)q(t)$ and its negation, contradicting consistency. $\square$
