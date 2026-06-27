---
role: proof
locale: en
of_concept: hom-ext-sequence-first-variable
source_book: gtm004
source_chapter: "III"
source_section: "5"
---

# Proof of Hom-Ext Sequence in the First Variable (Theorem 5.3)

Let $B$ be a $\Lambda$-module and let $A' \xrightarrow{\varphi} A \xrightarrow{\psi} A''$ be a short exact sequence. Then there exists a connecting homomorphism

$$
\omega : \operatorname{Hom}_\Lambda(A', B) \rightarrow \operatorname{Ext}_\Lambda(A'', B)
$$

such that the following sequence is exact and natural:

$$
0 \rightarrow \operatorname{Hom}_\Lambda(A'', B) \rightarrow \operatorname{Hom}_\Lambda(A, B) \xrightarrow{\varphi^*} \operatorname{Hom}_\Lambda(A', B) \xrightarrow{\omega} \operatorname{Ext}_\Lambda(A'', B) \rightarrow \operatorname{Ext}_\Lambda(A, B) \xrightarrow{\varphi^*} \operatorname{Ext}_\Lambda(A', B).
$$

**Proof.** Using Lemma 5.4, projective presentations may be chosen such that the following diagram is commutative with short exact middle row:

$$
\begin{array}{ccccccccc}
0 & \rightarrow & R' & \rightarrow & P' & \rightarrow & A' & \rightarrow & 0 \\
& & \downarrow & & \downarrow \iota & & \downarrow \varphi & & \\
0 & \rightarrow & R & \rightarrow & P & \rightarrow & A & \rightarrow & 0 \\
& & \downarrow & & \downarrow \pi & & \downarrow \psi & & \\
0 & \rightarrow & R'' & \rightarrow & P'' & \rightarrow & A'' & \rightarrow & 0
\end{array}
$$

By Lemma 5.1 applied to the second and third row, the top row is short exact as well. Applying $\operatorname{Hom}_\Lambda(-, B)$ we obtain the following diagram:

$$
\begin{array}{ccccc}
\operatorname{Hom}_\Lambda(A'', B) & \rightarrow & \operatorname{Hom}_\Lambda(A, B) & \rightarrow & \operatorname{Hom}_\Lambda(A', B) \\
\downarrow & & \downarrow & & \downarrow \\
0 \rightarrow \operatorname{Hom}_\Lambda(P'', B) & \rightarrow & \operatorname{Hom}_\Lambda(P, B) & \xrightarrow{\iota^*} & \operatorname{Hom}_\Lambda(P', B) \rightarrow 0 \\
\downarrow & & \downarrow & & \downarrow \\
0 \rightarrow \operatorname{Hom}_\Lambda(R'', B) & \rightarrow & \operatorname{Hom}_\Lambda(R, B) & \rightarrow & \operatorname{Hom}_\Lambda(R', B) \\
\downarrow & & \downarrow & & \downarrow \\
\operatorname{Ext}_\Lambda(A'', B) & \rightarrow & \operatorname{Ext}_\Lambda(A, B) & \rightarrow & \operatorname{Ext}_\Lambda(A', B)
\end{array}
$$

By Theorem I.2.2 the second and third rows are exact. In the second row, $\iota^* : \operatorname{Hom}_\Lambda(P, B) \rightarrow \operatorname{Hom}_\Lambda(P', B)$ is epimorphic since $P = P' \oplus P''$, so $\operatorname{Hom}_\Lambda(P' \oplus P'', B) \cong \operatorname{Hom}_\Lambda(P', B) \oplus \operatorname{Hom}_\Lambda(P'', B)$. Lemma 5.1 now yields the Hom-Ext sequence claimed.

As in the proof of Theorem 5.2, one shows that $\omega$ is independent of the chosen projective presentations. Also, one proves that the Hom-Ext sequence in the first variable is natural with respect to homomorphisms $\beta : B \rightarrow B'$ and with respect to morphisms of short exact sequences.

**Description of the connecting homomorphism in terms of extensions.** Given $\alpha : A' \rightarrow B$, consider the push-out $E$ of $\alpha$ and $\varphi : A' \rightarrow A$, yielding the diagram

$$
\begin{array}{ccccc}
A' & \rightarrow & A & \rightarrow & A'' \\
\downarrow \alpha & & \downarrow & & \parallel \\
B & \rightarrow & E & \rightarrow & A''
\end{array}
$$

The extension $B \rightarrow E \rightarrow A''$ represents $-\omega(\alpha)$ (up to sign convention). Specifically, using the presentation $R'' \rightarrow P'' \rightarrow A''$ and the map $\chi : P'' \rightarrow A$ from Lemma 5.4, one constructs $\sigma = -\tau : R'' \rightarrow B$ such that $[\sigma]$ represents $-\omega(\alpha)$.
