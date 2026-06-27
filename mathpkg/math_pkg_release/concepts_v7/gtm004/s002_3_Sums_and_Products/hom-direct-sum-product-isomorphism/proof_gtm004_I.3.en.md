---
role: proof
locale: en
of_concept: hom-direct-sum-product-isomorphism
source_book: gtm004
source_chapter: "I. Modules"
source_section: "3. Sums and Products"
---

# Proof of Isomorphism between Hom of Direct Sum and Product of Homs

The proof reveals that this theorem is merely a restatement of the universal property of the direct sum. For $\psi : \bigoplus_{j \in J} A_j \to B$, define

$$\eta(\psi) = (\psi i_j : A_j \to B)_{j \in J}.$$

Conversely, a family $\{\psi_j : A_j \to B\}$, $j \in J$, gives rise to a unique map $\psi : \bigoplus_{j \in J} A_j \to B$ by the universal property of the direct sum (Proposition 3.2). The projections $\pi_j : \prod_{j \in J} \operatorname{Hom}_\Lambda(A_j, B) \to \operatorname{Hom}_\Lambda(A_j, B)$ are given by $\pi_j \eta = \operatorname{Hom}_\Lambda(i_j, B)$.

These two constructions are inverse to each other, establishing the isomorphism

$$\eta : \operatorname{Hom}_\Lambda\left(\bigoplus_{j \in J} A_j, B\right) \xrightarrow{\sim} \prod_{j \in J} \operatorname{Hom}_\Lambda(A_j, B).$$
