---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Proposition 1 of Mac Lane's \textit{Categories for the Working Mathematician} (Chapter IX, Section 7) establishes that a natural transformation between two functors that each possess an end induces a unique arrow between those ends. This induced arrow is called the \textit{end of the natural transformation}, denoted $\int_c \gamma_{c,c}$. The proof follows directly from the universal property of the end wedge: the composites $\gamma_{c,c} \circ \omega_c$ form a wedge, which factors uniquely through $\omega'$. The construction satisfies a composition rule $\int_c (\gamma' \cdot \gamma) = (\int_c \gamma') \circ (\int_c \gamma)$, making the end a functorial operation on natural transformations.
