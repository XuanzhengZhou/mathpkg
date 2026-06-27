---
role: proof
locale: en
of_concept: dedekind-modular-law
source_book: gtm028
source_chapter: "III"
source_section: "2. Operations on submodules"
---

It is clear that the right side is contained in the left: since $L \subset K$ and $L \subset L + N$, we have $L \subset K \cap (L + N)$. Also $K \cap N \subset K$ and $K \cap N \subset N \subset L + N$, so $K \cap N \subset K \cap (L + N)$. Therefore $L + (K \cap N) \subset K \cap (L + N)$.

Conversely, let $x \in K \cap (L + N)$. Then $x \in L + N$, so $x = y + z$ with $y \in L$, $z \in N$. Since $x \in K$ and $y \in L \subset K$, we have $z = x - y \in K$. Thus $z \in K \cap N$. Hence $x = y + z \in L + (K \cap N)$, proving the reverse inclusion.
