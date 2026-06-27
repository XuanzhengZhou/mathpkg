---
role: proof
locale: en
of_concept: lambda-algebras-form-algebraic-category
source_book: gtm026
source_chapter: "3"
source_section: "3.15"
---

**Note:** The proof of Theorem 3.15 was truncated in the source text. The following is a sketch based on the context provided in the preceding discussion (3.11 through 3.14).

**Proof sketch.** The aim is to show that the forgetful functor $U \colon \mathcal{K}^{\lambda} \to \mathcal{K}$ is monadic, i.e., that $\mathcal{K}^{\lambda}$ is algebraic over $\mathcal{K}$. The proof makes crucial use of the distributive law axioms from Definition 3.6.

For the case $\mathcal{K} = \mathbf{Set}$, it was observed in the discussion following Definition 3.11 that $\mathbf{Set}^{\lambda}$ is isomorphic in $\mathbf{Struct}(\mathbf{Set})$ to $\mathbf{Set}^{\mathbf{X} \otimes \mathbf{T}}$, which is algebraic over $\mathbf{Set}$ by Theorem 3.6.21. Here $\mathbf{X} \otimes \mathbf{T}$ denotes the composite algebraic theory whose structure is induced by the distributive law.

For a general base category $\mathcal{K}$, one constructs the composite theory $\mathbf{X} \otimes_{\lambda} \mathbf{T}$ using the distributive law $\lambda$, generalizing the tensor product of theories from 3.6. The category of algebras for this composite theory is then shown to be isomorphic to $\mathcal{K}^{\lambda}$. Since categories of algebras for algebraic theories are algebraic over the base, the result follows.

The proof requires verifying the two distributive law axioms (unit and multiplication from 3.6) to ensure the composite theory is well-defined, and then establishing the equivalence between the $\lambda$-algebra condition (that $\xi$ is an $X$-dynamorphism) and the algebra condition for the composite theory.
