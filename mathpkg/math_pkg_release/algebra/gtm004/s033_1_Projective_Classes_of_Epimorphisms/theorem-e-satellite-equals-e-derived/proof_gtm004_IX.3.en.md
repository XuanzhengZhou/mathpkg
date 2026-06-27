---
role: proof
locale: en
of_concept: theorem-e-satellite-equals-e-derived
source_book: gtm004
source_chapter: "IX"
source_section: "3. Satellites"
---

# Proof of Left $\mathcal{E}$-Satellite Equals Left $\mathcal{E}$-Derived Functor

**Theorem 3.2.** If $H : \mathfrak{A} \to \mathfrak{B}$ is right $\mathfrak{E}$-exact and $\mathfrak{E}$ is a projective class of epimorphisms in $\mathfrak{A}$, then $L_j^{\mathfrak{E}} H = S_j^{\mathfrak{E}} H$ for all $j \geq 0$ (and $L_j^{\mathfrak{E}} H = 0$ for $j < 0$).

**Proof.** By right $\mathfrak{E}$-exactness, $H = L_0 H$. Given an $\mathfrak{E}$-connected sequence $T$ and $\varphi : T_0 \to L_0 H$, we construct $\varphi_j$ by induction. For the inductive step, given $A$ with an $\mathfrak{E}$-projective presentation $0 \to K \to P \to A \to 0$, the map $\omega_j : L_j H(A) \to L_{j-1} H(K)$ is monic (since $L_j H(P) = 0$). Define $\varphi_j(A)$ as the unique morphism satisfying $\omega_j \circ \varphi_j(A) = \varphi_{j-1}(K) \circ \omega_j$. A lemma establishes naturality: embed the naturality square in a cube where all other faces commute and the connecting morphism is monic, forcing the remaining face to commute. The compatibility with connecting homomorphisms is verified by composing the definition square with the naturality square for $\varphi_j$, using a morphism from a projective presentation to the short exact sequence. Uniqueness follows because if $\psi_j$ also satisfies the conditions, then $\omega_j \circ (\varphi_j - \psi_j) = 0$ on all objects, and since $\omega_j$ is monic on values of $L_j H$, we get $\varphi_j = \psi_j$.
