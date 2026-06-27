---
role: proof
locale: en
of_concept: factorization-of-ring-homomorphism
source_book: gtm030
source_chapter: "2"
source_section: "9"
---

We already know from group theory that the rule $a + \mathfrak{B} \mapsto a\eta$ defines a homomorphism $\bar{\eta}$ of the additive group of $\bar{\mathfrak{A}} = \mathfrak{A}/\mathfrak{B}$ into the additive group of $\mathfrak{A}'$. It remains to verify that $\bar{\eta}$ preserves multiplication:

$$[(a_1 + \mathfrak{B})(a_2 + \mathfrak{B})]\bar{\eta} = (a_1 a_2 + \mathfrak{B})\bar{\eta} = (a_1 a_2)\eta = (a_1\eta)(a_2\eta) = [(a_1 + \mathfrak{B})\bar{\eta}][(a_2 + \mathfrak{B})\bar{\eta}].$$

Thus $\bar{\eta}$ is a ring homomorphism. Evidently $\eta = \nu\bar{\eta}$. From the corresponding group-theoretic result, $\bar{\eta}$ is 1-1 if and only if $\mathfrak{B} = \mathfrak{R}$. When $\mathfrak{B} = \mathfrak{R}$, the induced map $\bar{\eta}$ is an isomorphism of $\mathfrak{A}/\mathfrak{R}$ into $\mathfrak{A}'$.
