---
role: proof
locale: en
of_concept: left-ideals-subspace-lattice-isomorphism
source_book: gtm031
source_chapter: "VIII"
source_section: "3"
---
Let $\mathfrak{J}'$ be any nonzero left ideal in $\mathfrak{L}$ and let $\mathfrak{S}$ be the join of all the rank subspaces $\mathfrak{R}B$ for $B \in \mathfrak{J}'$. If $B \neq 0$, we can write $B = \sum_{1}^{r} u_j' \times v_j$ where $r$ is the rank of $B$. The set $(v_1, v_2, \ldots, v_r)$ is a basis for $\mathfrak{R}B$ and $(u_1', u_2', \ldots, u_r')$ is a basis for $\mathfrak{R}'B'$, where $B'$ is the transpose of $B$. Since $v_j \in \mathfrak{R}B \subseteq \mathfrak{S}$, we have $B \in \mathfrak{R}' \times \mathfrak{S}$. Hence $\mathfrak{J}' \subseteq \mathfrak{R}' \times \mathfrak{S}$.

Conversely, let $y_1, y_2, \ldots, y_r$ be vectors such that $g(y_i, u_j') = \delta_{ij}$ and let $x_1', x_2', \ldots, x_r'$ be arbitrary in $\mathfrak{R}'$. Set $A = \sum x_i' \times y_i$. Then by the product formula (7),
$$AB = \sum x_i' g(y_i, u_j') \times v_j = \sum x_i' \times v_i,$$
and this linear transformation belongs to $\mathfrak{J}'$ since $\mathfrak{J}'$ is a left ideal. It follows that if $v = \sum \beta_i v_i$ is any vector in $\mathfrak{R}B$ and $x'$ is arbitrary in $\mathfrak{R}'$, then $x' \times v = \sum x' \beta_i \times v_i \in \mathfrak{J}'$. Consequently, if $B_1, B_2, \ldots$ are any linear transformations in $\mathfrak{J}'$, the join of their rank subspaces is contained in the corresponding $\mathfrak{S}$.

Thus the correspondence $\mathfrak{S} \mapsto \mathfrak{R}' \times \mathfrak{S}$ is a bijection between subspaces of $\mathfrak{R}$ and left ideals of $\mathfrak{L}$. Moreover, this correspondence preserves order: if $\mathfrak{S}_1 \supseteq \mathfrak{S}_2$, then $\mathfrak{R}' \times \mathfrak{S}_1 \supseteq \mathfrak{R}' \times \mathfrak{S}_2$. Hence it is a lattice isomorphism from the lattice of subspaces of $\mathfrak{R}$ onto the lattice of left ideals of $\mathfrak{L}$.
