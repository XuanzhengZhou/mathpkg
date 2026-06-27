---
role: proof
locale: en
of_concept: bound-occurrence-relation-recursive
source_book: gtm037
source_chapter: ""
source_section: ""
---

$(m, k, x) \in S$ iff $m \in \text{Rng}(g \circ v)$, $x \in g^{+*}\text{Fmla}$, $k \leq \text{lx}$, $(x)_k = m + 1$ and $\exists i \leq \text{lx}\, \exists y \leq x\, [(m, i, x, y) \in R \text{ and } k \text{ is in the scope of the } i\text{th quantifier}]$.

All conditions are recursive (using Proposition 10.42 for $R$), hence $S$ is recursive.
