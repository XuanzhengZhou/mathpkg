---
role: proof
locale: en
of_concept: theorem-b-composition-measurability
source_book: gtm018
source_chapter: "VIII"
source_section: "39. Measurable Transformations"
---
For any measurable set $M$ (not containing $0$ without loss of generality):
$$N(gT) \cap (gT)^{-1}(M) = \{x: (gT)(x) \in M - \{0\}\} = T^{-1}(\{y: g(y) \in M - \{0\}\}) = T^{-1}(N(g) \cap g^{-1}(M)).$$
Since $g$ is measurable, $N(g) \cap g^{-1}(M) \in \mathbf{T}$. By measurability of $T$, $T^{-1}(N(g) \cap g^{-1}(M)) \in \mathbf{S}$, so $gT$ is measurable with respect to $T^{-1}(\mathbf{T})$.
