---
role: proof
locale: en
of_concept: proposition-e-connected-sequence-differential
source_book: gtm004
source_chapter: "IX"
source_section: "3. Satellites"
---

# Proof of $\mathcal{E}$-Connected Sequence Yields Differential Sequence

**Proposition 3.1.** If $T = \{T_j, \omega_j\}$ is an $\mathcal{E}$-connected sequence of functors, then the sequence

$$\cdots \to T_j(A') \to T_j(A) \to T_j(A'') \xrightarrow{\omega_j} T_{j-1}(A') \to T_{j-1}(A) \to \cdots$$

is differential for each short $\mathcal{E}$-exact sequence $0 \to A' \to A \to A'' \to 0$ in $\mathfrak{U}$.

**Proof.** (1) Differentiality at $T_j(A)$ is immediate since $T_j(A' \to A \to A'') = 0$.

(2) At $T_j(A'')$: Consider the morphism from the trivial $\mathcal{E}$-exact sequence $0 \to 0 \to A \xrightarrow{1} A \to 0$ to the given one $0 \to A' \to A \to A'' \to 0$. The connecting homomorphism $T_j(A) \to T_{j-1}(0)$ in the trivial sequence vanishes. By naturality, $\omega_j \circ T_j(A \to A'') = T_{j-1}(0 \to A') \circ 0 = 0$.

(3) At $T_{j-1}(A')$: Consider the morphism from the given sequence to the trivial $\mathcal{E}$-exact sequence $0 \to A \xrightarrow{1} A \to 0 \to 0$. The connecting homomorphism $T_j(0) \to T_{j-1}(A)$ vanishes. By naturality, $T_{j-1}(A' \to A) \circ \omega_j = 0 \circ T_j(A'' \to 0) = 0$.

Thus the composite of any two consecutive morphisms is zero, establishing that the sequence is differential.
