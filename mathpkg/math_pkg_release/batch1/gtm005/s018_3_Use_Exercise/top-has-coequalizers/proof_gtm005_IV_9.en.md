---
role: proof
locale: en
of_concept: top-has-coequalizers
source_book: gtm005
source_chapter: "IV. Adjoints"
source_section: "9. Adjoints in Topology"
---

Proposition 1 was proved from the axioms of a category (faithful functor, equalizers in $D$, right-adjoint-right-inverse on slice categories). By duality, its dual is true: if $G: C \to D$ is a faithful functor, $D$ has coequalizers, and for each $x \in C$, $(x \downarrow G): (x \downarrow C) \to (Gx \downarrow D)$ has a left-adjoint-right-inverse, then $C$ has coequalizers.

Apply this dual to the forgetful functor $G: \mathbf{Top} \to \mathbf{Set}$. The functor $X \downarrow G: (X \downarrow \mathbf{Top}) \to (GX \downarrow \mathbf{Set})$ has a left-adjoint-right-inverse $M$, which equips a set function $t: GX \to S$ with the quotient topology. Since $\mathbf{Set}$ has coequalizers, $\mathbf{Top}$ has coequalizers.
