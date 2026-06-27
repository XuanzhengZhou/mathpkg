---
role: proof
locale: en
of_concept: algebraic-subcategory-infima-closed
source_book: gtm026
source_chapter: "3"
source_section: "3.13"
---

If $A$ is algebraic over $K$, then $A \cong K^T$ for a closure operator $T$. The closed elements are precisely those $x$ with $x^{-} \leqslant x$, and these are closed under infima: if $\{x_i\} \subseteq A$, then $(\inf x_i)^{-} = \inf x_i^{-} = \inf x_i$ because $T$ is order-preserving and each $x_i$ is closed. Conversely, if $A$ is closed under infima, define $x^{-} = \inf\{y \in A : x \leqslant y\}$. This is well-defined because $K$ is complete (the empty infimum $1$ ensures the set is nonempty). Then $x \leqslant x^{-}$ is clear, and $x^{--} = x^{-}$ follows because $x^{-} \in A$ (closed under infima) so the infimum defining $x^{--}$ is achieved at $x^{-}$. The closed elements are precisely $A$, establishing $A \cong K^T$.
