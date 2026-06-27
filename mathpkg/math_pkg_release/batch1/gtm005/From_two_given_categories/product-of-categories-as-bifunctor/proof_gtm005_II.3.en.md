---
role: proof
locale: en
of_concept: product-of-categories-as-bifunctor
source_book: gtm005
source_chapter: "II"
source_section: "3"
---

The product $B \times C$ has objects $(b, c)$ and arrows $(f, g): (b, c) \to (b', c')$. Composition is pointwise: $(f', g') \circ (f, g) = (f' \circ f, g' \circ g)$. This is a category.

The assignment $\times: \mathbf{Cat} \times \mathbf{Cat} \to \mathbf{Cat}$ is a bifunctor: on functors $F: B \to B'$, $G: C \to C'$, define $F \times G: B \times C \to B' \times C'$ by $(F \times G)(b, c) = (F(b), G(c))$ and similarly on arrows. Then $(F' \times G') \circ (F \times G) = (F' \circ F) \times (G' \circ G)$ and $1_B \times 1_C = 1_{B \times C}$, verifying functoriality.
