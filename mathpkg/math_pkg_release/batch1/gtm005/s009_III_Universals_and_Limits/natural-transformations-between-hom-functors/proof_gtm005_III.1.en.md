---
role: proof
locale: en
of_concept: natural-transformations-between-hom-functors
source_book: gtm005
source_chapter: "III"
source_section: "1"
---

Given functors $F: D \to C$ and $G: C \to D$, a natural isomorphism
$$\varphi: C(F-, -) \cong D(-, G-)$$
(of bifunctors $D^{\mathrm{op}} \times C \to \mathbf{Set}$) is precisely an adjunction $F \dashv G$.

The proof: A natural family of bijections $\varphi_{d,c}: C(F(d), c) \cong D(d, G(c))$ must be natural in both variables. Naturality in $d$ means: for $f: d' \to d$, the diagram
$$\begin{CD} C(F(d), c) @>{\varphi_{d,c}}>> D(d, G(c)) \\ @V{C(F(f), 1)}VV @VV{D(f, 1)}V \\ C(F(d'), c) @>>{\varphi_{d',c}}> D(d', G(c)) \end{CD}$$
commutes. Naturality in $c$ is similar. These two naturality conditions correspond exactly to the naturality of the unit and counit of the adjunction, or equivalently to the hom-set definition of an adjunction being a natural isomorphism of bifunctors.
