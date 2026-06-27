---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

The hom-functor is the prototypical example of a mixed-variance bifunctor. For each pair of objects $(b, c)$, it gives the set of arrows $\hom_C(b, c)$. Given arrows $f: b' \to b$ (contravariant) and $g: c \to c'$ (covariant), the induced map sends $h: b \to c$ to $g \circ h \circ f: b' \to c'$. The fact that the ordinary hom-functors satisfy the necessary interchange condition follows from the associativity of composition in $C$.
