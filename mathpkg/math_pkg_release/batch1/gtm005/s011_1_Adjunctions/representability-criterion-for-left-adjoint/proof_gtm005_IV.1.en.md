---
role: proof
locale: en
of_concept: representability-criterion-for-left-adjoint
source_book: gtm005
source_chapter: "IV"
source_section: "1"
---

$G: C \to D$ has a left adjoint iff for each $d \in D$, the functor $D(d, G(-)): C \to \mathbf{Set}$ is representable.

($\Rightarrow$) If $F \dashv G$, then $C(F(d), -) \cong D(d, G(-))$ naturally in the second variable, so $F(d)$ represents $D(d, G(-))$ with universal element $\eta_d$.

($\Leftarrow$) For each $d$, choose a representation $(F_0(d), \eta_d)$ of $D(d, G(-))$, with isomorphism $\psi_{d,c}: C(F_0(d), c) \xrightarrow{\cong} D(d, G(c))$. For $f: d \to d'$, define $F(f): F_0(d) \to F_0(d')$ as $\psi_{d, F_0(d')}^{-1}(\eta_{d'} \circ f)$. This makes $F$ a functor and $\psi$ natural in $d$, establishing $F \dashv G$.
