---
role: proof
locale: en
of_concept: limit-group-structure-via-forgetful-functor
source_book: gtm005
source_chapter: "V"
source_section: "1"
---

By Theorem 1, take $L = \operatorname{Cone}(*, UH)$ as the limit set in $\mathbf{Set}$. Define the product of two cones $\sigma, \tau \in L$ componentwise: for each $j \in \operatorname{obj}(J)$, set $(\sigma \tau)_j = \sigma_j \tau_j$, where the right-hand side is the product in the group $H_j$. Since each $v_j$ is then a homomorphism by construction, and since $L$ with this operation satisfies the group axioms (the identity is the cone of identity elements, inverses are taken componentwise), $L$ becomes a group. The uniqueness follows because each $v_j$ being a group homomorphism forces the group operation on $L$ to be defined componentwise as above. The universal property holds: given any cone $\tau : M \to H$ in $\mathbf{Grp}$, the underlying set map $UM \to L = \operatorname{Cone}(*, UH)$ lifts uniquely to a group homomorphism by the same componentwise argument.
