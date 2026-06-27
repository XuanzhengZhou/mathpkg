---
role: proof
locale: en
of_concept: planar-imbedding-edge-contraction
source_book: gtm054
source_chapter: "E"
source_section: "11"
---

Recall that operations (i) or (ii) from E13 where the edge in question is an isthmus do not reduce the cycle space in an essential way. Therefore, let $e \in \operatorname{Fnd}(\mathcal{Z}(\Gamma))$ — recall A21 — and let $Z_1, \ldots, Z_k$ be a planar imbedding of $\Gamma$ such that $e \in Z_1 \cap Z_2$ (in a planar imbedding every edge in $\operatorname{Fnd}(\mathcal{Z}(\Gamma))$ belongs to exactly two cycles).

To show that $Z_1 + Z_2, Z_3, \ldots, Z_k$ spans $\mathcal{Z}(\Gamma_{(e)})$, let $Z = \sum_{i=1}^{k} a_i Z_i$ for some $a_1, \ldots, a_k \in \mathbb{K}$. If $Z \in \mathcal{Z}(\Gamma_{(e)})$, then $a_1 = a_2$ (since $e$ has been contracted, the coefficients of the two cycles containing $e$ must agree on all edges of $Z$), and

$$Z = a_1(Z_1 + Z_2) + \sum_{i=3}^{k} a_i Z_i$$

as required. Thus $Z_1 + Z_2, Z_3, \ldots, Z_k$ spans $\mathcal{Z}(\Gamma_{(e)})$.

It follows that each edge in $\operatorname{Fnd}(\mathcal{Z}(\Gamma_{(e)}))$ belongs to at least one of the cycles $Z_1 + Z_2, Z_3, \ldots, Z_k$. Since $Z_1, \ldots, Z_k$ is a planar imbedding, each such edge is in at most two of the cycles. Finally, by the dependence relation $(Z_1 + Z_2) + Z_3 + \ldots + Z_k = \varnothing$ (since $\sum_{i=1}^{k} Z_i = \varnothing$ in a planar imbedding, by E3), each edge in $\operatorname{Fnd}(\mathcal{Z}(\Gamma_{(e)}))$ lies in exactly two of the cycles. Hence $Z_1 + Z_2, Z_3, \ldots, Z_k$ is a planar imbedding of $\Gamma_{(e)}$.
