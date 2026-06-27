---
role: proof
locale: en
of_concept: economical-description-abelian-categories
source_book: gtm005
source_chapter: "VIII"
source_section: "3"
---

Theorem (Freyd): A category $A$ is abelian iff:
1. $A$ has finite products and finite coproducts.
2. Every arrow has a kernel and a cokernel.
3. Every monic is a kernel, and every epi is a cokernel.

Proof (sketch): From (1), $A$ has a zero object (empty product/coproduct), hence zero morphisms. Condition (2) provides kernels and cokernels. Define the image of $f: a \to b$ as $\ker(\operatorname{coker} f)$ and the coimage as $\operatorname{coker}(\ker f)$. 

Condition (3) ensures the canonical map $\operatorname{coim}(f) \to \operatorname{im}(f)$ is an isomorphism. This map arises from the universal property of cokernel and kernel: since $(\ker f)$ followed by $f$ is zero, $f$ factors through $\operatorname{coker}(\ker f) = \operatorname{coim}(f)$, yielding a map to $\operatorname{im}(f)$. Condition (3) applied to the epi/monic factorization shows this is an isomorphism.

Finite biproducts then give the additive structure, and the image-coimage factorization establishes the abelian property.
