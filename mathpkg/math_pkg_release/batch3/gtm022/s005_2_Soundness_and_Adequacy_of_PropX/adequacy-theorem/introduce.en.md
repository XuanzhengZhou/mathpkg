---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

The Adequacy Theorem (also called the Completeness Theorem for propositional logic) states that semantic consequence implies provability: if a proposition $p$ is a logical consequence of a set of assumptions $A$ (every valuation satisfying $A$ also satisfies $p$), then $p$ is provable from $A$ in the formal system $\text{Prop}(X)$. Together with the Soundness Theorem, this establishes the equivalence of syntactic provability ($\vdash$) and semantic entailment ($\models$). The proof proceeds by contraposition: if $p$ is not provable from $A$, then $A \cup \{\sim p\}$ is consistent and can be extended to a maximal consistent set, which then yields a valuation witnessing $A \not\models p$.
