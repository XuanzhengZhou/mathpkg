---
role: proof
locale: en
of_concept: stiefel-whitney-class-thom-formula
source_book: gtm020
source_chapter: "9"
source_section: "9.1"
---

From the uniqueness character of $w_i$ it suffices to prove that $w^*(\xi) = \phi^{-1}SqU_\xi$ satisfies statements $(\text{SW}_0)$ to $(\text{SW}_3)$.

First, $(\text{SW}_0)$ follows from the property that $Sq^0 = \text{id}$, so $w_0(\xi) = \phi^{-1}(Sq^0 U_\xi) = \phi^{-1}(U_\xi) = 1$ in $H^0(B; Z_2)$.

For $(\text{SW}_1)$, consider the canonical line bundle $\gamma^1$ over $RP^\infty$. The Thom class $U_{\gamma^1}$ and the action of $Sq^1$ yield the nonzero class in $H^1(RP^\infty; Z_2)$, which is precisely $w_1(\gamma^1)$.

For $(\text{SW}_2)$, the Whitney sum formula, one uses the naturality of the Steenrod squares and the Cartan formula $Sq^k(a \cup b) = \sum_{i+j=k} Sq^i(a) \cup Sq^j(b)$ applied to the Thom classes of direct sums of bundles.

For $(\text{SW}_3)$, the condition $w_i(\xi) = 0$ for $i > \dim(\xi)$, this follows from the vanishing of $Sq^i U_\xi$ for $i > \dim(\xi)$, since $U_\xi$ lives in degree $n = \dim(\xi)$ and $Sq^i$ raises degree by $i$, while the cohomology of $(E, E_0)$ vanishes above degree $2n$.
