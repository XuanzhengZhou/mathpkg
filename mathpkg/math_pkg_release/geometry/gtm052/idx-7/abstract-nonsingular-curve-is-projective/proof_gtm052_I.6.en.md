---
role: proof
locale: en
of_concept: abstract-nonsingular-curve-is-projective
source_book: gtm052
source_chapter: "I"
source_section: "6"
---
The idea of the proof is this: we first cover $C = C_K$ with open subsets $U_i$ which are isomorphic to nonsingular affine curves. Let $Y_i$ be the projective closure of this affine curve. Then we have a diagram of dominant morphisms, where $\pi$ is the projection map onto the $i$th factor. Thus we have inclusions of local rings

$$\mathcal{O}_{\varphi_i(P), Y_i} \hookrightarrow \mathcal{O}_{\varphi(P), Y} \hookrightarrow \mathcal{O}_{P, C}$$

by (Ex. 3.3). The two outside ones are isomorphic, so the middle one is also. Thus we see that for any $P \in C$, the map $\varphi_P^*: \mathcal{O}_{\varphi(P), Y} \to \mathcal{O}_{P, C}$ is an isomorphism.

Next, let $Q$ be any point of $Y$. Then $\mathcal{O}_Q$ is dominated by some discrete valuation ring $R$ of $K/k$ (take for example a localization of the integral closure of $\mathcal{O}_Q$ at a maximal ideal). But $R = R_P$ for some $P \in C$, and $\mathcal{O}_{\varphi(P)} \cong R$, so by (6.4) we must have $Q = \varphi(P)$. This shows that $\varphi$ is surjective. But $\varphi$ is clearly injective, because distinct points of $C$ correspond to distinct subrings of $K$.

Thus $\varphi$ is a bijective morphism of $C$ to $Y$, and for every $P \in C$, $\varphi_P^*$ is an isomorphism, so by (Ex. 3.3b), $\varphi$ is an isomorphism.
