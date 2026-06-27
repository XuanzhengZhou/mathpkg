---
role: proof
locale: en
of_concept: given-bipartite-graph-a11
source_book: gtm054
source_chapter: "6"
source_section: "Section 21"
---

Let $V_i'$ be formed from $V_i$ by adjoining sufficiently many new vertices to $V_i$ ($i = 1, 2$) so that $|V_1'| = |V_2'|$ and that

$$\hat{\rho}(B) - 1 \leq \hat{\rho}(B)|V_1'| - |\mathcal{E}|.$$

Then $B' = \{V_1', V_2'\}, \mathcal{E}$ is a bipartite graph. Its valence function, being the extension by zero of $\rho$, will also be denoted by $\rho$.

Let $n$ denote the right-hand member of A12. By Exercise A10, there exists a $(\hat{\rho}(B) - 1)$-valent bipartite graph $B'' = \{V_1'', V_2''\}, \mathcal{E''}$ with $|V_1''| = |V_2''| = n$. We may assume that $B''$ is disjoint from $B'$.

For each $i = 1, 2$,

$$\sum_{x \in V_i'} (\hat{\rho}(B) - \rho(x)) = \hat{\rho}(B)|V_i'| - |\mathcal{E}| = n.$$

Hence for $j \in \{1, 2\}$, $j \neq i$, $V_j''$ admits a partition $\{U_x : x \in V_i'; \rho(x) < \hat{\rho}(B)\}$ wherein each cell $U_x$ has (positive) cardinality $|U_x| = \hat{\rho}(B) - \rho(x)$. Now let

$$\mathcal{E}' = \{x, y\}: x \in V_1' \cup V_2';

partition could have fewer than $\hat{\rho}(\text{B})$ cells. The next result shows that this bound is "best possible" in general and not only in the case of an isovalent bipartite graph (cf. A9).
