---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

The Satisfiability Theorem is the model-existence theorem for the predicate calculus $\text{Pred}(V, \mathcal{R})$. It states that every consistent set $A$ of formulas (i.e., $F \notin \text{Ded}(A)$) admits an interpretation in which all formulas of $A$ are true. The proof uses a Henkin-style construction: one inductively adds new individual variables $t_p^{(i)}$ as witnesses for existential formulas $(\exists x)q(x) \in A_i$, building an increasing chain of languages $V_i$ and maximal consistent extensions $A_i$, and taking the union $V^* = \bigcup_i V_i$, $A^* = \bigcup_i A_i$ which satisfies the saturation properties needed to construct the canonical model.
