---
role: proof
locale: en
of_concept: theorem-4-28-ostrom-desargues-configuration
source_book: gtm006
source_chapter: IV
source_section: '7'
content_hash: 49e9888a888e
written_against: ae08cec6f26b
---

Let the order of $\mathcal{P}$ be $n$. Assume $n \geq 5$ (planes of order $\leq 4$ are all desarguesian and the theorem is easily verified for $\mathcal{P}_2(K)$ with $K$ any field, by Exercise 4.24).

Let $\ell$ be any line and $V$ any point of $\mathcal{P}^\ell$. Let $\ell_1, \ell_2, \ell_3$ be distinct lines through $V$ and $A, B$ distinct points of $\ell$ not on any of $\ell_1, \ell_2, \ell_3$ (possible since $n > 4$).

Construct a mapping $\alpha$ from points of $\ell \setminus \{A, B, \ell\ell_1, \ell\ell_3\}$: pick $X \in \ell_1 \setminus \{V, \ell\ell_1\}$, join $A$ to $X$, let $X_2 = AX \cap \ell_2$, join $B$ to $X_2$, let $X_3 = BX_2 \cap \ell_3$, and define $X^\alpha = XX_3 \cap \ell$. By cardinality arguments, this mapping has a fixed point, which yields two triangles in perspective from $V$ and $\ell$.