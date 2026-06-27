---
role: proof
locale: en
of_concept: theoremhood-solubility-via-model
source_book: gtm022
source_chapter: "5"
source_section: "5"
---

Suppose $p$ is a theorem of $\mathcal{T}$. Then by the previous propositions, since $\mathcal{T}$ is effectively axiomatised, a Turing machine can enumerate proofs and find a proof of $p$.

Suppose now that $p$ is not a theorem of $\mathcal{T}$. Consider the theory $\mathcal{T}' = (\mathcal{R}, A \cup \{\sim p\}, C)$. Since $p$ is not a theorem of $\mathcal{T}$, $\mathcal{T}'$ is consistent. By the Gödel—Henkin completeness theorem, any consistent first-order theory has a model. Therefore $\mathcal{T}'$ has a model. The construction of a model of $\mathcal{T}'$ would clearly show that $p$ is not a theorem of $\mathcal{T}$, for in such a model $\sim p$ holds (by virtue of being an axiom), hence $p$ is false in that model and therefore cannot be provable in $\mathcal{T}$.

Thus, for any effectively axiomatised theory $\mathcal{T}$ and any $p \in \mathcal{L}(\mathcal{T})$, the problem of deciding whether $p$ is a theorem is soluble: find a proof of $p$ if $p$ is a theorem, or a model of $\mathcal{T}$ in which $p$ is false if $p$ is not a theorem.
