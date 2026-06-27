---
role: proof
locale: en
of_concept: abstract-curve-is-projective
source_book: gtm052
source_chapter: "I"
source_section: "6"
---

**Proof.** The idea of the proof is this: we first cover $C = C_K$ with open subsets $U_i$ which are isomorphic to nonsingular affine curves. Let $Y_i$ be the projective closure of this affine curve. Then we consider the product $Y = \prod Y_i$ and the diagonal map $\varphi: C \to Y$ defined by the morphisms $C \to Y_i$. By considering the induced maps on local rings, one shows that $\varphi$ is a closed immersion (in fact an isomorphism onto its image). Specifically, for each $P \in C$, the induced map $\varphi_P^*: \mathcal{O}_{\varphi(P), Y} \to \mathcal{O}_{P, C}$ on local rings is an isomorphism. Since $\varphi$ is injective (distinct points correspond to distinct subrings of $K$ by (6.4)) and surjective (any point of $Y$ is dominated by some DVR of $K/k$, which must be some $R_P$), $\varphi$ is a bijective morphism with isomorphisms on all local rings, hence an isomorphism by Exercise 3.3(b).
