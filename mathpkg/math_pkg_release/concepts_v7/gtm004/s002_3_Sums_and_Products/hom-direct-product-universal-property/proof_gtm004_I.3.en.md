---
role: proof
locale: en
of_concept: hom-direct-product-universal-property
source_book: gtm004
source_chapter: "I. Modules"
source_section: "3. Sums and Products"
---

# Proof of Isomorphism between Hom into Direct Product and Product of Homs

Define $\zeta : \operatorname{Hom}_\Lambda(A, \prod_{j \in J} B_j) \to \prod_{j \in J} \operatorname{Hom}_\Lambda(A, B_j)$ by

$$\zeta(\varphi) = (\pi_j \circ \varphi : A \to B_j)_{j \in J},$$

where $\pi_j : \prod_{j \in J} B_j \to B_j$ are the canonical projections.

Conversely, given a family $\{\varphi_j : A \to B_j\}_{j \in J}$, the universal property of the direct product (Proposition 3.3) yields a unique homomorphism $\varphi : A \to \prod_{j \in J} B_j$ such that $\pi_j \circ \varphi = \varphi_j$ for all $j \in J$. This defines the inverse $\zeta^{-1}$.

The maps $\zeta$ and $\zeta^{-1}$ are $\Lambda$-module homomorphisms and are inverse to each other, establishing the isomorphism

$$\zeta : \operatorname{Hom}_\Lambda\left(A, \prod_{j \in J} B_j\right) \xrightarrow{\sim} \prod_{j \in J} \operatorname{Hom}_\Lambda(A, B_j).$$
