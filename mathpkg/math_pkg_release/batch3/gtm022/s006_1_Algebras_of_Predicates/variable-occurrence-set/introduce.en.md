---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

The function $V(w)$ collects all individual variables that appear anywhere in the syntactic expression $w \in \tilde{P}(V, \mathcal{R})$, including those that occur bound inside quantifiers. It is defined by induction on the structure of formulas: $F$ contains no variables, atomic formulas contribute their argument variables, implication unions the variable sets of its components, and a universal quantifier $(\forall x)$ adds the quantified variable $x$ to the variable set. This function is essential for the subsequent definition of the congruence relation on $\tilde{P}$.
