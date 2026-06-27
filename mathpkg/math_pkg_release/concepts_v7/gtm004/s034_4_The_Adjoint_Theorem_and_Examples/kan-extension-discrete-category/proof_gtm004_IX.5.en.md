---
role: proof
locale: en
of_concept: kan-extension-discrete-category
source_book: gtm004
source_chapter: "IX"
source_section: "5. Kan Extensions"
---

# Proof of Kan Extension Formula for Discrete Categories

**Corollary 5.4.** Let $\mathfrak{U} = \mathfrak{B}_d$ be the discrete category on the objects of $\mathfrak{B}$ and let $I: \mathfrak{B}_d \hookrightarrow \mathfrak{B}$ be the inclusion. Then the Kan extension $\widetilde{I}: [\mathfrak{B}_d, \mathfrak{A}] \rightarrow [\mathfrak{B}, \mathfrak{A}]$ is given by

$$(\widetilde{I}\{A_V\})(V') = \coprod_{V \in \mathfrak{B}} (\widetilde{K}_V A_V)(V') = \coprod_{V \in \mathfrak{B}} \coprod_{v \in \mathfrak{B}(V, V')} (A_V)_v,$$

where $(A_V)_v = A_V$, with the obvious values on morphisms.

**Proof.** This follows immediately from Lemma 5.5 and Proposition 5.3. Let us recall the setup. For each $V \in \mathfrak{B}$, let $K_V: 1 \rightarrow \mathfrak{B}$ be the functor $K_V(1) = V$. Then $[\mathfrak{B}_d, \mathfrak{A}] \cong \prod_{V \in \mathfrak{B}} \mathfrak{A}$, and the Kan extension along the inclusion $I$ decomposes as the coproduct of the Kan extensions along the individual functors $\widetilde{K}_V$.

By Lemma 5.5, the left adjoint to $I^*$ is obtained by taking the coproduct of the left adjoints of the individual functors $K_V^*$. And by Proposition 5.3 (which identifies $\widetilde{K}_V$ for the special case $\mathfrak{U} = 1$), we have the explicit formula

$$(\widetilde{K}_V A_V)(V') = \coprod_{v \in \mathfrak{B}(V, V')} A_V.$$

Combining these facts yields the stated formula. The action on morphisms is induced by composition in $\mathfrak{B}$: a morphism $w: V' \rightarrow V''$ induces a map between the coproducts by composing indices. $\square$
