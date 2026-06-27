---
role: proof
locale: en
of_concept: gamma-planar-multigraph-e9
source_book: gtm054
source_chapter: "4"
source_section: "Section 11"
---

Suppose that $Z_1, \ldots, Z_k$ is a planar imbedding of $\Gamma$ which is not simple, in which case, for some reordering of the cycles,

$$\sum_{i=1}^{h} Z_i = \varnothing \quad \text{for some } h < k.$$

Let $\mathcal{B}_1$ and $\mathcal{B}_2$ be the subspaces spanned by $\{Z_1, \ldots, Z_h\}$ and $\{Z_{h+1}, \ldots, Z_k\}$, respectively, and let $B_j = \text{Fnd}(\mathcal{B}_j)$ for $j = 1, 2$. These subspaces are not trivial. If $e \in B_1 \cap B_2$, then by the definition of a planar imbedding, $e$ belongs to only one of the cycles $Z_1, \ldots, Z_h$, contrary to E10. Hence $B_1 \cap B_2 = \varnothing$, and $\mathcal{B}_1 \oplus \mathcal{B}_2$ is a well-defined subspace of $\mathcal{Z}(\Gamma)$. On the other hand, if $Z \in \mathcal{Z}(\Gamma)$, then for some $a_1, \ldots, a_k \in \mathbb{K}$, we have $Z = \sum_{i=1}^{k} a_i Z_i = \sum_{i=1}^{h} a_i Z_i + \sum_{i=h+1}^{k} a_i Z_i \in \mathcal{B}_1 \oplus \mathcal{B}_2$. Hence $\mathcal{Z}(\Gamma)$ is not connected.

If we suppose instead that the planar imbedding

One of the important and topologically obvious properties of planar multigraphs is that their submultigraphs are also planar, as are the multi-graphs obtainable therefrom by identifying a pair of vertices incident with a common edge.

A system $\Gamma' = (V', f', E')$ is a contraction of the multigraph $\Gamma = (V, f, E)$ if

(a) $V' \in \mathbb{P}(V)$ and $\Gamma_w$ is connected for all $W \in V'$;
(b) $E' = \{e \in E : f(e) \notin W \text{ for all } W \in V'\}$;
(c) $f'(e) = \{W \in V' : f(e) \cap W \neq \emptyset\}$, for all $e \in E'$.

A contraction of a multigraph is clearly a multigraph, but a contraction of a graph need not itself be a graph. The contraction $\Gamma'$ is uniquely determined by $\Gamma$ and $V'$. Every multigraph is obviously a contraction of itself. In Figure E11, each of the last three multigraphs is a contraction of the first.
