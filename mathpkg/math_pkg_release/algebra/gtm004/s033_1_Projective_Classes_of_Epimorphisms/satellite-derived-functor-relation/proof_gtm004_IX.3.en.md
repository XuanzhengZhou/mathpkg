---
role: proof
locale: en
of_concept: satellite-derived-functor-relation
source_book: gtm004
source_chapter: "IX. Relative Homological Algebra"
source_section: "3. E-Satellites"
---

# Proof of Satellite-Derived Functor Relation for E-Exact Functors

**Corollary 3.4.** If $H : \mathfrak{A} \to \mathfrak{B}$ is an additive functor, then

$$S_j^{\mathcal{E}}(L_0 H) = L_j^{\mathcal{E}} H, \quad j \geq 0.$$

**Proof.** The functor $L_0 H$ is right $\mathcal{E}$-exact by construction (it is the $0$-th left $\mathcal{E}$-derived functor, and the sequence $L_0 H(P) \to L_0 H(A) \to 0$ is exact for any $\mathcal{E}$-projective presentation $P \to A \to 0$). Applying Theorem 3.2 to the right $\mathcal{E}$-exact functor $L_0 H$, we obtain

$$S_j^{\mathcal{E}}(L_0 H) = L_j^{\mathcal{E}}(L_0 H).$$

Now observe that for any $\mathcal{E}$-projective object $P$, we have $L_0 H(P) = H(P)$, since the $\mathcal{E}$-projective presentation of $P$ is simply $0 \to 0 \to P \xrightarrow{1} P \to 0$, so $L_0 H(P) = H(P)$. Consequently, $\mathcal{E}$-projective resolutions compute the same derived functors whether the base functor is $H$ or $L_0 H$. More precisely, if $P_* \to A$ is an $\mathcal{E}$-projective resolution, then

$$L_j^{\mathcal{E}}(L_0 H)(A) = H_j((L_0 H)(P_*)) = H_j(H(P_*)) = L_j^{\mathcal{E}} H(A),$$

since $L_0 H(P_n) = H(P_n)$ for each $\mathcal{E}$-projective $P_n$. Hence $L_j^{\mathcal{E}}(L_0 H) = L_j^{\mathcal{E}} H$, and the result follows. $\square$
