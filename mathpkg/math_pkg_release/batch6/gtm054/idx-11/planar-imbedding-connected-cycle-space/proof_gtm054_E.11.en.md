---
role: proof
locale: en
of_concept: planar-imbedding-connected-cycle-space
source_book: gtm054
source_chapter: "E"
source_section: "11"
---

Let $\Gamma$ be a planar multigraph.

**($\Leftarrow$)** Suppose that $Z_1, \ldots, Z_k$ is a planar imbedding of $\Gamma$ which is not simple. Then, for some reordering of the cycles,

$$\sum_{i=1}^{h} Z_i = \varnothing \quad \text{for some } h < k.$$

Let $\mathcal{B}_1$ and $\mathcal{B}_2$ be the subspaces spanned by $\{Z_1, \ldots, Z_h\}$ and $\{Z_{h+1}, \ldots, Z_k\}$, respectively, and let $B_j = \operatorname{Fnd}(\mathcal{B}_j)$ for $j = 1, 2$. These subspaces are not trivial. If $e \in B_1 \cap B_2$, then by the definition of a planar imbedding, $e$ belongs to only one of the cycles $Z_1, \ldots, Z_h$, which is contrary to the properties of a planar imbedding (Exercise E10). Hence $B_1 \cap B_2 = \varnothing$, and $\mathcal{B}_1 \oplus \mathcal{B}_2$ is a well-defined subspace of $\mathcal{Z}(\Gamma)$.

On the other hand, if $Z \in \mathcal{Z}(\Gamma)$, then for some $a_1, \ldots, a_k \in \mathbb{K}$, we have

$$Z = \sum_{i=1}^{k} a_i Z_i = \sum_{i=1}^{h} a_i Z_i + \sum_{i=h+1}^{k} a_i Z_i \in \mathcal{B}_1 \oplus \mathcal{B}_2.$$

Thus $\mathcal{Z}(\Gamma) = \mathcal{B}_1 \oplus \mathcal{B}_2$ is a direct sum decomposition of the cycle space, and consequently $\mathcal{Z}(\Gamma)$ is not connected.

($\Rightarrow$) The converse direction follows by considering that if $\mathcal{Z}(\Gamma)$ is not connected, it admits a non-trivial direct sum decomposition $\mathcal{Z}(\Gamma) = \mathcal{B}_1 \oplus \mathcal{B}_2$. From this decomposition one can reconstruct a planar imbedding that fails to be simple. Together with the observation that every planar imbedding of $\Gamma$ involving a non-elementary region would similarly force a decomposition of the cycle space, the equivalence is established.
