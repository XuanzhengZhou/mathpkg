---
role: proof
locale: en
of_concept: hom-ext-sequence-second-variable
source_book: gtm004
source_chapter: "III"
source_section: "5"
---

# Proof of Hom-Ext Sequence in the Second Variable (Theorem 5.2)

Let $A$ be a $\Lambda$-module and let $B' \xrightarrow{\varphi} B \xrightarrow{\psi} B''$ be an exact sequence of $\Lambda$-modules. We construct a connecting homomorphism $\omega : \operatorname{Hom}_\Lambda(A, B'') \rightarrow \operatorname{Ext}_\Lambda(A, B')$ such that the following sequence is exact and natural:

$$
0 \rightarrow \operatorname{Hom}_\Lambda(A, B') \xrightarrow{\varphi_*} \operatorname{Hom}_\Lambda(A, B) \xrightarrow{\psi_*} \operatorname{Hom}_\Lambda(A, B'') \xrightarrow{\omega} \operatorname{Ext}_\Lambda(A, B') \xrightarrow{\varphi_*} \operatorname{Ext}_\Lambda(A, B) \xrightarrow{\psi_*} \operatorname{Ext}_\Lambda(A, B'').
$$

**Proof.** Choose any projective presentation $R \xrightarrow{\mu} P \xrightarrow{\varepsilon} A$ of $A$ and consider the following diagram with exact rows and columns:

$$
\begin{array}{ccccc}
& & 0 & & \\
& & \downarrow & & \\
\operatorname{Hom}_\Lambda(A, B') & \xrightarrow{\varphi_*} & \operatorname{Hom}_\Lambda(A, B) & \xrightarrow{\psi_*} & \operatorname{Hom}_\Lambda(A, B'') \\
\downarrow & & \downarrow & & \downarrow \\
0 \rightarrow \operatorname{Hom}_\Lambda(P, B') & \rightarrow & \operatorname{Hom}_\Lambda(P, B) & \rightarrow & \operatorname{Hom}_\Lambda(P, B'') \rightarrow 0 \\
\downarrow & & \downarrow & & \downarrow \\
0 \rightarrow \operatorname{Hom}_\Lambda(R, B') & \rightarrow & \operatorname{Hom}_\Lambda(R, B) & \rightarrow & \operatorname{Hom}_\Lambda(R, B'') \\
\downarrow & & \downarrow & & \downarrow \\
\operatorname{Ext}_\Lambda(A, B') & \xrightarrow{\varphi_*} & \operatorname{Ext}_\Lambda(A, B) & \xrightarrow{\psi_*} & \operatorname{Ext}_\Lambda(A, B'')
\end{array}
$$

The second row is exact because $P$ is projective, so $\operatorname{Hom}_\Lambda(P, -)$ is exact. The columns are exact by definition of Ext (up to the connecting homomorphisms). By Lemma 5.1 applied to the second and third rows, we obtain the claimed Hom-Ext sequence.

The connecting homomorphism $\omega$ is defined as follows: given $\alpha : A \rightarrow B''$, lift it to $\tilde{\alpha} : P \rightarrow B$ (using projectivity of $P$), then restrict to $\tilde{\alpha}|_R : R \rightarrow B$. The image lands in $B'$ (since the composition $R \rightarrow P \rightarrow A \rightarrow B''$ is zero), giving an element of $\operatorname{Hom}_\Lambda(R, B')$, and hence a class in $\operatorname{Ext}_\Lambda(A, B') = \operatorname{Hom}_\Lambda(R, B') / \operatorname{Im}(\operatorname{Hom}_\Lambda(P, B') \rightarrow \operatorname{Hom}_\Lambda(R, B'))$.

Naturality is proved by considering homomorphisms $\alpha : A' \rightarrow A$ (inducing a map on projective presentations) and homomorphisms $\beta', \beta, \beta''$ making the diagram

$$
\begin{array}{ccccc}
B' & \rightarrow & B & \rightarrow & B'' \\
\downarrow \beta' & & \downarrow \beta & & \downarrow \beta'' \\
C' & \rightarrow & C & \rightarrow & C''
\end{array}
$$

commutative. These induce mappings between the corresponding Hom-Ext sequences. In particular, choosing $\alpha = 1_A$ shows that $\omega$ is independent of the chosen projective presentation.
