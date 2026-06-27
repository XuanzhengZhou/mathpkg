---
role: proof
locale: en
of_concept: canonical-maps-in-monoidal-category
source_book: gtm005
source_chapter: "VII"
source_section: "2. Coherence"
---

**Proof.** This corollary is a direct consequence of the coherence theorem (Theorem 1). The coherence theorem establishes that any two paths between words $v$ and $w$ of the same length in the graph $G_n'$ yield equal arrows in $B$. Therefore, for each pair $(v, w)$, there is at most one isomorphism $v_B \Rightarrow w_B$ obtainable by composing instances of $\alpha$, $\lambda$, $\varrho$ and their inverses.

The existence of such an isomorphism for any pair of words of equal length follows from the fact that every word can be reduced to a canonical right-associated form by applying associativity and unit transformations. Specifically, define a canonical map from $v$ to $w$ by composing: a reduction path from $v$ to the right-associated form $w^{(n)}$ (using $\alpha$), followed by the inverse of a reduction path from $w$ to $w^{(n)}$. The coherence theorem guarantees that this composition is independent of the choice of reduction paths.

The closure properties follow by construction: composing two canonical maps gives a map between the appropriate words, and the $\square$-product of canonical maps is obtained by boxing them with identities, which preserves the canonical nature by the inductive definition of basic arrows. $\square$
