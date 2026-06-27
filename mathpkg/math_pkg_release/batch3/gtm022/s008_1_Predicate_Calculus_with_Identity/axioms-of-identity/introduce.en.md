---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

The axioms of identity formalise the concept of equality within the first-order predicate calculus $\text{Pred}(V, \mathcal{R})$. They consist of the reflexivity axiom $(\forall x)\mathcal{I}(x,x)$ and a scheme of substitutivity axioms: for every relation symbol $r$ of arity $n$ and every argument position $j \leq n$, the formula $(\forall x_1)\cdots(\forall x_n)(\forall y)(\mathcal{I}(x_j, y) \Rightarrow (r(x_1,\ldots,x_n) \Rightarrow r(x_1,\ldots,x_{j-1},y,x_{j+1},\ldots,x_n)))$ is asserted. Together these axioms ensure that $\mathcal{I}$ behaves as a congruence relation with respect to all relation symbols in $\mathcal{R}$.
