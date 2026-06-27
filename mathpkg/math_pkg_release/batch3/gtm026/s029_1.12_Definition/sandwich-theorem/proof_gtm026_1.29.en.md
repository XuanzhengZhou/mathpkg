---
role: proof
locale: en
of_concept: sandwich-theorem
source_book: gtm026
source_chapter: "1"
source_section: "1.29"
---

**Proof.** (1) Since $V$ has a left adjoint, if $U$ has a left adjoint then $W$ has a left adjoint by 2.2.30. In view of this, we need to prove that if $W$ has a left adjoint $F: \mathcal{K} \to \mathcal{A}$, then $U$ has a left adjoint. For an object $K$ of $\mathcal{B}$, let $(KF', K\eta')$ be the free object over $KU$ with respect to $W$. Define $KF$ to be the coequalizer of $a, b: (KTF', K\eta'T)$ where $(T, \eta, \mu)$ is the algebraic theory corresponding to $V$ and $a, b$ are defined using the $\mathbf{T}$-algebra structure of $K$. More explicitly, $KU = (KW, \gamma: KWT \to KW)$ and the two morphisms are defined via the triangular identities and the $\mathbf{T}$-algebra structure.

The key step is: $K\eta' \cdot pW: (K, \xi) \to AU$ is a $\mathbf{T}$-homomorphism if and only if $a \cdot p = b \cdot p$, where $p$ is the canonical map to the coequalizer. This follows because $(KTF', K\eta')$ is free over $KT$ with respect to $W$.

The rest is straightforward: Let $p: KF' \to A = \text{coeq}(a, b)$ in $\mathcal{A}$. Since $a \cdot p = b \cdot p$, $f = K\eta' \cdot pW: (K, \xi) \to AU$ is a $\mathbf{T}$-homomorphism. For any $A'$ in $\mathcal{A}$ and $\mathbf{T}$-homomorphism $f': (K, \xi) \to A'U$, since $(KF', K\eta')$ is free over $K$ with respect to $W$, there exists unique $p': KF' \to A'$ in $\mathcal{A}$ such that $K\eta' \cdot p'W = f'$. Since $f'$ is a $\mathbf{T}$-homomorphism, $a \cdot p' = b \cdot p'$, so since $p = \text{coeq}(a, b)$, there exists a unique $\psi: A \to A'$ in $\mathcal{A}$ such that $p \cdot \psi = p'$. This establishes the adjunction.

(2) If $W$ is algebraic, then by (1), $U$ has a left adjoint. To prove $U$ is algebraic, one must show it creates coequalizers of $U$-absolute pairs, which follows from the algebraicity of $W$ and $V$ via the commutative diagram and the coequalizer-creation properties. The remaining details are based on the same principles as the corresponding parts of (1). $\square$
