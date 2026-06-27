---
role: proof
locale: en
of_concept: free-category-forgetful-adjunction
source_book: gtm005
source_chapter: "II"
source_section: "7"
---

This follows immediately from Theorem 1. The natural bijection
$$\text{Cat}(C_G, B) \cong \text{Grph}(G, UB)$$
is established by the construction: given $D' : C_G \to B$, define $D = UD' \circ P$; conversely, given $D : G \to UB$, construct $D'$ as the unique functor extending $D$ along $P : G \to UC_G$ (see the proof of Theorem 1 for the explicit construction of $C_G$ by finite paths). Naturality in $G$ and $B$ follows from the universal property that $P$ is initial in $(G \downarrow U)$.
