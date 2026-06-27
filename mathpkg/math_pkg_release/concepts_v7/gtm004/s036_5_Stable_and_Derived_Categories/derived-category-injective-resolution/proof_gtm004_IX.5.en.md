---
role: proof
locale: en
of_concept: derived-category-injective-resolution
source_book: gtm004
source_chapter: "IX. Relative Homological Algebra"
source_section: "5. Stable and Derived Categories"
---

# Proof of Derived Category and Injective Resolutions

**Theorem 5.1.** Let $\mathfrak{A}$ be an abelian category with enough injectives. Then the natural functor

$$\Phi: \mathfrak{K}^+(\mathfrak{I}) \longrightarrow \mathfrak{D}^+(\mathfrak{A})$$

from the homotopy category of bounded-below complexes of injective objects to the bounded-below derived category is an equivalence of categories.

*Proof.* The functor $\Phi$ is the composition of the inclusion $\mathfrak{K}^+(\mathfrak{I}) \hookrightarrow \mathfrak{K}^+(\mathfrak{A})$ with the localization functor $Q: \mathfrak{K}^+(\mathfrak{A}) \to \mathfrak{D}^+(\mathfrak{A})$ that inverts quasi-isomorphisms. We prove that $\Phi$ is essentially surjective and fully faithful.

**Essential surjectivity.** Let $X^\bullet$ be any object of $\mathfrak{D}^+(\mathfrak{A})$, represented by a bounded-below cochain complex $C^\bullet$. Since $\mathfrak{A}$ has enough injectives, each term $C^n$ admits a monomorphism into an injective object. Using standard techniques (compare Chapter IV, Section 5), we can construct a quasi-isomorphism $C^\bullet \xrightarrow{\sim} I^\bullet$ where $I^\bullet$ is a bounded-below complex of injective objects. (Explicitly, embed $C^\bullet$ into a suitable Cartan--Eilenberg resolution of injectives, then take the total complex.) In $\mathfrak{D}^+(\mathfrak{A})$ this quasi-isomorphism becomes an isomorphism, so $X^\bullet \cong \Phi(I^\bullet)$.

**Full faithfulness.** Since $\mathfrak{D}^+(\mathfrak{A})$ is the localization of $\mathfrak{K}^+(\mathfrak{A})$ at quasi-isomorphisms, morphisms in $\mathfrak{D}^+(\mathfrak{A})$ between $I^\bullet, J^\bullet \in \mathfrak{K}^+(\mathfrak{I})$ are represented by equivalence classes of diagrams

$$\xymatrix{
& Y^\bullet \ar[dl]_{s}^{\sim} \ar[dr]^{f} & \\
I^\bullet & & J^\bullet
}$$

where $s: Y^\bullet \to I^\bullet$ is a quasi-isomorphism in $\mathfrak{K}^+(\mathfrak{A})$ and $f: Y^\bullet \to J^\bullet$ is a morphism in $\mathfrak{K}^+(\mathfrak{A})$. We claim that each such roof is equivalent to an honest morphism $I^\bullet \to J^\bullet$ in $\mathfrak{K}^+(\mathfrak{I})$.

Since $I^\bullet$ is a bounded-below complex of injectives and $s$ is a quasi-isomorphism, the dual of the fundamental lifting lemma (Chapter IV, Theorem 4.4) provides a morphism $t: I^\bullet \to Y^\bullet$ in $\mathfrak{K}^+(\mathfrak{A})$ such that $s \circ t \simeq \operatorname{id}_{I^\bullet}$. (The existence of such a homotopy inverse is a consequence of $I^\bullet$ being $K$-injective in the sense of Spaltenstein.) The roof $(s, f)$ is then equivalent to the single morphism $f \circ t: I^\bullet \to J^\bullet$.

Moreover, if $f \circ t$ is homotopic to zero, then the roof represents the zero morphism in $\mathfrak{D}^+(\mathfrak{A})$. Thus the natural map

$$\operatorname{Hom}_{\mathfrak{K}^+(\mathfrak{I})}(I^\bullet, J^\bullet) \longrightarrow \operatorname{Hom}_{\mathfrak{D}^+(\mathfrak{A})}(\Phi(I^\bullet), \Phi(J^\bullet))$$

is an isomorphism. This proves full faithfulness.

Having established both essential surjectivity and full faithfulness, $\Phi$ is an equivalence of categories. $\square$

*Remarks.* (1) This theorem explains why the classical approach to derived functors---using injective resolutions---is subsumed by the derived category formalism. For a left exact functor $F: \mathfrak{A} \to \mathfrak{B}$, its right derived functor $RF: \mathfrak{D}^+(\mathfrak{A}) \to \mathfrak{D}^+(\mathfrak{B})$ can be computed by applying $F$ termwise to an injective replacement, which corresponds to the classical construction of the $n$-th right derived functor via $R^nF(A) = H^n(F(I^\bullet))$.

(2) The analogous statement for $\mathfrak{D}^-(\mathfrak{A})$ using projective resolutions holds when $\mathfrak{A}$ has enough projectives. For the bounded derived category $\mathfrak{D}^b(\mathfrak{A})$, one needs suitable finiteness conditions on injective (or projective) dimension.
