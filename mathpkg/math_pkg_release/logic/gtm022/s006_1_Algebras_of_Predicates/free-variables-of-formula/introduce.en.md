---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

The set $\text{var}(w)$ of free variables of a formula $w \in P(V, \mathcal{R})$ consists of those individual variables that occur in $w$ and are not bound by any quantifier. It is defined by first choosing a representative $\tilde{w}$ in $\tilde{P}$ and then computing inductively: $F$ has no variables, atomic formulas contribute all their argument variables, implication takes the union, and a universal quantifier $(\forall x)$ removes the variable $x$ from the free variable set. Exercise 1.9 ensures this definition is independent of the choice of representative.
