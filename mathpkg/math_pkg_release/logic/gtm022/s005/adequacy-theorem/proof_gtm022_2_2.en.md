---
role: proof
locale: en
of_concept: adequacy-theorem-prop-calculus
source_book: gtm022
source_chapter: "II"
source_section: "§2 Soundness and Adequacy of Prop(X)"
---

**Proof.** Suppose $A \models p$, so that $v(A) \subseteq \{1\}$ implies $v(p) = 1$ for every valuation $v$. If $A \cup \{\sim p\}$ is consistent, it follows from the Satisfiability Theorem that there is a valuation $v$ such that $v(A \cup \{\sim p\}) \subseteq \{1\}$, which is not possible. Hence $F \in \text{Ded}(A \cup \{\sim p\})$, i.e., $A \cup \{\sim p\} \vdash F$. By the Deduction Theorem, $A \vdash \sim p \Rightarrow F$. Since $\vdash (\sim p \Rightarrow F) \Rightarrow p$, we obtain $A \vdash p$.
