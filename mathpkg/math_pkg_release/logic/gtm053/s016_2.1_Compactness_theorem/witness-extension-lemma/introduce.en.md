---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

This lemma extends a finitely satisfiable set of sentences $E$ to a complete set with Henkin witnesses by iteratively adding new constant symbols $c_Q$ for each one-variable formula $Q(v)$, along with the Henkin axiom $\exists v\,Q(v) \to Q(c_Q)$. The construction proceeds through $\omega$ stages: $L_0 = L$, $\mathcal{E}_0$ is a Lindenbaum completion of $E$, and at each stage $L_{i+1}$ adds constants for all $L_i$-formulas. The union $\tilde{L} = \bigcup_i L_i$ has cardinality $|L| + \aleph_0$, and a final Lindenbaum application yields the complete set $\tilde{\mathcal{E}}$ with witnesses. This is the core of Henkin's method for proving completeness and compactness.
