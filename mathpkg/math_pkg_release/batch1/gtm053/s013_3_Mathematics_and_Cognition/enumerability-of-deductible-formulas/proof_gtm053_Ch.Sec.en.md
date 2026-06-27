---
role: proof
locale: en
of_concept: enumerability-of-deductible-formulas
source_book: gtm053
source_chapter: "VII"
source_section: "5"
---

Let $a: \mathbb{Z}^+ \to S(A)$ be a recursive function with image $\mathrm{Ax}$, and let $\mathrm{inf}: \mathbb{Z}^+ \to S(A)$ be the partial recursive function encoding the rules of deduction. Construct $d: \mathbb{Z}^+ \to S(A)$ by $d(2n-1) = a(n)$, $d(2n) = \mathrm{inf}(n)$. Then $D$, the closure of the image of $d$ under the rules of deduction, is the image of a recursive function obtained by dovetailing all possible deduction sequences.
