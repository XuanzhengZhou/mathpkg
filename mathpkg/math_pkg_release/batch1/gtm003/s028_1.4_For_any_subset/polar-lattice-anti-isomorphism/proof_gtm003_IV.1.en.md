---
role: proof
locale: en
of_concept: polar-lattice-anti-isomorphism
source_book: gtm003
source_chapter: "IV"
source_section: "1.5"
---

From the corollary of the bipolar theorem, $M = M^{\circ\circ}$ holds precisely for the $\sigma(F, G)$-closed subspaces of $F$, and similarly $N = N^{\circ\circ}$ for the $\sigma(G, F)$-closed subspaces of $G$. Hence the polar map $M \mapsto M^\circ$ is a bijection between these two families.

It is immediate from (1.5) and its corollaries that the polar map reverses inclusions: if $M_1 \subset M_2$, then $M_2^\circ \subset M_1^\circ$. For the lattice operations, we verify:

For any two weakly closed subspaces $M_1, M_2 \subset F$, we have $\inf(M_1, M_2) = M_1 \cap M_2$. Its polar is $(M_1 \cap M_2)^\circ$. Since $M_1 \cap M_2 \subset M_i$, we have $M_i^\circ \subset (M_1 \cap M_2)^\circ$, so $\sup(M_1^\circ, M_2^\circ) = (M_1^\circ + M_2^\circ)^- \subset (M_1 \cap M_2)^\circ$. Conversely, any $y \in (M_1 \cap M_2)^\circ$ satisfies $\operatorname{Re}\langle x, y \rangle \leq 1$ for all $x \in M_1 \cap M_2$; a standard argument using the bipolar theorem shows that $y$ belongs to the $\sigma(G, F)$-closed sum $M_1^\circ + M_2^\circ$ taken with its closure, giving the reverse inclusion. Thus $(\inf(M_1, M_2))^\circ = \sup(M_1^\circ, M_2^\circ)$. The dual relation $(\sup(M_1, M_2))^\circ = \inf(M_1^\circ, M_2^\circ)$ follows by symmetry, applying the first relation to the closed subspaces $M_1^\circ, M_2^\circ \subset G$ and taking polars.
