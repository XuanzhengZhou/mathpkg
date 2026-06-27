---
role: proof
locale: en
of_concept: hom-functor-as-bifunctor
source_book: gtm005
source_chapter: "II"
source_section: "3"
---

For the hom-functor, the families are $L_c = \hom_C(-, c): C^{\mathrm{op}} \to \mathbf{Set}$ for each $c \in C$, and $M_b = \hom_C(b, -): C \to \mathbf{Set}$ for each $b \in C$. These satisfy $L_c(b) = M_b(c) = \hom_C(b, c)$. For arrows $f: b' \to b$ (so $f^{\mathrm{op}}: b \to b'$ in $C^{\mathrm{op}}$) and $g: c \to c'$, the commutativity condition requires
$$M_{b'}(g) \circ L_c(f^{\mathrm{op}}) = L_{c'}(f^{\mathrm{op}}) \circ M_b(g).$$
On an element $h \in \hom_C(b, c)$, both sides compute $g \circ h \circ f$, which is an element of $\hom_C(b', c')$. This equality holds by associativity of composition in $C$. Thus the interchange condition is satisfied, and $\hom_C$ is indeed a bifunctor.
