---
role: proof
locale: en
of_concept: mols-maximum-bound
source_book: gtm006
source_chapter: "V"
source_section: "5"
---

**Proof of Property 2.**

By Property 1 we may assume that the given set of mutually orthogonal $n \times n$ Latin squares is in normal form, so each square has $(0, 1, \dots, n-1)$ as its top row. Consider the $(1,0)$-position (the position in the left column and second row from the top) of each square.

No two distinct squares may have the same entry, say $s$, in the $(1,0)$-position. For if they did, then the ordered pair $(s, s)$ would occur in two distinct positions: at $(1,0)$ and at $(0, s)$ (since the top row of each square contains every symbol, and the symbol $s$ appears in column $s$ of the top row). This would violate orthogonality.

Moreover, none of the squares may have $0$ in the $(1,0)$-position. If a square had $0$ there, then its left column would contain two zeros (since $(0,0) = 0$ is already the entry at position $(0,0)$ in the top row), contradicting the Latin square property.

Therefore, the $(1,0)$-position of each square must be filled with one of the $n-1$ nonzero symbols $\{1, 2, \dots, n-1\}$, and no two squares may share the same symbol there. Hence there can be at most $n-1$ squares in the set.
