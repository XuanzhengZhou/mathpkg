---
role: proof
locale: en
of_concept: inverse-of-concrete-isomorphism-is-over-k
source_book: gtm026
source_chapter: "3"
source_section: "3.3"
---

Since $H$ is a homomorphism in $\text{Con}(\mathcal{K})$, we have $U = V H$. If $H$ is an isomorphism of categories with inverse $H^{-1}$, then composing on the right by $H^{-1}$ gives

$$U H^{-1} = V H H^{-1} = V \circ \mathrm{id}_{\mathcal{B}} = V.$$

But we must also check that $H^{-1}$ is indeed the inverse in $\text{Con}(\mathcal{K})$, i.e., that $V H^{-1} = U$. From $U = V H$, composing with $H^{-1}$ yields $U H^{-1} = V$, which is exactly the required commutativity condition. Therefore $H^{-1}: (\mathcal{B}, V) \to (\mathcal{A}, U)$ is a homomorphism of concrete categories, and $H$ is an isomorphism in $\text{Con}(\mathcal{K})$.
