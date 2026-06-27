---
role: proof
locale: en
of_concept: left-derived-functors-are-additive
source_book: gtm004
source_chapter: "IV. Derived Functors"
source_section: "5. Derived Functors"
---

# Proof of Additivity of Left Derived Functors

**Proposition 5.4.** The functors $L_n T: \mathfrak{M}_A \rightarrow \mathfrak{Ub}$, $n = 0, 1, \ldots$ are additive.

*Proof.* Let $P$ be a projective resolution of $A$ and $Q$ a projective resolution of $B$, then

$$P \oplus Q: \cdots \rightarrow P_n \oplus Q_n \rightarrow P_{n-1} \oplus Q_{n-1} \rightarrow \cdots \rightarrow P_0 \oplus Q_0 \rightarrow 0$$

is a projective resolution of $A \oplus B$. Since $T$ is additive we obtain

$$L_n T(A \oplus B) = L_n TA \oplus L_n TB.$$

The reader may convince himself that $L_n T(\iota_A)$ and $L_n T(\iota_B)$ are the canonical injections. $\square$
