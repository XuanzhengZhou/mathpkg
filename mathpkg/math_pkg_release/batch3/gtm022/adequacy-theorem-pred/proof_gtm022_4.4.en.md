---
role: proof
locale: en
of_concept: adequacy-theorem-pred
source_book: gtm022
source_chapter: "IV"
source_section: "4"
---

If $A \models p$, then $A \cup \{\sim p\}$ has no model, so is inconsistent by the Satisfiability Theorem. Thus $A \cup \{\sim p\} \vdash F$. By the Deduction Theorem, $A \vdash \sim p \Rightarrow F$, and $A \vdash p$ follows using the propositional tautology $(\sim p \Rightarrow F) \Rightarrow p$.
