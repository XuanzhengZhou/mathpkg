---
role: proof
locale: en
of_concept: prop-invariant-b-via-ramification-groups
source_book: gtm042
source_chapter: '19'
source_section: 19.3 An invariant
---

This follows from the formula $g \cdot sw_G = \sum_{i \geq 1} g_i \operatorname{Ind}_{G_i}^G(u_{G_i})$ by observing that $\langle \operatorname{Ind}_{G_i}^G(u_{G_i}), \phi_M \rangle$ is equal to $\dim_k(M/M^{G_i})$. Indeed, by Frobenius reciprocity,

$$\langle \operatorname{Ind}_{G_i}^G(u_{G_i}), \phi_M \rangle = \langle u_{G_i}, \operatorname{Res}_{G_i}^G \phi_M \rangle.$$

The character $u_{G_i}$ of the regular representation of $G_i$ pairs with the restriction of $\phi_M$ to give the dimension of the coinvariant space $M/M^{G_i}$, which equals the codimension of the fixed subspace.
