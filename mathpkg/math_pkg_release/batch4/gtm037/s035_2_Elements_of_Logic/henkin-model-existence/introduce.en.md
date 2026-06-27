---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

This theorem is the heart of Henkin's proof of the completeness theorem for first-order logic. It constructs a model directly from syntactic material: the universe consists of equivalence classes of variable-free terms under the equivalence relation $\sigma \equiv \tau$ iff $\Gamma \vdash \sigma = \tau$. Operations are defined by applying the corresponding function symbols to representatives, and relations hold exactly when the atomic formula is provable from $\Gamma$. The completeness and richness of $\Gamma$ ensure that every sentence's truth in this term model coincides with its provability from $\Gamma$. The cardinality bound follows because the universe is a quotient of the set of closed terms.
