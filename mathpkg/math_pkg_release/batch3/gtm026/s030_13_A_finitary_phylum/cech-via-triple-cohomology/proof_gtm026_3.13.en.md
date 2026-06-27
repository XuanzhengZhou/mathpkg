---
role: proof
locale: en
of_concept: cech-via-triple-cohomology
source_book: gtm026
source_chapter: "3"
source_section: "13"
---

We outline the construction showing that Čech cohomology arises as triple cohomology.

**Step 1: The functor $U = \gamma^*$ is algebraic.** The pullback functor along $\gamma: Z \rightarrow X$,

$$U: (\mathcal{K}, X) \rightarrow (\mathcal{K}, Z), \quad (A, a) \mapsto (A \times_X Z, \pi_2)$$

has a left adjoint $F = \Sigma_\gamma$ given by composition with $\gamma$: $(B, b) \mapsto (B, b \cdot \gamma)$. To show $U$ is algebraic (monadic), one verifies the Beck conditions using the properties of pullbacks in the category of topological spaces. The key point is that $U$ creates absolute coequalizers because pullbacks preserve coequalizers in $\mathbf{Top}$ when the maps involved are suitable.

**Step 2: The algebraic theory in $(\mathcal{K}, Z)$.** The adjunction $F \dashv U$ induces an algebraic theory (monad) $\mathbf{T}$ on $(\mathcal{K}, Z)$. By Exercise 19-20, this $\mathbf{T}$ yields triple cohomology groups.

**Step 3: Agreement with Čech cohomology.** For a topological abelian group $Y$, the Čech cochain complex of the cover $\mathcal{U}$ with coefficients in $Y$ is:

$$\check{C}^n(\mathcal{U}, Y) = \prod_{(U_0, \ldots, U_n)} Y(U_0 \cap \cdots \cap U_n)$$

where the product is over $(n+1)$-tuples of elements of $\mathcal{U}$ with nonempty intersection. The triple cochain complex from the algebraic theory $\mathbf{T}$ applied to the appropriate object in $(\mathcal{K}, Z)^{\mathbf{T}}$ yields an isomorphic complex. The isomorphism follows from the fact that $Z$ is the coproduct of the $U \in \mathcal{U}$, so maps out of $Z$ decompose as products of maps out of each $U$, and the nerve of the cover corresponds to the bar resolution.

Thus the triple cohomology groups coincide with the Čech cohomology groups $\check{H}^n(\mathcal{U}, Y)$.
