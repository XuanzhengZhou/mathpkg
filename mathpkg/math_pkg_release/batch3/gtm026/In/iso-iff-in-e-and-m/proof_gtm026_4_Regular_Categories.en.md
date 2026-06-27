---
role: proof
locale: en
of_concept: iso-iff-in-e-and-m
source_book: gtm026
source_chapter: "4"
source_section: "Regular Categories"
---

This is a formal consequence of the uniqueness clause in axiom (4.5). Factor $f$ in two ways:

First, write $f = f \cdot \mathrm{id}_B$. Since $f \in M$ and $\mathrm{id}_B \in M$ (every isomorphism is in $M$ by (4.4)), and also $f \in E$ and $\mathrm{id}_B \in E$, this is an $E$-$M$ factorization.

Second, write $f = \mathrm{id}_A \cdot f$. Here $\mathrm{id}_A \in E$ (by (4.4)) and $f \in M$, so this is also an $E$-$M$ factorization.

By the uniqueness clause of (4.5), there exists an isomorphism $\psi$ such that $f \cdot \psi = \mathrm{id}_A$ and $\psi \cdot f = \mathrm{id}_B$. Thus $f$ has a two-sided inverse $\psi$ and is therefore an isomorphism. (This is the same argument used in 2.1.50.)
