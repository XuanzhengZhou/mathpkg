---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

The Free Category Theorem (Theorem 1 of Section I.7) states that for any directed graph $G$, there exists a category $C_G$ and a graph morphism $P: G \to UC_G$ universal among morphisms from $G$ to underlying graphs of categories. Concretely, $C_G$ has the vertices of $G$ as objects and finite paths in $G$ as arrows, with composition given by concatenation of paths. The universal property means that any graph morphism $D: G \to UB$ into the underlying graph of a category $B$ extends uniquely to a functor $C_G \to B$. This exhibits the free category construction as left adjoint to the forgetful functor $U: \mathbf{Cat} \to \mathbf{Grph}$.
