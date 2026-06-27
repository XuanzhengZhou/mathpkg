---
role: proof
locale: en
of_concept: first-long-exact-sequence-of-derived-functors
source_book: gtm004
source_chapter: "IV"
source_section: "6"
---

# Proof of the First Long Exact Sequence of Derived Functors

By Lemma III.5.4 we can construct a commutative diagram with exact rows

$$
\begin{CD}
0 @>>> \ker \varepsilon' @>>> \ker \varepsilon @>>> \ker \varepsilon'' @>>> 0 \\
@VVV @VVV @VVV \\
P'_0 @>>> P_0 @>>> P''_0 @>>> 0 \\
@V\varepsilon'VV @V\varepsilon VV @V\varepsilon''VV \\
A' @>>{\alpha'}> A @>>{\alpha''}> A'' @>>> 0
\end{CD}
$$

where $P'_0$, $P_0$, $P''_0$ are projective objects, $\varepsilon', \varepsilon, \varepsilon''$ are epimorphisms, and the middle row is split exact with $P_0 \cong P'_0 \oplus P''_0$. By Lemma III.5.1, the induced sequence of kernels

$$
\ker \varepsilon' \xrightarrow{\;\alpha'\;} \ker \varepsilon \xrightarrow{\;\alpha''\;} \ker \varepsilon''
$$

is short exact.

Repeating this construction with the short exact sequence $\ker \varepsilon' \rightarrowtail \ker \varepsilon \twoheadrightarrow \ker \varepsilon''$ in place of $A' \rightarrowtail A \twoheadrightarrow A''$, and proceeding inductively, we construct projective resolutions $P'$, $P$, $P''$ of $A'$, $A$, $A''$ respectively, together with an exact sequence of chain complexes

$$
0 \longrightarrow P' \xrightarrow{\;\alpha'\;} P \xrightarrow{\;\alpha''\;} P'' \longrightarrow 0.
$$

Now apply the additive functor $T$ to this short exact sequence of complexes. Since each $P'_n$, $P_n$, $P''_n$ is projective (hence a direct summand), the sequence

$$
0 \longrightarrow T P' \xrightarrow{T\alpha'} T P \xrightarrow{T\alpha''} T P'' \longrightarrow 0
$$

is also short exact.

The long exact homology sequence (Theorem IV.2.1) applied to this short exact sequence of chain complexes yields connecting homomorphisms

$$
\omega_n : H_n(T P'') \longrightarrow H_{n-1}(T P'), \qquad n = 1, 2, \ldots
$$

and the long exact sequence

$$
\cdots \longrightarrow H_n(T P') \xrightarrow{H_n(T\alpha')} H_n(T P) \xrightarrow{H_n(T\alpha'')} H_n(T P'') \xrightarrow{\omega_n} H_{n-1}(T P') \longrightarrow \cdots
$$

By definition, $L_n T A = H_n(T P)$ for any projective resolution $P$ of $A$, and similarly for $A'$ and $A''$. Hence we obtain the first long exact sequence of derived functors:

$$
\cdots \longrightarrow L_n T A' \xrightarrow{L_n T \alpha'} L_n T A \xrightarrow{L_n T \alpha''} L_n T A'' \xrightarrow{\omega_n} L_{n-1} T A' \longrightarrow \cdots
$$

terminating at

$$
\cdots \longrightarrow L_1 T A'' \xrightarrow{\omega_1} L_0 T A' \xrightarrow{L_0 T \alpha'} L_0 T A \xrightarrow{L_0 T \alpha''} L_0 T A'' \longrightarrow 0.
$$
