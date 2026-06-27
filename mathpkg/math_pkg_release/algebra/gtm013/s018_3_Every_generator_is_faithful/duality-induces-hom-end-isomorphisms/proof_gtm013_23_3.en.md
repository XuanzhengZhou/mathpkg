---
role: proof
locale: en
of_concept: duality-induces-hom-end-isomorphisms
source_book: gtm013
source_chapter: "23"
source_section: "23.3"
---
The proof is dual to that of (21.2) and (21.3). Since $(H', H'')$ is a duality with natural isomorphisms $\eta: H''H' \to 1$ and $\zeta: H'H'' \to 1$, for any $f: M_1 \to M_2$ in ${}_R \mathcal{C}$, the map $H'(f): H'(M_2) \to H'(M_1)$ is the image under the contravariant functor $H'$. The inverse is given by conjugating with $\eta$: for $g \in \operatorname{Hom}_S(H'(M_2), H'(M_1))$, the corresponding morphism in $\operatorname{Hom}_R(M_1, M_2)$ is $\eta_{M_2} \circ H''(g) \circ \eta_{M_1}^{-1}$. This establishes the abelian group isomorphisms on Hom-sets. Specializing to $M_1 = M_2 = M$ yields the ring isomorphism on endomorphism rings, after accounting for the contravariance: viewing domain morphisms as right operators and codomain morphisms as left operators straightens the order $H'(fg) = H'(g)H'(f)$ into a proper ring homomorphism $\operatorname{End}({}_R M) \to \operatorname{End}(H'(M)_S)$.
