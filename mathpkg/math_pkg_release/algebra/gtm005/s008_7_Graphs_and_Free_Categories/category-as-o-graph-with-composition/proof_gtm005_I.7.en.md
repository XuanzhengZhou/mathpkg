---
role: proof
locale: en
of_concept: category-as-o-graph-with-composition
source_book: gtm005
source_chapter: "I"
source_section: "7"
---

An $O$-graph consists of a set $O$ of objects and, for each ordered pair $(a, b) \in O \times O$, a set $\hom(a, b)$ of arrows. A category is an $O$-graph equipped with:

1. Identity: For each $a \in O$, an arrow $1_a \in \hom(a, a)$.
2. Composition: For $f \in \hom(a, b)$, $g \in \hom(b, c)$, a composite $g \circ f \in \hom(a, c)$.

These satisfy the unit laws ($1_b \circ f = f = f \circ 1_a$) and associativity ($h \circ (g \circ f) = (h \circ g) \circ f$). The proof that this is equivalent to the standard definition is a direct translation: the class of objects is $O$, hom-sets are the $\hom(a, b)$, and composition is given as an operation on the graph structure satisfying the axioms.
