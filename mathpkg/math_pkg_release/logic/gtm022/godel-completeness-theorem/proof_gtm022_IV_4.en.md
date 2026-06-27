---
role: proof
locale: en
of_concept: "godel-completeness-theorem"
source_book: gtm022
source_chapter: "IV"
source_section: "4"
---
Proof. Soundness (Theorem 4.4): $A \vdash p \Rightarrow A \models p$.

Adequacy: Suppose $A \models p$. If $A \cup \{\sim p\}$ were consistent, the Satisfiability Theorem would give an interpretation with $v(A \cup \{\sim p\}) \subseteq \{1\}$, contradicting $A \models p$. Hence $F \in \operatorname{Ded}(A \cup \{\sim p\})$, i.e., $A \cup \{\sim p\} \vdash F$. By the Deduction Theorem, $A \vdash \sim p \Rightarrow F = \sim\sim p$. Since $\vdash \sim\sim p \Rightarrow p$, we have $A \vdash p$. $\square$
