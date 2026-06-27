---
role: proof
locale: en
of_concept: isomorphism-product-opposite
source_book: gtm005
source_chapter: "I"
source_section: "3. Products of Categories"
---

Define a functor $\Phi: (B \times C)^{\text{op}} \to B^{\text{op}} \times C^{\text{op}}$ as follows. On objects, $\Phi\langle b, c \rangle = \langle b, c \rangle$. On arrows, for $\langle f, g \rangle^{\text{op}}: \langle b', c' \rangle \to \langle b, c \rangle$ in $(B \times C)^{\text{op}}$ (which corresponds to $\langle f, g \rangle: \langle b, c \rangle \to \langle b', c' \rangle$ in $B \times C$), define
$$\Phi(\langle f, g \rangle^{\text{op}}) = \langle f^{\text{op}}, g^{\text{op}} \rangle,$$
which is an arrow $\langle b', c' \rangle \to \langle b, c \rangle$ in $B^{\text{op}} \times C^{\text{op}}$.

$\Phi$ is clearly bijective on objects and arrows. It preserves composition because, for composable arrows $\langle f, g \rangle^{\text{op}}$ followed by $\langle f', g' \rangle^{\text{op}}$ in $(B \times C)^{\text{op}}$:
$$\Phi(\langle f', g' \rangle^{\text{op}} \circ \langle f, g \rangle^{\text{op}}) = \Phi((\langle f, g \rangle \circ \langle f', g' \rangle)^{\text{op}}) = \Phi(\langle f \circ f', g \circ g' \rangle^{\text{op}})$$
$$= \langle (f \circ f')^{\text{op}}, (g \circ g')^{\text{op}} \rangle = \langle (f')^{\text{op}} \circ f^{\text{op}}, (g')^{\text{op}} \circ g^{\text{op}} \rangle$$
$$= \langle (f')^{\text{op}}, (g')^{\text{op}} \rangle \circ \langle f^{\text{op}}, g^{\text{op}} \rangle = \Phi(\langle f', g' \rangle^{\text{op}}) \circ \Phi(\langle f, g \rangle^{\text{op}}).$$

It preserves identities because $\Phi(1_{\langle b,c \rangle}^{\text{op}}) = \Phi(\langle 1_b, 1_c \rangle^{\text{op}}) = \langle 1_b^{\text{op}}, 1_c^{\text{op}} \rangle = 1_{\langle b, c \rangle}$ in $B^{\text{op}} \times C^{\text{op}}$. Thus $\Phi$ is an isomorphism of categories.
