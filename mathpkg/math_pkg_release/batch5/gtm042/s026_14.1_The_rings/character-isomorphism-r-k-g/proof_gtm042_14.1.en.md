---
role: proof
locale: en
of_concept: character-isomorphism-r-k-g
source_book: gtm042
source_chapter: "14"
source_section: "14.1"
---

Since $K$ has characteristic zero, the character $\chi_E$ of a $K[G]$-module $E$ is already defined; it is an additive function of $E$ (characters are additive with respect to direct sums).

By linearity, we obtain a linear map $x \mapsto \chi_x$ from $R_K(G)$ into the ring of class functions of $G$.

This map is in fact an isomorphism of $R_K(G)$ onto the group of virtual characters of $G$ over $K$. The injectivity follows from the fact that characters determine representations in characteristic zero: if $\chi_x = 0$ as a class function, then $x$ must be zero in $R_K(G)$ because the irreducible characters are linearly independent and form a basis of the space of class functions. The surjectivity onto virtual characters holds because every virtual character is by definition an integer linear combination of irreducible characters, each of which comes from an irreducible $K[G]$-module.

We often identify $R_K(G)$ with the group of virtual characters (this explains the notation used in 12.1).

In contrast to the case of $R_K(G)$, if $E$ and $E'$ are two $K[G]$-modules such that $[E] = [E']$ in $R_K(G)$, then $E$ and $E'$ are isomorphic: this follows from the fact that $E$ and $E'$ are semisimple in characteristic zero. The analogous result is not true for $k[G]$-modules if $p$ divides the order of $G$, because of the existence of modules which are not semisimple.
