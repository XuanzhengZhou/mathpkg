---
role: proof
locale: en
of_concept: fundamental-theorem-of-ring-homomorphisms
source_book: gtm030
source_chapter: "II"
source_section: "9"
---

Let $\eta$ be a homomorphism of $\mathfrak{A}$ into $\mathfrak{A}'$ with kernel $\mathfrak{R}$, and let $\mathfrak{B}$ be an ideal of $\mathfrak{A}$ contained in $\mathfrak{R}$. From group theory, we know that the rule $a + \mathfrak{B} \mapsto a\eta$ defines a homomorphism $\bar{\eta}$ of the additive group of $\mathfrak{A}/\mathfrak{B}$ into the additive group of $\mathfrak{A}'$. To verify that $\bar{\eta}$ respects multiplication:

$$[(a_1 + \mathfrak{B})(a_2 + \mathfrak{B})]\bar{\eta} = (a_1a_2 + \mathfrak{B})\bar{\eta} = (a_1a_2)\eta = (a_1\eta)(a_2\eta) = [(a_1 + \mathfrak{B})\bar{\eta}][(a_2 + \mathfrak{B})\bar{\eta}]$$

Thus $\bar{\eta}$ is a ring homomorphism. Evidently $\eta = \nu\bar{\eta}$ where $\nu$ is the natural homomorphism $a \mapsto a + \mathfrak{B}$ of $\mathfrak{A}$ onto $\mathfrak{A}/\mathfrak{B}$.

We recall that $\bar{\eta}$ is 1-1 if and only if $\mathfrak{B} = \mathfrak{R}$. Thus, taking $\mathfrak{B} = \mathfrak{R}$, we obtain a factorization of $\eta$ as $\nu\bar{\eta}$ where $\nu$ is the natural homomorphism of $\mathfrak{A}$ onto $\mathfrak{A}/\mathfrak{R}$ and $\bar{\eta}$ is the induced isomorphism of $\mathfrak{A}/\mathfrak{R}$ into $\mathfrak{A}'$.
