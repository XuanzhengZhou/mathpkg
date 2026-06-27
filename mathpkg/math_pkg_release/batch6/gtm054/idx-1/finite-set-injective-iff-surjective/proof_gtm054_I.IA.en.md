---
role: proof
locale: en
of_concept: finite-set-injective-iff-surjective
source_book: gtm054
source_chapter: "I"
source_section: "IA"
---
**Proof.** Let $ be a finite set with $|X| = n$. If $ is injective, then $|h[X]| = |X| = n$. Since [X] \subseteq X$ and $ is finite, [X] = X$, so $ is surjective.

Conversely, if $ is surjective, suppose $ is not injective. Then there exist distinct , x_2 \in X$ with (x_1) = h(x_2)$. But then $|h[X]| \leq n-1 < n$, contradicting surjectivity. Hence $ is injective.
