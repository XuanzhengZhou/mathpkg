---
role: proof
locale: en
of_concept: hopf-algebra-isomorphism-from-coalgebra-morphism
source_book: gtm020
source_chapter: "17"
source_section: "1"
---

Since $A = R \oplus I(A)$ as modules, we can iterate the above given isomorphism

$$\prod_{1 \leq k < m} I(C)^{k \otimes} \oplus (A \otimes I(C)^{m \otimes}) \to I(A)$$

whose restriction $f_m: \prod_{1 \leq k < m} I(C)^{k \otimes} \to I(A)$ is just the restriction of $f$ to this part of the tensor algebra. By the connectivity hypothesis $f_m$ is an isomorphism in degrees $< m$ and hence $f: T(C) \to A$ is an isomorphism because $I(C)^{m \otimes}$ is zero in degrees $< m$. This proves the proposition.
