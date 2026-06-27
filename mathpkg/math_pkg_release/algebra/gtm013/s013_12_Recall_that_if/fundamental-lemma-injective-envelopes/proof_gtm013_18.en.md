---
role: proof
locale: en
of_concept: fundamental-lemma-injective-envelopes
source_book: gtm013
source_chapter: "5"
source_section: "18"
---

Since $E$ is injective, the monomorphism $q: M \to Q$ lifts along the essential monomorphism $i: M \to E$ to a homomorphism $g: Q \to E$ such that $g q = i$. Since $i$ is essential and $g q = i$, $\operatorname{Ker} g \cap \operatorname{Im} q = 0$; but since $\operatorname{Im} q \leq^{\text{ess}} Q$ (because $q$ is a monomorphism into an injective module and $i$ is essential), we must have $\operatorname{Ker} g = 0$, so $g$ is monic. Since $E$ is injective, the monomorphism $g$ splits: $Q = \operatorname{Im} g \oplus E$ with $\operatorname{Im} g \cong E$. Now $E = \operatorname{Im} g \cong E$ and $\operatorname{Im} q \leq \operatorname{Im} g = E$. Since $q$ is essential (because $i = g q$ is essential and $g$ is monic), $q: M \to E$ is an injective envelope.

For uniqueness: given $\bar{f} i_1 = i_2 f$, since $i_1$ is essential and $i_2$ is monic, $\bar{f}$ is monic. Since $E_1$ is injective, $\operatorname{Im} \bar{f}$ is a direct summand of $E_2$. But $i_2$ is essential, so $\operatorname{Im} \bar{f} = E_2$, hence $\bar{f}$ is an isomorphism.
