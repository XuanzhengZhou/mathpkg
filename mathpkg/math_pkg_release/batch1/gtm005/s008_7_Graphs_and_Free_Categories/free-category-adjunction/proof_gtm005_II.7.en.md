---
role: proof
locale: en
of_concept: free-category-adjunction
source_book: gtm005
source_chapter: "II"
source_section: "7"
---

This is a direct consequence of Theorem 1 (free category). By Theorem 1, for each graph $G$ there is a universal morphism $P: G \to UC_G$ such that every $D: G \to UB$ factors uniquely as $D = UD' \circ P$ for a unique functor $D': C_G \to B$. This establishes a bijection

$$\mathbf{Cat}(C_G, B) \cong \mathbf{Grph}(G, UB), \qquad D' \mapsto UD' \circ P.$$

Naturality in $G$: for any graph morphism $H: G \to G'$, the induced functor $C_H: C_G \to C_{G'}$ makes the diagram commute, ensuring naturality of the bijection in the first variable.

Naturality in $B$: for any functor $F: B \to B'$, post-composition yields commutativity of the relevant square, giving naturality in the second variable.

Thus $C: \mathbf{Grph} \to \mathbf{Cat}$ is left adjoint to $U: \mathbf{Cat} \to \mathbf{Grph}$, with unit $P: \text{Id}_{\mathbf{Grph}} \to UC$ whose component at $G$ is $P_G: G \to UC_G$.
