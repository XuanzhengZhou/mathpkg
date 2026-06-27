---
role: proof
locale: en
of_concept: frame-semantics-lemma
source_book: gtm037
source_chapter: "30"
source_section: "Unusual Logics"
---

With each $\mathcal{L}$-structure $\mathfrak{A}$ and each frame $G$ for $A$ we associate an $\mathcal{L}''$-structure $\mathfrak{A}_G^*$ defined by:

$$A_G^* = \bigcup_{\tau \text{ a type}} G^\tau;$$
$$R_i^{\mathfrak{A}_G^*} = R_i^{\mathfrak{A}};$$
$$T_i^{\mathfrak{A}_G^*} = G^\tau;$$
$$S^{\mathfrak{A}_G^*} = \{(U_0, \ldots, U_m, V) : U_0, \ldots, U_m, V \in A_G^*, (U_0, \ldots, U_m) \in V \in G^\tau\}$$

where $\tau = (\sigma_0, \ldots, \sigma_m)$. The lemma is then proved by induction on the formula $\varphi$, checking each clause of the satisfaction definition.
