---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

This lemma shows that any consistent set of formulas can be extended to one where the alphabet is sufficient for Henkin-style model construction. The idea is to add new constant symbols $c_P$ for each existential-type formula $\neg \forall x P(x)$ and add the corresponding Henkin axioms $R_P: \neg \forall x P(x) \Rightarrow \neg P(c_P)$. The construction must be done carefully to avoid inconsistency: one shows that adding all the logical axioms of the extended language $L'$ together with the $R$-formulas preserves consistency. A rank assignment on the new constants ensures well-foundedness. This lemma, together with Lemma 6.6 (completion) and Lemma 6.5 (fundamental lemma), forms the three pillars of the proof of Gödel's Completeness Theorem.
