---
role: proof
locale: en
of_concept: kuratowski-planarity-theorem
source_book: gtm054
source_chapter: "III"
source_section: "13 (III.G Kuratowski's Theorem)"
---

This section is devoted to proving Kuratowski's Theorem. A complete proof extends beyond the current section and uses results on lobes and separating sets. The key reduction is:

A multigraph is planar if and only if its lobes are planar. This is extended to biconnected and triconnected multigraphs via Proposition G3, which shows that planarity can be checked on contracted components obtained by cutting along a minimal separating set $W$ with $|W| \leq 3$. By iteratively applying this reduction, the problem is reduced to checking planarity of $3$-connected multigraphs, for which the forbidden subcontractions $K_5$ and $K_{3,3}$ serve as the only obstructions.
