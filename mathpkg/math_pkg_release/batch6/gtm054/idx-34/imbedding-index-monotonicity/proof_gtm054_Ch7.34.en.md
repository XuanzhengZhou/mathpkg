---
role: proof
locale: en
of_concept: imbedding-index-monotonicity
source_book: gtm054
source_chapter: "Chapter VII"
source_section: "Section 34"
---

Any subgraph of $\Gamma$ may be obtained by first deleting some edges of $\Gamma$ and then deleting some isolated vertices. Since isolated vertices affect neither the dimension of a cycle space nor the size of a cycle cover, we need show only that $\iota(\Gamma_{(E)}) \leq \iota(\Gamma)$ for any edge $E$ of $\Gamma$.

By IIIC1a, $\dim(\mathcal{L}(\Gamma_{(E)})) = \dim(\mathcal{L}(\Gamma)) - 1$ unless $E$ is an isthmus, in which case $\dim(\mathcal{L}(\Gamma_{(E)})) = \dim(\mathcal{L}(\Gamma))$. Turning to cycle covers, we note that every cycle cover of $\Gamma_{(E)}$ is a cycle cover of $\Gamma$, and if $E$ is an isthmus, the converse also holds. Hence $\nu_{2}(\Gamma) \geq \nu_{2}(\Gamma_{(E)})$, with equality holding if $E$ is an isthmus. Hence $\iota(\Gamma_{(E)}) = \iota(\Gamma)$ for $E$ an isthmus. If $E$ is not an isthmus, then because of C2, it suffices to show that $\nu_{2}(\Gamma) \leq \nu_{2}(\Gamma_{(E)}) + 1$.

Suppose $\nu_{2}(\Gamma) = \nu_{2}(Z_{1}, \ldots, Z_{m})$. If $E \notin \bigcup_{i=1}^{m} Z_{i}$, then $Z_{1}, \ldots, Z_{m}$ is also a cycle cover of $\Gamma_{(E)}$, and $\nu_{2}(\Gamma) = \nu_{2}(\Gamma_{(E)})$. If $E \in \bigcup_{i=1}^{m} Z_{i}$, then by including $Z_{1} + \cdots + Z_{m}$ if necessary, we may assume that $E$ belongs to exactly two of the cycles, say $Z_{m-1}$ and $Z_{m}$. It follows that $Z_{1}, \ldots, Z_{m-1}, (Z_{m-1} + Z_{m})$ is a cycle cover of $\Gamma_{(E)}$ of size $m-1$. Hence $\nu_{2}(\Gamma_{(E)}) \leq m-1 = \nu_{2}(\Gamma) - 1$, i.e., $\nu_{2}(\Gamma) \leq \nu_{2}(\Gamma_{(E)}) + 1$.

From this, for $E$ not an isthmus, $\iota(\Gamma_{(E)}) = \nu_{2}(\Gamma_{(E)}) - \dim(\mathcal{L}(\Gamma_{(E)})) \leq \nu_{2}(\Gamma) - (\dim(\mathcal{L}(\Gamma)) - 1) = \iota(\Gamma) + 1 - 1 = \iota(\Gamma)$, completing the proof.
