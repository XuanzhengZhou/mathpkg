---
role: proof
locale: en
of_concept: kunneth-theorem
source_book: gtm004
source_chapter: "V. Double Complexes"
source_section: "2. The Künneth Theorem"
---

# Proof of the Künneth Theorem

**Theorem 2.1.** Let $\Lambda$ be a principal ideal domain. Let $C$, $D$ be chain complexes over $\Lambda$, and let $C$ be flat. Then there is a natural short exact sequence

$$0 \to \bigoplus_{p+q=n} H_p(C) \otimes_\Lambda H_q(D) \xrightarrow{\zeta} H_n(C \otimes_\Lambda D) \xrightarrow{\omega} \bigoplus_{p+q=n-1} \operatorname{Tor}_1^\Lambda(H_p(C), H_q(D)) \to 0,$$

where $\zeta$ is induced by the inclusion $Z_p(C) \otimes_\Lambda Z_q(D) \to Z_{p+q}(C \otimes_\Lambda D)$ of representative cycles. Moreover the sequence splits, but not naturally.

**Proof.** We recall the boundary operator $\partial^{\otimes}$ in $C \otimes_\Lambda D$:
$$\partial^{\otimes}(c \otimes d) = \partial c \otimes d + (-1)^p c \otimes \partial d, \quad c \in C_p, \; d \in D_q.$$

There is a natural isomorphism $C \otimes_\Lambda D \cong D \otimes_\Lambda C$ given by $c \otimes d \mapsto (-1)^{pq} d \otimes c$ ($c \in C_p$, $d \in D_q$), so it suffices to prove the theorem when $C$ is flat.

Introduce the notation:
$$Z_p = Z_p(C), \quad B_p = B_p(C); \qquad \bar{Z}_p = Z_p(D), \quad \bar{B}_p = B_p(D).$$
Regard $Z = \{Z_p\}$, $B = \{B_p\}$ as complexes with trivial differentials. Also set $B'_p = B_{p-1}(C)$ and regard $B' = \{B'_p\}$ with the grading chosen so that $\partial: C \to B'$ is a chain map. Consider the exact sequence of chain complexes
$$0 \to Z \xrightarrow{\iota} C \xrightarrow{\partial} B' \to 0.$$

Since $\Lambda$ is a p.i.d. and $C$ is flat, $Z$, $B$, and $B'$ are flat as well. Tensoring with $D$ yields an exact sequence
$$0 \to Z \otimes_\Lambda D \xrightarrow{\iota \otimes 1} C \otimes_\Lambda D \xrightarrow{\partial \otimes 1} B' \otimes_\Lambda D \to 0,$$
which gives rise to a long exact homology sequence. Identifying terms:

Since $B'$ is flat, the homology of $B' \otimes_\Lambda D$ is computed as:
$$\ker(1 \otimes \partial)_n = (B' \otimes_\Lambda \bar{Z})_n = (B \otimes_\Lambda \bar{Z})_{n-1},$$
$$\operatorname{im}(1 \otimes \partial)_n = (B' \otimes_\Lambda \bar{B})_n = (B \otimes_\Lambda \bar{B})_{n-1},$$
hence
$$H_n(B' \otimes_\Lambda D) = (B \otimes_\Lambda H(D))_{n-1}.$$

Similarly, since $Z$ is flat,
$$H_n(Z \otimes_\Lambda D) = (Z \otimes_\Lambda H(D))_n.$$

The long exact homology sequence becomes
$$\cdots \to Z \otimes_\Lambda H(D) \xrightarrow{(\iota \otimes 1)_*} H(C \otimes_\Lambda D) \xrightarrow{\omega} B \otimes_\Lambda H(D) \xrightarrow{\text{connecting}} \cdots$$

The map $(\iota \otimes 1)_*$ induces $\zeta$ in the statement. To analyze $\omega$, pick a representative $\partial c \otimes z$ of a generator $\partial c \otimes [z]$ of $B \otimes_\Lambda H(D)$. Then $\partial c \otimes z = (\partial \otimes 1)(c \otimes z)$, and $\partial^{\otimes}(c \otimes z) = \partial c \otimes z$, so $\omega(\partial c \otimes [z])$ is measured by the connecting homomorphism from the short exact sequence.

The kernel-cokernel exact sequence from the long exact sequence yields precisely the short exact Künneth sequence (2.1).

**Splitting (when $C$ and $D$ are free).** If $C$ and $D$ are free, we decompose $C_p = Z_p \oplus Y_p$ where $\partial|Y_p: Y_p \xrightarrow{\sim} B_{p-1}$, and similarly $D_q = \bar{Z}_q \oplus \bar{Y}_q$. Define $\kappa_p: C_p \to Z_p$ and $\bar{\kappa}_q: D_q \to \bar{Z}_q$ as the canonical projections. Then $\kappa \otimes \bar{\kappa}: C \otimes_\Lambda D \to Z \otimes_\Lambda \bar{Z}$ maps boundaries to $B \otimes_\Lambda \bar{Z} + Z \otimes_\Lambda \bar{B}$, and induces $\theta: H(C \otimes_\Lambda D) \to H(C) \otimes_\Lambda H(D)$ with $\theta \zeta = 1$. Thus the sequence splits.

**General flat case.** Use Proposition 2.4 (realization of homology) to find free chain complexes $F$, $G$ and chain maps $\varphi: F \to C$, $\psi: G \to D$ inducing isomorphisms on homology. By naturality of (2.1), we have a commutative diagram of exact sequences, and since $\varphi_* \otimes \psi_*$ and $\operatorname{Tor}(\varphi_*, \psi_*)$ are isomorphisms, the five lemma implies $(\varphi \otimes \psi)_*$ is an isomorphism. The top sequence splits (free case), so the bottom sequence splits.

**Non-naturality of splitting.** The splitting cannot be natural: if it were, then specializing to the universal coefficient theorem case would yield a natural splitting of the universal coefficient sequence, which is known to be false (a counterexample can be constructed with $C$ a free resolution of $\mathbb{Z}/2\mathbb{Z}$ and appropriate maps).
