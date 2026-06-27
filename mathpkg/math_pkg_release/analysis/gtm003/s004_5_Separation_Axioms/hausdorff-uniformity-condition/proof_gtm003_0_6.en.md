---
role: proof
locale: en
of_concept: hausdorff-uniformity-condition
source_book: gtm003
source_chapter: "0"
source_section: "6"
---

The text states the equivalence without detailed proof. Sufficiency: If $\bigcap \mathfrak{W} = \Delta$, then for distinct $x \neq y$, there exists a vicinity $W$ with $(x,y) \notin W$. By the uniformity axioms, one can find a symmetric vicinity $V$ with $V \circ V \subset W$. Then the uniform neighborhoods $V[x]$ and $V[y]$ are disjoint, proving the Hausdorff property. Necessity: If the uniform topology is Hausdorff, then for any $(x,y) \notin \Delta$ (i.e., $x \neq y$), there exist disjoint uniform neighborhoods, implying some vicinity misses $(x,y)$. Hence the intersection of all vicinities is exactly $\Delta$.
