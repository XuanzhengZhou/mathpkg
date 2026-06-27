---
role: proof
locale: en
of_concept: construction-of-bifunctor-from-families
source_book: gtm005
source_chapter: "II"
source_section: "3"
---

For necessity, observe that in the product category $B \times C$, every arrow $\langle f, g \rangle: \langle b, c \rangle \to \langle b', c' \rangle$ factors as
$$\langle f, g \rangle = \langle f, 1_{c'} \rangle \circ \langle 1_b, g \rangle = \langle 1_{b'}, g \rangle \circ \langle f, 1_c \rangle.$$
Applying the functor $S$ to this equation yields
$$S(f, g) = S(f, 1_{c'}) \circ S(1_b, g) = S(1_{b'}, g) \circ S(f, 1_c).$$
Writing $S(f, 1_c) = L_c(f)$ and $S(1_b, g) = M_b(g)$, this gives
$$S(f, g) = L_{c'}(f) \circ M_b(g) = M_{b'}(g) \circ L_c(f),$$
so $M_{b'}(g) \circ L_c(f) = L_{c'}(f) \circ M_b(g)$, which is exactly the commutativity condition (4).

For sufficiency, given families $L_c$ and $M_b$ with $L_c(b) = M_b(c)$ satisfying the interchange condition, define $S$ on objects by $S(b, c) = L_c(b) = M_b(c)$ and on arrows by
$$S(f, g) = M_{b'}(g) \circ L_c(f) = L_{c'}(f) \circ M_b(g)$$
(the interchange condition ensures these two expressions are equal). One verifies that this $S$ preserves identities and composition, hence is a bifunctor with the required restrictions.
