---
role: proof
locale: en
of_concept: naturality-of-second-long-exact-sequence
source_book: gtm004
source_chapter: "IV"
source_section: "6"
---

# Proof of the Naturality of the Second Long Exact Sequence

The naturality of the second long exact sequence (6.3) must be established in two respects: with respect to a morphism $\alpha : A \rightarrow A'$ of objects, and with respect to a morphism of short exact sequences of functors.

**Naturality in the object $A$.** Let $\alpha : A \rightarrow A'$ be a homomorphism of $A$-modules, and let $T' \xrightarrow{\tau'} T \xrightarrow{\tau''} T''$ be a short exact sequence of additive functors that is exact on projectives. Choose projective resolutions $P$ of $A$ and $P'$ of $A'$. By the comparison theorem (Lemma III.6.1), the morphism $\alpha$ lifts to a chain map $\bar{\alpha} : P \rightarrow P'$, unique up to chain homotopy. This chain map induces, for each functor in the short exact sequence, a commutative diagram of chain complexes:

$$
\begin{CD}
0 @>>> T' P @>{\tau'_P}>> T P @>{\tau''_P}>> T'' P @>>> 0 \\
@. @V{T'\bar{\alpha}}VV @V{T\bar{\alpha}}VV @V{T''\bar{\alpha}}VV @. \\
0 @>>> T' P' @>{\tau'_{P'}}>> T P' @>{\tau''_{P'}}>> T'' P' @>>> 0
\end{CD}
$$

The naturality of the long exact homology sequence with respect to chain maps then guarantees that the induced maps on homology — which are precisely $\alpha_* : L_n T A \rightarrow L_n T A'$ for each derived functor — commute with all maps in the long exact sequence (6.3), including the connecting homomorphisms $\omega_n$. The commutativity of the first diagram in Proposition 6.4 follows.

**Naturality in the sequence of functors.** Let

$$
\begin{CD}
T' @>{\tau'}>> T @>{\tau''}>> T'' \\
@V{\varphi'}VV @V{\varphi}VV @V{\varphi''}VV \\
S' @>{\sigma'}>> S @>{\sigma''}>> S''
\end{CD}
$$

be a commutative diagram of additive functors and natural transformations such that both rows are exact on projectives. For a fixed object $A$ with projective resolution $P$, evaluating this diagram on each $P_n$ yields, for each $n \ge 0$, a commutative diagram with exact rows:

$$
\begin{CD}
0 @>>> T' P_n @>{\tau'}>> T P_n @>{\tau''}>> T'' P_n @>>> 0 \\
@. @V{\varphi'}VV @V{\varphi}VV @V{\varphi''}VV @. \\
0 @>>> S' P_n @>{\sigma'}>> S P_n @>{\sigma''}>> S'' P_n @>>> 0
\end{CD}
$$

Assembling these across all $n$ yields a commutative diagram of short exact sequences of chain complexes. Applying the naturality of the long exact homology sequence, the induced maps on homology — which are the natural transformations $L_n \varphi'$, $L_n \varphi$, $L_n \varphi''$ between the derived functors — commute with the connecting homomorphisms and all maps in the long exact sequence (6.3). This establishes the commutativity of the second diagram in Proposition 6.4.
