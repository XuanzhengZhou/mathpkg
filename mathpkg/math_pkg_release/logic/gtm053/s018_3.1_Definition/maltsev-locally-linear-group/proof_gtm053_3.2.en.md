---
role: proof
locale: en
of_concept: maltsev-locally-linear-group
source_book: gtm053
source_chapter: "3"
source_section: "3.2"
---

We use the notion of interpretability of structures and the fact that the interpretation of $\text{GL}_n(F)$ in a field $F$ is independent of $F$.

Let $G = (G, *, e)$ be a group with the property that every finitely generated subgroup is embeddable into $\text{GL}_n(F)$ for some field $F$ (depending on the subgroup). We must show that $G$ itself embeds into $\text{GL}_n(K)$ for some field $K$.

Consider the theory $T_F$ of fields in the language $(+, \cdot, 0, 1)$. Consider the diagram $\text{Diag}(G)$ of the group.

Let $D((x_{ij}))$ be the formula in $n^2$ variables in the language of fields defining the set of invertible matrices:

$$\{(x_{ij}) \in F^{n^2} : i, j = 1, \ldots, n,\; \det(x_{ij}) \neq 0\}.$$

Now we translate the diagram of $G$ into a diagram $\text{Diag}^F(G)$ in the language of fields extended by new constant symbols. For each constant symbol $c^g$ naming an element $g$ of $G$ we introduce $n^2$ constant symbols $c^g_{ij}$ ($i, j \in \{1, \ldots, n\}$), and include in $\text{Diag}^F(G)$ the formula $D((c^g_{ij}))$ for every $g \in G$. For each equation $c^g * c^h = c^{gh}$ in the diagram of $G$, we include in $\text{Diag}^F(G)$ the formula

$$\sum_{k=1}^{n} c^g_{ik} \cdot c^h_{kj} = c^{gh}_{ij}.$$

Consider the set of sentences

$$T = T_F \cup \text{Diag}^F(G).$$

The assumption that every finitely generated subgroup of $G$ is linear of rank $n$ implies that every finite subset of $T$ is consistent (a finitely generated subgroup is realized by matrices over some field). By the Compactness Theorem, $T$ itself is consistent. A model of $T$ is a field $K$ together with an assignment of $n \times n$ matrices to the constants $c^g_{ij}$ that satisfy the matrix multiplication equations, giving an embedding of $G$ into $\text{GL}_n(K)$. Hence $G$ is linear of rank $n$.
