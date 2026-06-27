---
role: proof
locale: en
of_concept: deducibility-criterion
source_book: gtm053
source_chapter: "I"
source_section: "6"
---

The deducibility criterion follows from Theorem 6.2 (Gödel's Completeness Theorem).

\textbf{(a)} If $\mathcal{E}$ is inconsistent, then any formula $P$ is deducible from $\mathcal{E}$ by the principle of explosion. If $\mathcal{E}$ is consistent, then by Theorem 6.2(b), $\mathcal{E}$ can be imbedded in a Gödelian set $T$. By Theorem 6.2(a), $T = T_{\phi}L$ for some model $\phi$ with cardinality $\leqslant \operatorname{card}(\text{alphabet of } L) + \aleph_0$. Now $P$ is deducible from $\mathcal{E}$ if and only if $P \in T$ (since $T$ is deduction-closed and contains $\mathcal{E}$), which happens if and only if $P$ is $\phi$-true. If $P$ is $\phi$-true for all models of $\mathcal{E}$ having the stated cardinality bound, then in particular $P$ is true in the model constructed above, so $P$ is deducible. Conversely, if $P$ is deducible from $\mathcal{E}$, soundness guarantees $P$ is true in all models of $\mathcal{E}$.

\textbf{(b)} A formula $P$ is independent of $\mathcal{E}$ if neither $P$ nor $\neg P$ is deducible from $\mathcal{E}$. This means both $\mathcal{E} \cup \{P\}$ and $\mathcal{E} \cup \{\neg P\}$ are consistent (a set from which a contradiction is not deducible). By Theorem 6.2(b), each consistent set can be embedded in a Gödelian set, and by Theorem 6.2(a) each Gödelian set has a model, so both $\mathcal{E} \cup \{P\}$ and $\mathcal{E} \cup \{\neg P\}$ have models. Conversely, if both have models, then by soundness neither proves a contradiction, so both are consistent, and $P$ is independent.
