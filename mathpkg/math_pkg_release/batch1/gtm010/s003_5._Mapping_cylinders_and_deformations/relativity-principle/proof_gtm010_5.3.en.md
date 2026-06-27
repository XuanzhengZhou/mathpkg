---
role: proof
locale: en
of_concept: relativity-principle
source_book: gtm010
source_chapter: "5"
source_section: "5"
---

Let $f: L \times I \to L$ be the natural projection. Consider the mapping cylinder $M_h$ where $h: K_1 \to K_2$ is a CW isomorphism with $h|L = 1$. By (5.1),

$$M_h \searrow M_{h|L} = (L \times I) \cup (K_2 \times 1),$$

and, $h$ being a CW isomorphism, the same proof can be used to collapse from the other end and get $M_h \searrow (L \times I) \cup (K_1 \times 0)$. Now let $\bar{M}_h$ be gotten from $M_h$ by identifying $(x, t) = x$ if $x \in L$, $0 \leq t \leq 1$. Since $(K_1 - L) \cap (K_2 - L) = \varnothing$, we may assume that $K_1$ and $K_2$ themselves are contained in the two ends of $\bar{M}_h$. Then the collapses of $M_h$ (rel $L \times I$) may be performed in this new context, since $M_h - (L \times I)$ is isomorphic to $\bar{M}_h - L$, to yield $K_1 \nearrow \bar{M}_h \searrow K_2$ rel $L$.

This generalizes to the full relativity principle: if $K_1 \wedge K_2$ rel $L$, then the adjunction spaces satisfy the same formal deformation.
