---
role: proof
locale: en
of_concept: bound-on-mols
source_book: gtm006
source_chapter: "5"
source_section: "5. Latin Squares"
---

**Proof of Property 2.** By Property 1, we may assume that the given set of mutually orthogonal Latin squares is in normal form, so each square has $(0, 1, \dots, n-1)$ as its top row.

Consider the $(1,0)$-position (i.e., the position in the left column and second row from the top). None of the squares may have a $0$ in this position, since the $(0,0)$-position already contains $0$ (being in the top row) and the left column would then contain two zeros, violating the Latin square property.

Furthermore, no two distinct squares in the set may have the same entry, say $s$, in the $(1,0)$-position. For if they did, the ordered pair $(s, s)$ would occur both in the $(1,0)$-position and in the $(0,s)$-position (since in normal form the top row is $(0,1,\dots,n-1)$, the entry in row $0$, column $s$ is $s$ in all squares), contradicting orthogonality.

Thus the entries in the $(1,0)$-positions of the squares must be distinct elements of $\{1, 2, \dots, n-1\}$. There are only $n-1$ such possible entries, which gives an upper bound of $n-1$ on the number of mutually orthogonal Latin squares of order $n$.
