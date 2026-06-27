---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

The Deduction Lemma (also known as the Deduction Theorem) is a fundamental metatheorem of first-order logic. It states that if a formula $Q$ is deducible from $\mathcal{E}$ augmented with a closed formula $P$, then the implication $P \Rightarrow Q$ is deducible from $\mathcal{E}$ alone.

The lemma requires that $\mathcal{E}$ contains all logical axioms $\text{Ax } L$ and that $P$ is closed (no free variables). The proof proceeds by induction on the length of the deduction of $Q$ from $\mathcal{E} \cup \{P\}$, considering each possible justification for a step in the deduction. The closedness condition on $P$ is needed for the case where generalization (Gen) is applied.
