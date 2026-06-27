---
role: proof
locale: en
of_concept: indecomposable-decomposition-complements-summands
source_book: gtm013
source_chapter: "7"
source_section: "25. Injective Modules and Noetherian Rings—The Faith–Walker Theorems"
---

By the above lemma an indecomposable decomposition of an injective module $E = \bigoplus_A E_\alpha$ satisfies the hypothesis of Azumaya's Theorem (12.6). Let $K$ be a direct summand of $E$ and choose a subset $B \subseteq A$ maximal with respect to

$$(\bigoplus_B E_\beta) \cap K = 0.$$

Then the submodule $(\bigoplus_B E_\beta) + K = (\bigoplus_B E_\beta) \oplus K$ is injective (18.2); thus for some $E' \leq E$,

$$E = E' \oplus (\bigoplus_B E_\beta) \oplus K.$$

We claim that $E' = 0$. For if $E' \neq 0$, then by (12.6) $E'$ contains an indecomposable direct summand and there is a $\gamma \in A$ and a direct summand $E''$ of $E'$ such that

$$E = E_\gamma \oplus (E'' \oplus (\bigoplus_B E_\beta) \oplus K)$$

contrary to the maximality of $B$. Thus $E = (\bigoplus_B E_\beta) \oplus K$, and the given decomposition complements direct summands.
