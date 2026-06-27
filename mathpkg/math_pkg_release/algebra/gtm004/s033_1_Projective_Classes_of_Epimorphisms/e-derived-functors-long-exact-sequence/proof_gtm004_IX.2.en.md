---
role: proof
locale: en
of_concept: e-derived-functors-long-exact-sequence
source_book: gtm004
source_chapter: "IX. Relative Homological Algebra"
source_section: "2. E-Derived Functors"
---

# Proof of Long Exact Sequence of E-Derived Functors

**Theorem 2.3.** Let $0 \to T' \to T \to T'' \to 0$ be a sequence of additive functors $\mathfrak{A} \to \mathfrak{B}$ which is $\mathcal{E}$-exact on $\mathcal{E}$-projectives. Then, for any object $A$ in $\mathfrak{A}$, there exist connecting homomorphisms

$$\omega_n : L_n^{\mathcal{E}} T''(A) \to L_{n-1}^{\mathcal{E}} T'(A)$$

such that the sequence

$$\cdots \to L_n T'(A) \to L_n T(A) \to L_n T''(A) \xrightarrow{\omega_n} L_{n-1} T'(A) \to \cdots$$

$$\cdots \to L_0 T'(A) \to L_0 T(A) \to L_0 T''(A) \to 0$$

is exact.

**Proof.** Choose an $\mathcal{E}$-projective resolution $P_* \to A$ of $A$. The hypothesis that $0 \to T' \to T \to T'' \to 0$ is $\mathcal{E}$-exact on $\mathcal{E}$-projectives implies that applying these functors to each term $P_n$ yields a short exact sequence of chain complexes

$$0 \to T'(P_*) \to T(P_*) \to T''(P_*) \to 0.$$

(The exactness holds termwise because each $P_n$ is $\mathcal{E}$-projective.) The long exact homology sequence of this short exact sequence of chain complexes yields the desired long exact sequence of derived functors, with $L_n^{\mathcal{E}} T(A) = H_n(T(P_*))$.

The connecting homomorphism $\omega_n$ is the standard homology connecting homomorphism from the snake lemma applied to the short exact sequence of chain complexes. Naturality in $A$ follows from the fact that a morphism $A \to B$ lifts to a morphism of $\mathcal{E}$-projective resolutions, and all constructions are natural with respect to such liftings.
