---
role: proof
locale: en
of_concept: equivalence-hom-isomorphism
source_book: gtm013
source_chapter: "6"
source_section: "21"
---

Since $F$ is additive, these restrictions are abelian group homomorphisms. The latter is a ring homomorphism by (20.3). To finish the proof we adopt the notation of (21.1). Then for each $M$ and $M'$ in ${}_R \mathbf{M}$,

$$H: \operatorname{Hom}_S(F(M), F(M')) \to \operatorname{Hom}_R(M, M')$$

defined by

$$H: g \mapsto \eta_{M'} \circ G(g) \circ \eta_M^{-1}$$

is a $\mathbb{Z}$-homomorphism. Moreover, it is monic, for if $H(g) = 0$, then $G(g) = 0$ (since $\eta_{M'}$ and $\eta_M^{-1}$ are isomorphisms). But $G$ is an equivalence, so $G(g) = 0$ implies $g = 0$ by applying $F$ and using the natural isomorphism $FG \cong 1$.

To see that $H$ is an inverse to $F$, compute for $f \in \operatorname{Hom}_R(M, M')$:

$$H(F(f)) = \eta_{M'} \circ G(F(f)) \circ \eta_M^{-1} = \eta_{M'} \circ GF(f) \circ \eta_M^{-1}.$$

By naturality of $\eta$, we have $\eta_{M'} \circ GF(f) = f \circ \eta_M$, so $H(F(f)) = f \circ \eta_M \circ \eta_M^{-1} = f$. Similarly, $F(H(g)) = g$ for $g \in \operatorname{Hom}_S(F(M), F(M'))$, using the natural isomorphism $\zeta$.

For the preservation of epimorphisms and monomorphisms: $f$ is monic iff $\operatorname{Hom}_R(X, M) \to \operatorname{Hom}_R(X, M')$ is injective for all $X$. Since $F$ is bijective on Hom sets (as just proved), and $G$ is also an equivalence, the corresponding property for $F(f)$ follows by applying $F$ and $G$ appropriately. The same reasoning applies to epimorphisms.

The endomorphism ring statement follows since $\operatorname{End}({}_R M) = \operatorname{Hom}_R(M, M)$ and the restriction of $F$ to this set is a ring homomorphism by (20.3) and bijective by the above.
