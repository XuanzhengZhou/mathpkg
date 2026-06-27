---
role: proof
locale: en
of_concept: additive-group-structure-uniqueness
source_book: gtm004
source_chapter: "II"
source_section: "9"
---

# Proof of Uniqueness of Additive Structure on an Additive Category

Let $\mathfrak{A}$ be an additive category. Suppose one defines two additive structures on $\mathfrak{A}$: one via the enrichment in abelian groups determined by the canonical biproduct structure, and another via some alternative definition. We show they coincide.

Given objects $A, B \in \mathfrak{A}$, the addition in $\mathfrak{A}(A, B)$ is determined by the biproduct structure. Specifically, for $f, g: A \to B$, the sum $f + g$ is given by the composition

$$A \xrightarrow{\Delta} A \oplus A \xrightarrow{f \oplus g} B \oplus B \xrightarrow{\nabla} B,$$

where $\Delta = \{1_A, 1_A\}: A \to A \oplus A$ is the diagonal (using the product structure) and $\nabla = \langle 1_B, 1_B \rangle: B \oplus B \to B$ is the codiagonal (using the coproduct structure), and $f \oplus g = \{f p_1, g p_2\}: A \oplus A \to B \oplus B$.

Now, any additive structure must satisfy bilinearity of composition. In particular, for any $A$, the morphism $0: A \to A$ is uniquely determined as the additive identity of the abelian group $\mathfrak{A}(A, A)$. The zero morphism $0: A \to B$ must factor through the zero object: $A \to 0 \to B$, which is unique.

Moreover, the biproduct $A \oplus B$ with its projections $p_i$ and injections $i_j$ satisfying $p_j i_k = \delta_{jk}$ and $i_1 p_1 + i_2 p_2 = 1$ completely determines the addition, since for any $f, g: X \to Y$,

$$f + g = \nabla_Y \circ (f \oplus g) \circ \Delta_X,$$

and this formula uses only the category-theoretic biproduct structure and composition. By Proposition 9.1, the biproduct structure is itself forced by the existence of finite products and the abelian group structure on hom-sets. Therefore the additive structure (the abelian group law on each hom-set) is uniquely determined by the categorical structure of finite products and zero object.

Alternatively, if $U: \mathfrak{A} \to \mathfrak{S}$ is the "underlying set" functor that lifts to $\mathfrak{Ab}$, then Corollary 9.4 asserts that this lifting is unique: there is at most one way to enrich an additive category in abelian groups consistent with the biproduct structure.
