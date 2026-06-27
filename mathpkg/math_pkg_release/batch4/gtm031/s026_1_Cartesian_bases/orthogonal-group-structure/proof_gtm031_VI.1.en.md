---
role: proof
locale: en
of_concept: orthogonal-group-structure
source_book: gtm031
source_chapter: "VI"
source_section: "1"
---

If $(\sigma)$ and $(\tau)$ are orthogonal matrices, then $(\sigma)(\tau)$ satisfies

$$(\sigma\tau)(\sigma\tau)' = (\sigma\tau)(\tau'\sigma') = \sigma(\tau\tau')\sigma' = \sigma \cdot 1 \cdot \sigma' = \sigma\sigma' = 1,$$

so the product is orthogonal. Also $(\sigma)^{-1}$ satisfies $(\sigma^{-1})(\sigma^{-1})' = \sigma^{-1}(\sigma')^{-1} = (\sigma'\sigma)^{-1} = 1^{-1} = 1$, so the inverse is orthogonal. Hence $O(\Phi, n)$ is a subgroup of $L(\Phi, n)$.

For any orthogonal matrix $(\sigma)$, $\det(\sigma)^2 = 1$, so $\det: O(\Phi, n) \to \{\pm 1\}$ is a group homomorphism. Its kernel is $O_1(\Phi, n) = \{\sigma \in O(\Phi, n) : \det(\sigma) = 1\}$, the set of proper orthogonal matrices. Since the determinant map is surjective onto $\{\pm 1\}$ (e.g., diag$(-1, 1, \ldots, 1)$ has determinant $-1$), $O_1(\Phi, n)$ is an invariant subgroup (as the kernel of a homomorphism) and $[O(\Phi, n) : O_1(\Phi, n)] = 2$.
