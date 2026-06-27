---
role: proof
locale: en
of_concept: change-of-basepoint-isomorphism
source_book: gtm047
source_chapter: "14"
source_section: "14"
---

**Proof.** Define $p^*(\bar{q}) = \overline{p^{-1}qp}$. To verify this is well-defined: if $q \cong q'$, then $p^{-1}qp \cong p^{-1}q'p$ by Theorem 2 (path multiplication respects equivalence).

$p^*$ is a homomorphism: for $\bar{q}, \bar{r} \in \pi(X, P_0)$,
$$p^*(\bar{q}\bar{r}) = \overline{p^{-1}qr p} \cong \overline{p^{-1}q p \, p^{-1} r p} = p^*(\bar{q}) \, p^*(\bar{r}),$$
since $pp^{-1} \cong e$.

$p^*$ is bijective with inverse $(p^{-1})^* = (p^*)^{-1}$, because $(p^{-1})^* \circ p^* = \text{id}$ and $p^* \circ (p^{-1})^* = \text{id}$, as $p^{-1}p \cong e$ and $pp^{-1} \cong e$.
