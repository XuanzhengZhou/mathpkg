---
role: proof
locale: en
of_concept: natural-transformations-from-bimodule-homomorphism
source_book: gtm013
source_chapter: "20"
source_section: "20.5"
---

We prove (1). Because $\operatorname{Hom}_R(-, M): {}_R\mathcal{M} \to {}_{\mathbb{Z}}\mathcal{M}$ is a contravariant additive functor, Lemma (20.4.1) implies that $\eta_M = \operatorname{Hom}_R(\theta, M)$ is a left $S$-homomorphism.

Now check naturality in $M$: for each $f: {}_R M \to {}_R M'$, we need the following diagram to commute:

$$\begin{CD}
\operatorname{Hom}_R(V, M) @>{\operatorname{Hom}_R(V, f)}>> \operatorname{Hom}_R(V, M')\\
@V{\eta_M}VV @VV{\eta_{M'}}V\\
\operatorname{Hom}_R(U, M) @>{\operatorname{Hom}_R(U, f)}>> \operatorname{Hom}_R(U, M')
\end{CD}$$

For $\gamma \in \operatorname{Hom}_R(V, M)$:

$$\operatorname{Hom}_R(U, f)(\eta_M(\gamma)) = f \circ (\gamma \circ \theta) = (f \circ \gamma) \circ \theta = \eta_{M'}(\operatorname{Hom}_R(V, f)(\gamma)).$$

Thus the square commutes, so $\eta$ is a natural transformation.

The proofs of (2) and (3) are analogous, using the covariance/contravariance of the respective functors. For the last statement: if $\theta$ is an isomorphism with inverse $\theta^{-1}$, then the induced transformations have inverses given by the transformations induced by $\theta^{-1}$.
