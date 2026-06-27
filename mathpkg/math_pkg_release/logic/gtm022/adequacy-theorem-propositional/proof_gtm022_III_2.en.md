---
role: proof
locale: en
of_concept: "adequacy-theorem-propositional"
source_book: gtm022
source_chapter: "III"
source_section: "2"
---
Proof. Suppose $A \models p$, so that $v(A) \subseteq \{1\}$ implies $v(p) = 1$ for every valuation $v$. If $A \cup \{\sim p\}$ is consistent, it follows from the Satisfiability Theorem that there is a valuation $v$ such that $v(A \cup \{\sim p\}) \subseteq \{1\}$, which contradicts $A \models p$ since $v(\sim p) = 1$ means $v(p) = 0$. Hence $F \in \operatorname{Ded}(A \cup \{\sim p\})$, i.e., $A \cup \{\sim p\} \vdash F$. By the Deduction Theorem, $A \vdash \sim p \Rightarrow F = \sim\sim p$. Since $\vdash \sim\sim p \Rightarrow p$ (axiom $\mathcal{A}_3$), we have $A \vdash p$. $\square$
