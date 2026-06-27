---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

A truth valuation $v : P(V, \mathcal{R}) \to \mathbb{Z}_2$ assigns a truth value ($1$ for true, $0$ for false) to each proposition of the predicate calculus relative to an interpretation $(U, \varphi, \psi)$. Atomic formulas are evaluated according to whether the tuple of assigned elements belongs to the interpreted relation. The logical constant $F$ and implication $\Rightarrow$ are interpreted via the $\{F, \Rightarrow\}$-algebra homomorphism property. The universal quantifier is treated by induction on depth: $(\forall x)q(x)$ is true precisely when $q(t)$ is true under every possible interpretation of a fresh variable $t$, using all valuations that agree with the given one up to depth $k-1$.
