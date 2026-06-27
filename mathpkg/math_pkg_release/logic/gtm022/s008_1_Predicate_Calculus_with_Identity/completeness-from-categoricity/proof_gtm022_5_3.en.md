---
role: proof
locale: en
of_concept: completeness-from-categoricity
source_book: gtm022
source_chapter: "V"
source_section: "3"
---

\textbf{Proof.} Let $p \in \mathcal{L}(\mathcal{T})$, and suppose that neither $p$ nor $\sim p$ is a theorem of $\mathcal{T} = (\mathcal{R}, A, C)$. Since $\sim p$ is not a theorem, the theory $\mathcal{T} \cup \{\sim p\}$ is consistent; since all models of $\mathcal{T}$ are infinite, $\mathcal{T} \cup \{\sim p\}$ has an infinite model, and so the theory $\mathcal{T}' = (\mathcal{R}, A \cup \{p\}, C)$ has an infinite model (or else every model satisfies $\sim p$, making it a theorem). Since $|\mathcal{T}'| \leqslant \aleph$, by the Löwenheim-Skolem Theorem $\mathcal{T}'$ has a model $M'$ of cardinal $\aleph$. Similarly $\mathcal{T}'' = (\mathcal{R}, A \cup \{\sim p\}, C)$ has a model $M''$ of cardinal $\aleph$. But $M'$ and $M''$ are each models of $\mathcal{T}$ of cardinal $\aleph$, and hence by $\aleph$-categoricity they are isomorphic. This contradicts $p$ being true in $M'$ and false in $M''$. Therefore either $\mathcal{T} \vdash p$ or $\mathcal{T} \vdash \sim p$, and $\mathcal{T}$ is complete.
