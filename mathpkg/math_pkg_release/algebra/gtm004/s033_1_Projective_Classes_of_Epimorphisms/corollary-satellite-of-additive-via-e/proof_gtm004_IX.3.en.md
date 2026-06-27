---
role: proof
locale: en
of_concept: corollary-satellite-of-additive-via-e
source_book: gtm004
source_chapter: "IX"
source_section: "3. Satellites"
---

# Proof of Satellite of $L_0$ via $\mathcal{E}$-Derived Functors

**Corollary 3.4.** If $H : \mathfrak{A} \to \mathfrak{B}$ is an additive functor, then

$$S_j^{\mathcal{E}}(L_0 H) = L_j^{\mathcal{E}} H, \quad j \geq 0.$$

**Proof.** $L_0 H$ is right $\mathcal{E}$-exact. By Theorem 3.2, $S_j^{\mathcal{E}}(L_0 H) = L_j^{\mathcal{E}}(L_0 H)$. But $L_0 H(P) = H(P)$ for every $\mathcal{E}$-projective $P$, since an $\mathcal{E}$-projective presentation $0 \to 0 \to P \xrightarrow{1} P \to 0$ yields $L_0 H(P) = \operatorname{coker}(H(0) \to H(P)) = H(P)$. Therefore, if $P_* \to A$ is an $\mathcal{E}$-projective resolution, then $(L_0 H)(P_*) = H(P_*)$ as chain complexes, so their homologies coincide: $L_j^{\mathcal{E}}(L_0 H) = L_j^{\mathcal{E}} H$. $\square$
