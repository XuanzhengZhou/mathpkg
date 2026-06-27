---
role: proof
locale: en
of_concept: clutching-bundle-decomposition-isomorphism
source_book: gtm020
source_chapter: "10"
source_section: "4. Analysis of Linear Clutching Maps"
---

By (4.5), the linear homotopies $p_+^t$ and $p_-^t$ are isomorphisms onto their images for all $t$, $0 \leq t \leq 1$. Then the bundles
$$
[\zeta, p] \quad \text{and} \quad \left(\zeta_+^0 \bigcup_{a_+ z} \zeta_+^0\right) \oplus \left(\zeta_-^0 \bigcup_{b_-} \zeta_-^0\right)
$$
are isomorphic bundles over $X \times S^2$, where the notation $\zeta_+^0 \bigcup_{a_+ z} \zeta_+^0$ denotes the clutching construction using the clutching map $a_+ z$, and similarly $\zeta_-^0 \bigcup_{b_-} \zeta_-^0$ uses the clutching map $b_-$.

Since $a_+: \zeta_+^0 \to \zeta_+^0$ and $b_-: \zeta_-^0 \to \zeta_-^0$ are isomorphisms, there are bundle isomorphisms
$$
[\zeta_+^0, z] \cong \zeta_+^0 \bigcup_{a_+ z} \zeta_+^0, \qquad
[\zeta_-^0, 1] \cong \zeta_-^0 \bigcup_{b_-} \zeta_-^0.
$$
Combining these isomorphisms yields $[\zeta, p] \cong [\zeta_+^0, z] \oplus [\zeta_-^0, 1]$, which proves the proposition.
