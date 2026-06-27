---
role: proof
locale: en
of_concept: tor-exact-sequences
source_book: gtm004
source_chapter: "III"
source_section: "8"
---

# Proof of the Two Exact Sequences for Tor (Theorem 8.3)

For any short exact sequence $B' \xrightarrow{\kappa} B \xrightarrow{\lambda} B'' \rightarrow 0$ of left $\Lambda$-modules and any right $\Lambda$-module $A$, there is an exact sequence

$$
\operatorname{Tor}^\Lambda(A, B') \xrightarrow{\kappa_*} \operatorname{Tor}^\Lambda(A, B) \xrightarrow{\lambda_*} \operatorname{Tor}^\Lambda(A, B'') \xrightarrow{\omega} A \otimes_\Lambda B' \xrightarrow{\kappa_*} A \otimes_\Lambda B \xrightarrow{\lambda_*} A \otimes_\Lambda B'' \rightarrow 0. \tag{8.3}
$$

Similarly, for any short exact sequence $A' \xrightarrow{\kappa} A \xrightarrow{\lambda} A'' \rightarrow 0$ of right $\Lambda$-modules and any left $\Lambda$-module $B$, there is an exact sequence

$$
\operatorname{Tor}^\Lambda(A', B) \xrightarrow{\kappa_*} \operatorname{Tor}^\Lambda(A, B) \xrightarrow{\lambda_*} \operatorname{Tor}^\Lambda(A'', B) \xrightarrow{\omega} A' \otimes_\Lambda B \xrightarrow{\kappa_*} A \otimes_\Lambda B \xrightarrow{\lambda_*} A'' \otimes_\Lambda B \rightarrow 0. \tag{8.4}
$$

**Proof of (8.3).** Choose a projective presentation $R \xrightarrow{\mu} P \xrightarrow{\varepsilon} A$ and construct the diagram:

$$
\begin{array}{cccccc}
\operatorname{Tor}^\Lambda(A, B') & \rightarrow & \operatorname{Tor}^\Lambda(A, B) & \rightarrow & \operatorname{Tor}^\Lambda(A, B'') & \\
\downarrow & & \downarrow & & \downarrow & & \\
R \otimes_\Lambda B' & \rightarrow & R \otimes_\Lambda B & \xrightarrow{1 \otimes \lambda} & R \otimes_\Lambda B'' & \rightarrow 0 \\
\downarrow \mu \otimes 1 & & \downarrow \mu \otimes 1 & & \downarrow \mu \otimes 1 & & \\
0 \rightarrow P \otimes_\Lambda B' & \rightarrow & P \otimes_\Lambda B & \xrightarrow{1 \otimes \lambda} & P \otimes_\Lambda B'' & \rightarrow 0 \\
\downarrow & & \downarrow & & \downarrow & & \\
A \otimes_\Lambda B' & \rightarrow & A \otimes_\Lambda B & \xrightarrow{1 \otimes \lambda} & A \otimes_\Lambda B'' & \rightarrow 0
\end{array}
$$

In this diagram:
- The second row is exact by right exactness of $R \otimes_\Lambda -$ (Proposition 7.3).
- The third row is exact because $P$ is projective, hence flat (Proposition 7.4), so $P \otimes_\Lambda -$ is exact.
- The columns are exact by definition of $\operatorname{Tor}^\Lambda(A, -)$ as the kernel of $\mu \otimes 1$.

Applying Lemma 5.1 (the kernel-cokernel exact sequence) to this diagram yields the exact sequence (8.3).

The connecting homomorphism $\omega : \operatorname{Tor}^\Lambda(A, B'') \rightarrow A \otimes_\Lambda B'$ is induced by the diagram chase in Lemma 5.1: an element of $\operatorname{Tor}^\Lambda(A, B'') = \ker(\mu \otimes 1)$ lifts to $R \otimes_\Lambda B$, maps to $P \otimes_\Lambda B$, and is then pulled back along the isomorphism $P \otimes_\Lambda B' \cong \ker(1 \otimes \lambda)$ to $A \otimes_\Lambda B'$.

The proof of (8.4) is symmetric, using a projective presentation of $B$.

Like the Hom-Ext sequences, the sequences (8.3) and (8.4) are natural. Notice that by contrast with the two sequences involving Ext we obtain only one kind of sequence involving Tor, since $A$ and $B$ play symmetric roles in the definition of Tor.
