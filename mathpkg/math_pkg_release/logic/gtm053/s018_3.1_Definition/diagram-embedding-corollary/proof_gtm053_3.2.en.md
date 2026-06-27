---
role: proof
locale: en
of_concept: diagram-embedding-corollary
source_book: gtm053
source_chapter: "3"
source_section: "3.2"
---

For (i): If $A$ can be embedded in $\mathcal{M} \models T$, then the expansion $\mathcal{M}_A$ obtained by interpreting each $c_a$ as the image of $a$ under the embedding satisfies $T \cup \text{Diag}(A)$, so the set is consistent. Conversely, if $T \cup \text{Diag}(A)$ is consistent, it has a model $\mathcal{N}$. Since $\mathcal{N} \models \text{Diag}(A)$, the map $a \mapsto c_a^{\mathcal{N}}$ is an embedding of $A$ into the $L$-reduct of $\mathcal{N}$, which is a model of $T$.

For (ii): The same argument with $\text{CDiag}(A)$ replacing $\text{Diag}(A)$, noting that satisfying $\text{CDiag}(A)$ ensures the embedding is elementary.
