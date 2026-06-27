---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

A logic $\mathcal{L}$ is defined abstractly as a triple $(P, \mathcal{V}, \text{Proofs})$ where $P$ is a set of propositions, $\mathcal{V}$ is a collection of valuation functions mapping propositions to a truth-value set $W$, and for each subset $A \subseteq P$ there is a specified set of finite sequences called proofs from the assumptions $A$. This abstract framework unifies the semantic side (valuations) and the syntactic side (proofs) of a formal system. The propositional calculus $\text{Prop}(X)$ serves as the canonical example: $P = P(X)$ (the free proposition algebra), $\mathcal{V}$ is the set of all homomorphisms $P(X) \to \mathbb{Z}_2$, and proofs are finite sequences governed by axioms and modus ponens.
