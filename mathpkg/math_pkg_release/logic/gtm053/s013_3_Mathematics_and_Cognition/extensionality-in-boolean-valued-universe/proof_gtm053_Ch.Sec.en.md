---
role: proof
locale: en
of_concept: extensionality-in-boolean-valued-universe
source_book: gtm053
source_chapter: "III"
source_section: "5"
---

The proof establishes three auxiliary statements (I)-(III) by induction on rank:
(I) $\|X = Y\| \wedge \|Y = Z\| \leqslant \|X = Z\|$ (transitivity of equality);
(II) $\|X = Y\| \wedge \|Z \in X\| \leqslant \|Z \in Y\|$ (substitution for membership);
(III) $\|X \in Y\| \wedge \|Y = Z\| \leqslant \|X \in Z\|$ (substitution in second argument).

These are proved using the recursive definitions from Section 4, considering cases based on whether elements are new or old at each rank. The proposition then follows from (I)-(III) together with the definition of $\|X = Y\|$.
