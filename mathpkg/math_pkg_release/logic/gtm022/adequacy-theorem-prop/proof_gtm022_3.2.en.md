---
role: proof
locale: en
of_concept: adequacy-theorem-prop
source_book: gtm022
source_chapter: "III"
source_section: "2"
---

Suppose $A \models p$. If $A \cup \{\sim p\}$ is consistent, then by the Satisfiability Theorem there is a valuation $v$ with $v(A \cup \{\sim p\}) \subseteq \{1\}$, contradicting $A \models p$. Hence $F \in \operatorname{Ded}(A \cup \{\sim p\})$, i.e., $A \cup \{\sim p\} \vdash F$. By the Deduction Theorem, $A \vdash \sim p \Rightarrow F$. Since $\vdash (\sim p \Rightarrow F) \Rightarrow p$, we obtain $A \vdash p$ by Modus Ponens.
