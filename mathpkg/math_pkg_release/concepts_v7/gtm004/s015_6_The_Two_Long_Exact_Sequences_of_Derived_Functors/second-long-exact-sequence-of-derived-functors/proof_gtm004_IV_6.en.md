---
role: proof
locale: en
of_concept: second-long-exact-sequence-of-derived-functors
source_book: gtm004
source_chapter: "IV"
source_section: "6"
---

# Proof of the Second Long Exact Sequence of Derived Functors

Let $T' \xrightarrow{\tau'} T \xrightarrow{\tau''} T''$ be a short exact sequence of additive covariant functors $\mathfrak{M}_A \rightarrow \mathfrak{Ub}$ that is exact on projectives. Choose a projective resolution $P$ of $A$ and consider the induced sequence of chain complexes

$$
0 \longrightarrow T' P \xrightarrow{\;\tau'_P\;} T P \xrightarrow{\;\tau''_P\;} T'' P \longrightarrow 0.
$$

Since the sequence $T' \rightarrow T \rightarrow T''$ is exact on projectives and each $P_n$ is projective, the sequence

$$
0 \longrightarrow T' P_n \xrightarrow{\tau'} T P_n \xrightarrow{\tau''} T'' P_n \longrightarrow 0
$$

is exact for every $n \ge 0$. Hence the sequence of chain complexes is short exact.

Applying the long exact homology sequence (Theorem IV.2.1) to this short exact sequence of chain complexes, we obtain connecting homomorphisms

$$
\omega_n : H_n(T'' P) \longrightarrow H_{n-1}(T' P), \qquad n = 1, 2, \ldots
$$

and the long exact sequence

$$
\cdots \longrightarrow H_n(T' P) \xrightarrow{H_n(\tau'_P)} H_n(T P) \xrightarrow{H_n(\tau''_P)} H_n(T'' P) \xrightarrow{\omega_n} H_{n-1}(T' P) \longrightarrow \cdots
$$

By definition of the left derived functors, $H_n(T' P) = L_n T' A$, $H_n(T P) = L_n T A$, and $H_n(T'' P) = L_n T'' A$. The induced maps on homology are precisely the induced maps on derived functors: $L_n \tau'_A$ and $L_n \tau''_A$. Thus we obtain the second long exact sequence of derived functors:

$$
\cdots \longrightarrow L_n T' A \xrightarrow{L_n \tau'_A} L_n T A \xrightarrow{L_n \tau''_A} L_n T'' A \xrightarrow{\omega_n} L_{n-1} T' A \longrightarrow \cdots
$$

terminating at

$$
\cdots \longrightarrow L_1 T'' A \xrightarrow{\omega_1} L_0 T' A \xrightarrow{L_0 \tau'_A} L_0 T A \xrightarrow{L_0 \tau''_A} L_0 T'' A \longrightarrow 0.
$$
