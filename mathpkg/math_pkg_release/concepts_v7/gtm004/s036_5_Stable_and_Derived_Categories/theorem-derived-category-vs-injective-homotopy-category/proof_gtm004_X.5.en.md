---
role: proof
locale: en
of_concept: theorem-derived-category-vs-injective-homotopy-category
source_book: gtm004
source_chapter: "X"
source_section: "5. Stable and Derived Categories"
---

# Proof of Theorem 5.1: Equivalence of Injective Homotopy Category and Bounded-Below Derived Category

**Theorem 5.1.** If the abelian category $\mathfrak{A}$ admits enough injectives, then the homotopy category $\mathfrak{K}^+(\mathfrak{I})$ of bounded-below complexes of injective objects and the bounded-below derived category $\mathfrak{D}^+(\mathfrak{A})$ are equivalent.

*Proof.* Let $\mathfrak{C}^+(\mathfrak{A})$ denote the category of cochain complexes in $\mathfrak{A}$ that are bounded below. Let $\mathfrak{C}^+(\mathfrak{I})$ be the full subcategory whose objects are complexes consisting of injective objects of $\mathfrak{A}$. Let $\mathfrak{K}^+(\mathfrak{A})$ be the homotopy category of $\mathfrak{C}^+(\mathfrak{A})$ (morphisms are cochain maps modulo homotopy), and let $\mathfrak{K}^+(\mathfrak{I})$ be the corresponding full subcategory. The derived category $\mathfrak{D}^+(\mathfrak{A})$ is the localization of $\mathfrak{K}^+(\mathfrak{A})$ with respect to the class of quasi-isomorphisms.

Consider the composition of functors

$$F: \mathfrak{K}^+(\mathfrak{I}) \hookrightarrow \mathfrak{K}^+(\mathfrak{A}) \xrightarrow{Q} \mathfrak{D}^+(\mathfrak{A}),$$

where the first arrow is the inclusion and $Q$ is the localization functor. We claim that $F$ is an equivalence of categories.

**Step 1: $F$ is essentially surjective.** Let $X^\bullet$ be an object of $\mathfrak{D}^+(\mathfrak{A})$, represented by a bounded-below cochain complex $C^\bullet \in \mathfrak{C}^+(\mathfrak{A})$. Since $\mathfrak{A}$ has enough injectives, we may construct a Cartan--Eilenberg injective resolution of $C^\bullet$: there exists a bicomplex $I^{\bullet,\bullet}$ whose columns are injective resolutions of the individual terms $C^n$, together with an augmentation $C^\bullet \to I^{\bullet,0}$ such that the total complex $\operatorname{Tot}^\oplus(I^{\bullet,\bullet})$ is a complex of injectives and the augmentation induces a quasi-isomorphism

$$C^\bullet \xrightarrow{\sim} \operatorname{Tot}^\oplus(I^{\bullet,\bullet}).$$

Let $J^\bullet = \operatorname{Tot}^\oplus(I^{\bullet,\bullet}) \in \mathfrak{C}^+(\mathfrak{I})$. In $\mathfrak{K}^+(\mathfrak{A})$, the quasi-isomorphism becomes an isomorphism after localization, so $C^\bullet \cong J^\bullet$ in $\mathfrak{D}^+(\mathfrak{A})$. Hence every object of $\mathfrak{D}^+(\mathfrak{A})$ is isomorphic to $F(J^\bullet)$ for some $J^\bullet \in \mathfrak{K}^+(\mathfrak{I})$.

**Step 2: $F$ is fully faithful.** It suffices to show that for any $I^\bullet \in \mathfrak{K}^+(\mathfrak{I})$ and any $C^\bullet \in \mathfrak{K}^+(\mathfrak{A})$, the canonical map

$$\operatorname{Hom}_{\mathfrak{K}^+(\mathfrak{A})}(I^\bullet, C^\bullet) \longrightarrow \operatorname{Hom}_{\mathfrak{D}^+(\mathfrak{A})}(I^\bullet, C^\bullet)$$

is an isomorphism; the full faithfulness for objects of $\mathfrak{K}^+(\mathfrak{I})$ then follows by taking both arguments in $\mathfrak{K}^+(\mathfrak{I})$. In the localization of $\mathfrak{K}^+(\mathfrak{A})$ at quasi-isomorphisms, the morphisms from $I^\bullet$ to $C^\bullet$ in $\mathfrak{D}^+(\mathfrak{A})$ are represented by "roofs"

$$\xymatrix{
& X^\bullet \ar[dl]_{s}^{\sim} \ar[dr]^{f} & \\
I^\bullet & & C^\bullet
}$$

where $s: X^\bullet \to I^\bullet$ is a quasi-isomorphism and $f: X^\bullet \to C^\bullet$ is a morphism in $\mathfrak{K}^+(\mathfrak{A})$. Since $I^\bullet$ is a bounded-below complex of injectives and $s$ is a quasi-isomorphism, $s$ admits a homotopy inverse (see Chapter IV, Theorem 4.4, the dual statement for injective complexes). That is, there exists $t: I^\bullet \to X^\bullet$ in $\mathfrak{K}^+(\mathfrak{A})$ such that $s \circ t \simeq \operatorname{id}_{I^\bullet}$ and $t \circ s \simeq \operatorname{id}_{X^\bullet}$. Consequently, every roof as above is equivalent to a single morphism $f \circ t: I^\bullet \to C^\bullet$ in $\mathfrak{K}^+(\mathfrak{A})$. This establishes the desired isomorphism of Hom-sets, proving that $F$ is fully faithful.

**Conclusion.** $F: \mathfrak{K}^+(\mathfrak{I}) \to \mathfrak{D}^+(\mathfrak{A})$ is essentially surjective and fully faithful, hence an equivalence of categories. $\square$

*Remark.* This result shows that the derived category $\mathfrak{D}^+(\mathfrak{A})$ can be concretely realised as the homotopy category of injective complexes, providing the fundamental link between the classical approach to derived functors via injective resolutions and the modern framework of derived categories. The left-bounded and bounded variants ($\mathfrak{D}^-(\mathfrak{A})$ with projectives and $\mathfrak{D}^b(\mathfrak{A})$) admit analogous statements.
