---
role: proof
locale: en
of_concept: theory-category-embedding
source_book: gtm026
source_chapter: "2"
source_section: "2.10"
---

The passages of Proposition 2.9 assign to each theory map $\lambda: T \to T'$ a functor $V: \mathcal{K}^{T'} \to \mathcal{K}^T$, which is a morphism of algebraic functors from $(\mathcal{K}^{T'}, U^{T'})$ to $(\mathcal{K}^T, U^T)$ in $\mathrm{Struct}(\mathcal{K})$. This assignment is contravariant: a theory map $T \to T'$ gives a functor $\mathcal{K}^{T'} \to \mathcal{K}^T$, which corresponds to a morphism in the opposite direction of the algebraic functors. Hence we obtain a functor
$$
(\mathrm{Th}(\mathcal{K}))^{\mathrm{op}} \longrightarrow \mathrm{Alg}(\mathcal{K}).
$$

The only details left to check are the preservation of identities and composition. These are immediate:
$$
X\lambda \cdot \xi = \xi \quad \text{if } X\lambda = \mathrm{id}_{XT},
$$
since the action of the identity theory map is trivial. For composition:
$$
(X\lambda \cdot X\lambda') \cdot \xi'' = X\lambda \cdot (X\lambda' \cdot \xi''),
$$
which follows from the associativity of the algebra action. Thus the functor is well-defined and, by construction, fully faithful and representative on objects (every algebraic functor is isomorphic to some $(\mathcal{K}^T, U^T)$), making it a full representative subcategory.
