---
role: proof
locale: en
of_concept: em-intersection-isomorphism
source_book: gtm026
source_chapter: "2"
source_section: "4"
---

This is a formal consequence of axiom 4.5 (unique $E$-$M$ factorization).

Consider the two factorizations of $f$:
$$
f = f \circ \mathrm{id}_A \quad \text{and} \quad f = \mathrm{id}_B \circ f.
$$

Since $f \in E$ by hypothesis and $\mathrm{id}_A \in M$ (as every isomorphism is in $M$ by 4.4, and $\mathrm{id}_A$ is an isomorphism), the first factorization $f = f \circ \mathrm{id}_A$ is an $E$-$M$ factorization. Similarly, since $f \in M$ by hypothesis and $\mathrm{id}_B \in E$, the second factorization $f = \mathrm{id}_B \circ f$ is also an $E$-$M$ factorization.

By the uniqueness clause of axiom 4.5, there exists an isomorphism $\psi$ such that
$$
f \circ \psi = \mathrm{id}_B \quad \text{and} \quad \psi \circ f = \mathrm{id}_A.
$$
Thus $f$ has a two-sided inverse $\psi$, so $f$ is an isomorphism. The argument is the same as in 2.1.50.
