---
role: proof
locale: en
of_concept: fundamental-theorem-of-ring-homomorphisms
source_book: gtm030
source_chapter: "2"
source_section: "9. Homomorphism of rings"
---

We know from group theory that the rule $$a + \mathfrak{B} \mapsto a\eta$$ defines a homomorphism $$\bar{\eta}$$ of the additive group of $$\mathfrak{A}/\mathfrak{B}$$ into the additive group of $$\mathfrak{A}'$$. To verify that $$\bar{\eta}$$ is a ring homomorphism, we check compatibility with multiplication:

$$
\begin{aligned}
[(a_1 + \mathfrak{B})(a_2 + \mathfrak{B})]\bar{\eta}
&= (a_1 a_2 + \mathfrak{B})\bar{\eta} \\
&= (a_1 a_2)\eta \\
&= (a_1\eta)(a_2\eta) \\
&= [(a_1 + \mathfrak{B})\bar{\eta}][(a_2 + \mathfrak{B})\bar{\eta}].
\end{aligned}
$$

Thus $$\bar{\eta}$$ preserves multiplication and is a ring homomorphism. Evidently $$\eta = \nu \bar{\eta}$$ where $$\nu: a \mapsto a + \mathfrak{B}$$ is the natural homomorphism.

From group theory, we recall that $$\bar{\eta}$$ is 1-1 if and only if its kernel is trivial, which happens precisely when $$\mathfrak{B} = \mathfrak{K}$$ (the kernel of $$\eta$$). Taking $$\mathfrak{B} = \mathfrak{K}$$ yields the factorization of $$\eta$$ as the natural homomorphism $$\nu$$ onto $$\mathfrak{A}/\mathfrak{K}$$ followed by the induced isomorphism $$\bar{\eta}$$ of $$\mathfrak{A}/\mathfrak{K}$$ into $$\mathfrak{A}'$$.
