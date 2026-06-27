---
role: proof
locale: en
of_concept: functoriality-of-product-of-functors
source_book: gtm005
source_chapter: "I"
source_section: "3. Products of Categories"
---

For any object $\langle b, c \rangle$ in $B \times C$:
$$((U' \times V') \circ (U \times V))\langle b, c \rangle = (U' \times V')(\langle Ub, Vc \rangle) = \langle U'(Ub), V'(Vc) \rangle = \langle (U'U)b, (V'V)c \rangle = (U'U \times V'V)\langle b, c \rangle.$$

For any arrow $\langle f, g \rangle: \langle b, c \rangle \to \langle b', c' \rangle$ in $B \times C$:
$$((U' \times V') \circ (U \times V))\langle f, g \rangle = (U' \times V')(\langle Uf, Vg \rangle) = \langle U'(Uf), V'(Vg) \rangle = \langle (U'U)f, (V'V)g \rangle = (U'U \times V'V)\langle f, g \rangle.$$

Thus the two functors agree on all objects and arrows, so they are equal.
