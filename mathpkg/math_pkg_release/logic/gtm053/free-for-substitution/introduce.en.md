---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

The "free for" condition is the rule of hygiene for variable substitution in first-order logic. It prevents the accidental capture of free variables during substitution, analogous to the rule in analysis that one may write $\int_1^x f(z) dz$ but not $\int_1^x f(x) dx$. This condition is essential for the validity of the logical axiom of specialization: $\forall x P(x) \Rightarrow P(t)$, which requires that $t$ be free for $x$ in $P$.
