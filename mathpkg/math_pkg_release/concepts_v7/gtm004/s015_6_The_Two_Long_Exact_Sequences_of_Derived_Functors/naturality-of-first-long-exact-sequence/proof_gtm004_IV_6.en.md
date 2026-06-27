---
role: proof
locale: en
of_concept: naturality-of-first-long-exact-sequence
source_book: gtm004
source_chapter: "IV"
source_section: "6"
---

# Proof of the Naturality of the First Long Exact Sequence

The naturality of the first long exact sequence (6.1) must be verified in two respects: with respect to a natural transformation $\tau : T \rightarrow T'$ of the functor, and with respect to a morphism of short exact sequences.

**Naturality in $T$.** Let $\tau : T \rightarrow T'$ be a natural transformation between additive covariant functors $T, T' : \mathfrak{M}_A \rightarrow \mathfrak{Ub}$. For the projective resolutions $P'$, $P$, $P''$ constructed in the proof of Theorem 6.1, the natural transformation $\tau$ induces chain maps

$$
\tau_{P'} : T P' \rightarrow T' P', \quad \tau_P : T P \rightarrow T' P, \quad \tau_{P''} : T P'' \rightarrow T' P''
$$

defined componentwise by $(\tau_P)_n = \tau_{P_n} : T P_n \rightarrow T' P_n$. These chain maps are compatible with the morphisms in the short exact sequence of complexes $0 \rightarrow P' \rightarrow P \rightarrow P'' \rightarrow 0$, yielding a commutative diagram of chain complexes:

$$
\begin{CD}
0 @>>> T P' @>>> T P @>>> T P'' @>>> 0 \\
@. @V{\tau_{P'}}VV @V{\tau_P}VV @V{\tau_{P''}}VV @. \\
0 @>>> T' P' @>>> T' P @>>> T' P'' @>>> 0
\end{CD}
$$

The naturality of the long exact homology sequence (Theorem IV.2.1) with respect to chain maps then guarantees that the induced maps on homology — which are precisely the induced maps on derived functors $\tau_A : L_n T A \rightarrow L_n T' A$ — commute with all maps in the long exact sequence, including the connecting homomorphisms $\omega_n$. This yields the first commutative diagram of Proposition 6.2.

**Naturality in the short exact sequence.** Let

$$
\begin{CD}
A' @>{\alpha'}>> A @>{\alpha''}>> A'' \\
@V{\varphi'}VV @V{\varphi}VV @V{\varphi''}VV \\
B' @>{\beta'}>> B @>{\beta''}>> B''
\end{CD}
$$

be a commutative diagram with short exact rows. By Lemma III.5.4, we can construct projective resolutions $P'_A$, $P_A$, $P''_A$ for $A'$, $A$, $A''$ and $P'_B$, $P_B$, $P''_B$ for $B'$, $B$, $B''$ together with chain maps lifting $\varphi', \varphi, \varphi''$, such that the following diagram of chain complexes commutes and has exact rows:

$$
\begin{CD}
0 @>>> P'_A @>>> P_A @>>> P''_A @>>> 0 \\
@. @VVV @VVV @VVV @. \\
0 @>>> P'_B @>>> P_B @>>> P''_B @>>> 0
\end{CD}
$$

Applying the functor $T$ and taking homology, the naturality of the long exact homology sequence again yields the commutativity of the ladder diagram in Proposition 6.2, i.e., the induced maps $(L_n T \varphi', L_n T \varphi, L_n T \varphi'')$ commute with the long exact sequences for the two short exact sequences.
