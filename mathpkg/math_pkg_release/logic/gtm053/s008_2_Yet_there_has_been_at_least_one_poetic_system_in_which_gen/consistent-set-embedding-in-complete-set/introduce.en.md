---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

This is a Lindenbaum-type lemma: any consistent set of formulas containing the logical axioms can be extended to a consistent and complete set. Completeness here means that for every closed formula $P$, either $P \in \mathcal{E}'$ or $\neg P \in \mathcal{E}'$. The proof proceeds by enumerating all closed formulas and deciding at each step whether to add the formula or its negation, preserving consistency. This lemma is an essential building block in the proof of Gödel's Completeness Theorem: to construct a model for a consistent set $\mathcal{E}$, one first extends it to a complete set, then ensures the alphabet is sufficient, and finally builds a term model.
