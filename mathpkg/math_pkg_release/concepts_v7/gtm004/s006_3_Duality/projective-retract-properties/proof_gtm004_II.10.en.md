---
role: proof
locale: en
of_concept: projective-retract-properties
source_book: gtm004
source_chapter: "II"
source_section: "10"
---

# Proof of Properties of Projectives as Retracts

**(i) A retract of a projective object is projective.** Let $P$ be projective and suppose $Q$ is a retract of $P$, i.e., there exist morphisms $\sigma: Q \to P$ and $\varrho: P \to Q$ with $\varrho \circ \sigma = 1_Q$. Given a diagram

$$\begin{array}{ccc}
Q & \xrightarrow{\varphi} & B \\
& & \downarrow{\scriptstyle \varepsilon} \\
A & \xrightarrow{\varepsilon} & B
\end{array}$$

with $\varepsilon$ epimorphic. Compose the top arrow with $\varrho$ to get $\varphi \circ \varrho: P \to B$. Since $P$ is projective, there exists $\psi': P \to A$ such that $\varepsilon \circ \psi' = \varphi \circ \varrho$. Set $\psi = \psi' \circ \sigma: Q \to A$. Then

$$\varepsilon \circ \psi = \varepsilon \circ \psi' \circ \sigma = \varphi \circ \varrho \circ \sigma = \varphi \circ 1_Q = \varphi.$$

Thus $Q$ is projective.

**(ii) If $U$ maps epimorphisms to surjections, then $FrU(P)$ is projective for every $P$, and every projective $P$ is a retract of $FrU(P)$.** Since $\varepsilon_P: FrU(P) \twoheadrightarrow P$ is an epimorphism (by the hypothesis on $U$; the counit of the free-forgetful adjunction is surjective because every element of $U(P)$ generates $P$), and $P$ is projective, the diagram

$$\begin{array}{ccc}
P & \xrightarrow{1_P} & P \\
{\scriptstyle \sigma}\downarrow & \nearrow & \downarrow{\scriptstyle \varepsilon_P} \\
FrU(P) & = & FrU(P)
\end{array}$$

admits a lift $\sigma: P \to FrU(P)$ with $\varepsilon_P \circ \sigma = 1_P$. Thus $P$ is a retract of the free object $FrU(P)$, which is projective by Corollary 10.3.

**(iii) If the morphism sets of $\mathfrak{C}$ are nonempty, and $P = \coprod_i P_i$ is a coproduct of projectives, then each $P_i$ is also projective.** This follows from (i) and the fact that each $P_i$ is a retract of the coproduct $P$ via the canonical injection and the universal property of the coproduct with the zero morphisms on the other components.
