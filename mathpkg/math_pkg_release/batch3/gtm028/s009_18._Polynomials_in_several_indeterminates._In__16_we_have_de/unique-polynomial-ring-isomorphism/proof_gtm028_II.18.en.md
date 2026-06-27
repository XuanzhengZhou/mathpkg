---
role: proof
locale: en
of_concept: unique-polynomial-ring-isomorphism
source_book: gtm028
source_chapter: "II"
source_section: "18"
---

Apply the isomorphism extension theorem with $T_0 = \text{id}_R$ (the identity isomorphism of $R$ onto itself). Both $S^\prime = R[x_1, \dots, x_n]$ and $\bar{S} = R[y_1, \dots, y_n]$ are polynomial rings over $R$, so the $y_i$ are algebraically independent over $R$. By the theorem, there exists a unique isomorphism $T: S^\prime \to \bar{S}$ extending $\text{id}_R$ and sending $x_i \mapsto y_i$ for $i = 1, \dots, n$. Since $T$ extends the identity on $R$, it is an $R$-isomorphism.
