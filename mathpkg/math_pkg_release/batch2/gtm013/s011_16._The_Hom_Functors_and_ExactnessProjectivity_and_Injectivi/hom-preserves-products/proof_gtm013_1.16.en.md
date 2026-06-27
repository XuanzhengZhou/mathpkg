---
role: proof
locale: en
of_concept: hom-preserves-products
source_book: gtm013
source_chapter: "1"
source_section: "§16. The Hom Functors and Exactness—Projectivity and Injectivity"
---

(1) is left as an exercise. For (2), let $(\pi_\alpha)_{\alpha \in A}$ be the projections associated with the product of the $Hom_R(M_\alpha, U_S)$. Define $\eta: Hom_R(M, U_S) \to \prod_A Hom_R(M_\alpha, U_S)$ by $\eta(\gamma) = (\gamma j_\alpha)_{\alpha \in A}$. For each $\alpha$, $\pi_\alpha \eta = Hom_R(j_\alpha, U_S)$. Now, if $(\gamma_\alpha) \in \prod_A Hom_R(M_\alpha, U_S)$, define $\gamma: M \to U_S$ by $\gamma(\sum m_\alpha) = \sum \gamma_\alpha(m_\alpha)$ (the sum is finite since $M = \bigoplus M_\alpha$). Then $\eta(\gamma) = (\gamma_\alpha)$, showing $\eta$ is surjective. If $\eta(\gamma) = 0$, then $\gamma j_\alpha = 0$ for all $\alpha$, so $\gamma = 0$, showing $\eta$ is injective. Thus $\eta$ is an isomorphism and the proof is complete.
