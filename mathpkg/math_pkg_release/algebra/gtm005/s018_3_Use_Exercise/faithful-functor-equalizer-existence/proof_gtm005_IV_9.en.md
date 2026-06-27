---
role: proof
locale: en
of_concept: faithful-functor-equalizer-existence
source_book: gtm005
source_chapter: "IV. Adjoints"
source_section: "9. Adjoints in Topology"
---

To get the equalizer of a parallel pair $f, f': x \to y$ in $C$, apply $G$ to obtain $Gf, Gf': Gx \to Gy$ in $D$. Since $D$ has equalizers, take the equalizer $t: s \to Gx$ of $Gf, Gf'$ in $D$. Then apply the right-adjoint-right-inverse $L$ to the object $t$ in the slice category $(D \downarrow Gx)$. The universal property of the adjunction

$$\hom_{(C \downarrow x)}(Lt, f) \cong \hom_{(D \downarrow Gx)}(t, Gf)$$

shows that $Lt: Ls \to x$ is an equalizer of $f, f'$ in $C$.
