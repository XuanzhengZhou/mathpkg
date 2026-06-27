---
role: proof
locale: en
of_concept: character-values-are-algebraic-integers
source_book: gtm042
source_chapter: "6"
source_section: "6.5"
---

For each $s \in G$, the operator $\rho(s)$ satisfies $\rho(s)^{|G|} = I$, since $G$ is a finite group. Thus every eigenvalue $\lambda$ of $\rho(s)$ satisfies $\lambda^{|G|} = 1$, so $\lambda$ is a root of unity. Each root of unity is an algebraic integer, as it satisfies $x^m - 1 = 0$ for some $m$, a monic polynomial with integer coefficients.

Now $\chi(s) = \text{Tr}(\rho(s))$ is the sum of the eigenvalues of $\rho(s)$ (counted with multiplicity). Since the set of algebraic integers is a ring (closed under addition and multiplication), a sum of algebraic integers is an algebraic integer. Therefore $\chi(s)$ is an algebraic integer.
