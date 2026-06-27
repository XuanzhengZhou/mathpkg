---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

The Deduction Theorem for propositional logic states that if a proposition $q$ is provable from a set of assumptions augmented by $p$ (i.e., $A \cup \{p\} \vdash q$), then the implication $p \Rightarrow q$ is provable from $A$ alone ($A \vdash p \Rightarrow q$). This fundamental result allows one to "discharge" hypotheses, converting them into antecedents of implications. The proof proceeds by induction on the length of the proof of $q$ from $A \cup \{p\}$, explicitly constructing a proof of $p \Rightarrow q$ from $A$ using the axiom schemas of the propositional calculus.
