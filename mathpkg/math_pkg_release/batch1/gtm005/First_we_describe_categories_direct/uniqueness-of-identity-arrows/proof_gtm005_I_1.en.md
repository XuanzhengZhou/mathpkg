---
role: proof
locale: en
of_concept: uniqueness-of-identity-arrows
source_book: gtm005
source_chapter: "I. Categories, Functors, and Natural Transformations"
source_section: "1. Axioms for Categories"
---

Suppose $1_b$ and $1_b'$ are two arrows $b \to b$ both satisfying the unit law, i.e., for all arrows $f: a \to b$ and $g: b \to c$,
$$1_b \circ f = f, \quad g \circ 1_b = g,$$
and similarly for $1_b'$. Applying the unit law for $1_b$ with $g = 1_b'$ gives $1_b' \circ 1_b = 1_b'$. Applying the unit law for $1_b'$ with $f = 1_b$ gives $1_b' \circ 1_b = 1_b$. Hence $1_b = 1_b'$, proving uniqueness.
