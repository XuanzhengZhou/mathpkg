---
role: proof
locale: en
of_concept: projective-iff-ext-vanishes
source_book: gtm004
source_chapter: "III"
source_section: "5"
---

# Proof of Projectivity iff Ext Vanishes (Corollary 5.5)

The $\Lambda$-module $A$ is projective if and only if $\operatorname{Ext}_\Lambda(A, B) = 0$ for all $\Lambda$-modules $B$.

**Proof.** If $A$ is projective, then $\operatorname{Ext}_\Lambda(A, B) = 0$ for all $B$ by Proposition 4.3 (or directly from the definition: for a projective presentation $0 \rightarrow 0 \rightarrow P \xrightarrow{1} A \rightarrow 0$, we have $\operatorname{Ext}_\Lambda(A, B) = 0$).

Conversely, suppose $\operatorname{Ext}_\Lambda(A, B) = 0$ for all $\Lambda$-modules $B$. Take any epimorphism $\varepsilon : P \twoheadrightarrow A$ with $P$ projective, and let $K = \ker \varepsilon$, giving a short exact sequence

$$
0 \rightarrow K \rightarrow P \xrightarrow{\varepsilon} A \rightarrow 0.
$$

Apply the Hom-Ext sequence in the first variable (Theorem 5.3) with respect to this short exact sequence and an arbitrary $\Lambda$-module $B$:

$$
0 \rightarrow \operatorname{Hom}_\Lambda(A, B) \rightarrow \operatorname{Hom}_\Lambda(P, B) \rightarrow \operatorname{Hom}_\Lambda(K, B) \xrightarrow{\omega} \operatorname{Ext}_\Lambda(A, B) \rightarrow \cdots
$$

Since $\operatorname{Ext}_\Lambda(A, B) = 0$ by hypothesis, the connecting homomorphism $\omega$ is zero, and the map $\operatorname{Hom}_\Lambda(P, B) \rightarrow \operatorname{Hom}_\Lambda(K, B)$ is epimorphic. Taking $B = K$, the identity map $1_K \in \operatorname{Hom}_\Lambda(K, K)$ lifts to a map $s : P \rightarrow K$, which shows that the sequence splits, hence $A$ is a direct summand of the projective module $P$, and therefore $A$ is projective.
