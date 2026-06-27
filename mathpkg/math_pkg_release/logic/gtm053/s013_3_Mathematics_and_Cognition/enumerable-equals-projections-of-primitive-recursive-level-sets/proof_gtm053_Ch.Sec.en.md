---
role: proof
locale: en
of_concept: enumerable-equals-projections-of-primitive-recursive-level-sets
source_book: gtm053
source_chapter: "V"
source_section: "4"
---

The first direction (b) $\subset$ (a) uses three cases based on projection codimension $m = 0, 1, \geqslant 2$. For $m = 1$, the $\mu$-operator directly gives a partial recursive function. For $m \geqslant 2$, the codimension reduction lemma (4.5) providing a recursive bijection $t^{(m)}: \mathbb{Z}^+ \to (\mathbb{Z}^+)^m$ reduces to case $m=1$.

The converse direction shows that graphs of partial recursive functions are primitive enumerable (i.e., projections of primitive recursive level sets). This uses the Godel function $\operatorname{Gd}(k, t)$ to encode sequences, and proceeds by verifying closure under the elementary operations: composition, juxtaposition, the $\mu$-operator, and recursion.
