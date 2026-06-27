---
role: proof
locale: en
of_concept: e-connected-sequence-differential
source_book: gtm004
source_chapter: "IX. Relative Homological Algebra"
source_section: "3. E-Satellites"
---

# Proof of E-Connected Sequence Yields Differential Long Sequence

**Proposition 3.1.** If $T = \{T_j, \omega_j\}$ is an $\mathcal{E}$-connected sequence of functors, then for each short $\mathcal{E}$-exact sequence

$$0 \to A' \to A \to A'' \to 0$$

in $\mathfrak{U}$, the sequence

$$\cdots \to T_j(A') \to T_j(A) \to T_j(A'') \xrightarrow{\omega_j} T_{j-1}(A') \to T_{j-1}(A) \to \cdots$$

is differential (i.e., the composite of any two consecutive morphisms vanishes).

**Proof.** By definition of an $\mathcal{E}$-connected sequence of functors, the connecting homomorphisms $\omega_j : T_j(A'') \to T_{j-1}(A')$ are natural with respect to morphisms of short $\mathcal{E}$-exact sequences.

The sequence is certainly differential at $T_j(A)$: the composite $T_j(A') \to T_j(A) \to T_j(A'')$ vanishes because it is $T_j$ applied to the composite $A' \to A \to A''$, which is zero by exactness of the original sequence.

To prove differentiality at $T_j(A'')$, i.e., that the composite

$$T_j(A) \to T_j(A'') \xrightarrow{\omega_j} T_{j-1}(A')$$

vanishes, we use naturality of $\omega_j$ applied to the morphism of short $\mathcal{E}$-exact sequences

$$
\begin{array}{cccccc}
0 & \to & 0 & \to & A & \to & A & \to & 0 \\
& & \downarrow & & \downarrow & & \parallel \\
0 & \to & A' & \to & A & \to & A'' & \to & 0.
\end{array}
$$

Since the top row comes from a split (hence $\mathcal{E}$-exact) sequence where one term is zero, the connecting homomorphism for the top row is necessarily zero. Naturality forces the composite $T_j(A) \to T_j(A'') \xrightarrow{\omega_j} T_{j-1}(A')$ to factor through the zero connecting homomorphism, hence itself vanishes.

To prove differentiality at $T_{j-1}(A')$, i.e., that the composite

$$T_j(A'') \xrightarrow{\omega_j} T_{j-1}(A') \to T_{j-1}(A)$$

vanishes, we use naturality applied to the morphism

$$
\begin{array}{cccccc}
0 & \to & A' & \to & A & \to & A'' & \to & 0 \\
& & \parallel & & \downarrow & & \downarrow \\
0 & \to & A & \to & A & \to & 0 & \to & 0.
\end{array}
$$

The bottom row has zero connecting homomorphism (since the right term vanishes). Naturality forces the composite $T_j(A'') \xrightarrow{\omega_j} T_{j-1}(A') \to T_{j-1}(A)$ to factor through zero, hence vanishes. $\square$
