---
role: proof
locale: en
of_concept: completeness-from-models
source_book: gtm022
source_chapter: "V"
source_section: "3"
---

\textbf{Proof.} Since $\mathcal{T}$ is consistent, it has a model $M$ say. Put $A' = \{p \in \mathcal{L}(\mathcal{T}) \mid p \text{ is true in } M\}$. Then $A'$ has the required properties. Indeed, $A' \supseteq A$ because every axiom is true in $M$. The theory $(\mathcal{R}, A', C)$ is consistent because it has a model (namely $M$), and it is complete because for every $p \in \mathcal{L}(\mathcal{T})$, either $p$ is true in $M$ (so $p \in A'$) or $\sim p$ is true in $M$ (so $\sim p \in A'$), hence every sentence is decided.
