---
role: proof
locale: en
of_concept: existence-injective-envelope
source_book: gtm013
source_chapter: "5"
source_section: "18"
---

By (18.6), embed $M$ into an injective module $Q$. Consider the set $\mathcal{E}$ of all submodules $E \leq Q$ such that $M \leq E$ and $M \trianglelefteq E$ (the inclusion is essential). Order $\mathcal{E}$ by inclusion. By Zorn's Lemma (the union of a chain in $\mathcal{E}$ is essential over $M$), there exists a maximal element $E \in \mathcal{E}$.

Suppose $E \oplus E \leq Q$ with $E \cap E = 0$. Consider $h: (E \oplus E)/E \to Q/E$ the natural map. By (5.13), $h$ is monic, so $M \trianglelefteq E = \operatorname{Im} g = h((E \oplus E)/E) \trianglelefteq h(Q/E)$. Therefore $M \trianglelefteq h(Q/E)$ by (5.16), so by maximality of $E$, $h((E \oplus E)/E) = h(Q/E)$. Since $h$ is monic, $Q = E \oplus E$, so $E$ is injective by (18.2). Thus $M \to E$ is an injective envelope. Uniqueness up to isomorphism follows from (18.9).
