---
role: proof
locale: en
of_concept: theorem-long-exact-sequence-e-derived
source_book: gtm004
source_chapter: "IX"
source_section: "2. $\mathcal{E}$-Derived Functors"
---

# Proof of Long Exact Sequence of $\mathcal{E}$-Derived Functors

**Theorem 2.1.** Let $\mathfrak{A}$, $\mathfrak{B}$ be abelian categories, let $T : \mathfrak{A} \to \mathfrak{B}$ be an additive functor, and let $\mathcal{E}$ be a projective class of epimorphisms in $\mathfrak{A}$. For each short $\mathcal{E}$-exact sequence

$$0 \to A' \xrightarrow{\alpha'} A \xrightarrow{\alpha''} A'' \to 0$$

in $\mathfrak{A}$, there exist connecting homomorphisms

$$\omega_n : L_n^{\mathcal{E}} T(A'') \to L_{n-1}^{\mathcal{E}} T(A'), \quad n \geq 1,$$

such that the sequence

$$\cdots \to L_n^{\mathcal{E}} T(A') \to L_n^{\mathcal{E}} T(A) \to L_n^{\mathcal{E}} T(A'') \xrightarrow{\omega_n} L_{n-1}^{\mathcal{E}} T(A') \to \cdots$$

$$\cdots \to L_0^{\mathcal{E}} T(A') \to L_0^{\mathcal{E}} T(A) \to L_0^{\mathcal{E}} T(A'') \to 0$$

is exact and natural in the short $\mathcal{E}$-exact sequence.

**Proof.** The theorem is derived from Lemma 2.2, which provides an embedding of the given short $\mathcal{E}$-exact sequence into a diagram

$$
\begin{array}{cccccc}
K' & \xrightarrow{\kappa'} & K & \xrightarrow{\kappa''} & K'' \\
\downarrow & & \downarrow & & \downarrow \\
P' & \xrightarrow{\lambda'} & P & \xrightarrow{\lambda''} & P'' \\
\downarrow & & \downarrow & & \downarrow \\
A' & \xrightarrow{\alpha'} & A & \xrightarrow{\alpha''} & A''
\end{array}
$$

with all rows and columns $\mathcal{E}$-exact and $P', P, P''$ $\mathcal{E}$-projective. Here $P = P' \oplus P''$, $\lambda'$ is the injection, and $\lambda''$ the projection.

Apply the functor $T$ to the $\mathcal{E}$-projective resolutions of $A'$, $A$, and $A''$ given by the columns of this diagram. The top row yields a short exact sequence of $\mathcal{E}$-projective resolutions (after applying the appropriate truncations), which gives rise to a short exact sequence of chain complexes. Applying $T$ and taking homology yields the long exact sequence of $\mathcal{E}$-derived functors by the standard homological algebra argument (the snake lemma applied to the short exact sequence of complexes).

The connecting homomorphism $\omega_n$ is defined at the chain level by the usual diagram chase: given $x \in L_n^{\mathcal{E}} T(A'')$, represent it by a cycle in $T(P_n'')$, lift to $T(P_n)$, apply the differential, and descend to a cycle in $T(P_{n-1}')$.

Naturality follows from the naturality of the embedding diagram constructed in Lemma 2.2 with respect to morphisms of short $\mathcal{E}$-exact sequences, together with the functoriality of the $\mathcal{E}$-projective resolution construction.

(In the text, the reader is told: "The reader should now have no difficulty in deriving Theorem 2.1 from Lemma 2.2." The derivation is the same as the absolute case in Chapter IV, adapted to the relative $\mathcal{E}$-projective setting.)
