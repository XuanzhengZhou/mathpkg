---
role: proof
locale: en
of_concept: proposition-6-13-properties-of-sheaf-associated-to-divisor
source_book: gtm052
source_chapter: "II"
source_section: "6"
---
(a) Since each $f_i \in \Gamma(U_i, \mathcal{K}^*)$, the map $\mathcal{O}_{U_i} \to \mathcal{L}(D)|_{U_i}$ defined by $1 \mapsto f_i^{-1}$ is an isomorphism. Thus $\mathcal{L}(D)$ is an invertible sheaf. The Cartier divisor $D$ can be recovered from $\mathcal{L}(D)$ together with its embedding in $\mathcal{K}$ by taking $f_i$ on $U_i$ as the inverse of a local generator of $\mathcal{L}(D)$.

(b) Follows from the definition: on $U_i \cap U_j$, the generators for $\mathcal{L}(D_1 - D_2)$ are $(f_{1,i}/f_{2,i})^{-1} = f_{1,i}^{-1} \cdot f_{2,i}$, which is exactly the generator for $\mathcal{L}(D_1) \otimes \mathcal{L}(D_2)^{-1}$.

(c) If $D_1 \sim D_2$, then $D_1 - D_2 = (f)$ is principal, so $\mathcal{L}(D_1 - D_2) \cong \mathcal{O}_X$, and by (b) $\mathcal{L}(D_1) \cong \mathcal{L}(D_2)$. Conversely, an isomorphism $\mathcal{L}(D_1) \cong \mathcal{L}(D_2)$ induces an isomorphism of their embeddings in $\mathcal{K}$, which gives the principal divisor.
