---
role: proof
locale: en
of_concept: subobject-classifier-for-presheaf-category
source_book: gtm005
source_chapter: "I"
source_section: "9. Subsets and Characteristic Functions"
---

The construction of the subobject classifier $\Omega$ for $\mathbf{Sets}^{\mathcal{C}^{\mathrm{op}}}$ proceeds as follows. For each object $c \in \mathcal{C}$, define $\Omega(c)$ to be the set of all sieves on $c$, i.e., collections $S$ of morphisms with codomain $c$ such that if $f \in S$ and $g$ is composable with $f$, then $f \circ g \in S$. The functorial action of $\Omega$ on a morphism $h : d \to c$ is given by pulling back sieves: $\Omega(h)(S) = \{ g : \cdot \to d \mid h \circ g \in S \}$.

The terminal presheaf $1$ satisfies $1(c) = \{*\}$ for all $c$. Define $\mathsf{true} : 1 \to \Omega$ by $\mathsf{true}_c(*) = \text{maximal sieve on } c$ (all morphisms with codomain $c$). This is a monomorphism since $\mathsf{true}_c$ is injective for each $c$.

Given a subobject (monomorphism) $\alpha : F \rightarrowtail G$ in $\mathbf{Sets}^{\mathcal{C}^{\mathrm{op}}}$, for each $c \in \mathcal{C}$ the component $\alpha_c : F(c) \hookrightarrow G(c)$ is an injection. For each $c$ and each $x \in G(c)$, define the sieve $\chi(x)_c = \{ f : d \to c \mid G(f)(x) \in F(d) \}$, which is a sieve on $c$. This natural transformation $\chi : G \to \Omega$ is the classifying map, and one verifies that $F$ is the pullback of $\mathsf{true}$ along $\chi$. Uniqueness of $\chi$ follows from the Yoneda lemma.
