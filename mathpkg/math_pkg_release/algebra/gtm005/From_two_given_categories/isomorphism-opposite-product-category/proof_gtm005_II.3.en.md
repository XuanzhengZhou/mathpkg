---
role: proof
locale: en
of_concept: isomorphism-opposite-product-category
source_book: gtm005
source_chapter: "II"
source_section: "3"
---

Define $\Phi: (B \times C)^{\mathrm{op}} \to B^{\mathrm{op}} \times C^{\mathrm{op}}$ as identity on objects. On arrows: an arrow in $(B \times C)^{\mathrm{op}}$ from $(b, c)$ to $(b', c')$ is a pair $(f, g)^{\mathrm{op}}$ where $(f, g): (b', c') \to (b, c)$ in $B \times C$, i.e., $f: b' \to b$ in $B$, $g: c' \to c$ in $C$.

Then $f^{\mathrm{op}}: b \to b'$ in $B^{\mathrm{op}}$ and $g^{\mathrm{op}}: c \to c'$ in $C^{\mathrm{op}}$, so $(f^{\mathrm{op}}, g^{\mathrm{op}}): (b, c) \to (b', c')$ in $B^{\mathrm{op}} \times C^{\mathrm{op}}$. $\Phi$ preserves composition: for composable arrows, $\Phi((f', g')^{\mathrm{op}} \circ (f, g)^{\mathrm{op}}) = \Phi((f' \circ f, g' \circ g)^{\mathrm{op}}) = ((f' \circ f)^{\mathrm{op}}, (g' \circ g)^{\mathrm{op}}) = (f^{\mathrm{op}} \circ f'^{\mathrm{op}}, g^{\mathrm{op}} \circ g'^{\mathrm{op}})$.

The inverse functor is defined identically (mapping $(f^{\mathrm{op}}, g^{\mathrm{op}})$ to $(f, g)^{\mathrm{op}}$), giving an isomorphism of categories.
