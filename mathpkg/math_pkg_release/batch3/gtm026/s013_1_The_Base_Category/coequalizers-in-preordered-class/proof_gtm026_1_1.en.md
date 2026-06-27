---
role: proof
locale: en
of_concept: coequalizers-in-preordered-class
source_book: gtm026
source_chapter: "1"
source_section: "1. The Base Category"
---

In a preordered class $\mathcal{K}$ viewed as a category, for any objects $A, B$ the hom-set $\mathcal{K}(A, B)$ has at most one element. Given $f, g \in \mathcal{K}(A, B)$, we must have $f = g$.

Now $\text{id}_B \circ f = f = g = \text{id}_B \circ g$, so $\text{id}_B$ coequalizes $f$ and $g$.

For the universal property: suppose $q': B \to Q'$ satisfies $q' \circ f = q' \circ g$. Since $f = g$, this condition is automatically satisfied for any $q'$. Take $h = q'$. Then $\text{id}_B \circ h = h = q'$, so $h$ satisfies the required factorization. Uniqueness of $h$ follows because there is at most one morphism $B \to Q'$ in a preordered class.
