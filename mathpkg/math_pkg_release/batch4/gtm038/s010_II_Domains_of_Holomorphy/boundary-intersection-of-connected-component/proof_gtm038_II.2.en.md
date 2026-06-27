---
role: proof
locale: en
of_concept: boundary-intersection-of-connected-component
source_book: gtm038
source_chapter: "II"
source_section: "2. Pseudoconvexity"
---

We have $G = Q \cup (G - Q)$. $Q$ is open and not empty, and because $(\mathbb{C}^n - B) \cap G \neq \emptyset$, $G - Q$ is also non-empty. Since $G$ is a domain it does not split into two non-empty open subsets. Hence $G - Q$ is not open. Let $\mathfrak{z}_1 \in G - Q$ not be an interior point. Then for every arbitrary neighborhood $U(\mathfrak{z}_1) \subset G$ it is true that $U \cap Q \neq \emptyset$. Therefore $\mathfrak{z}_1$ lies in $\partial Q$. If $\mathfrak{z}_1 \in B$ then there is a connected neighborhood $V(\mathfrak{z}_1) \subset B \cap G$ (with $V \cap Q \neq \emptyset$ also). But then $Q \cup V$ is an open connected set in $B \cap G$ which properly contains $Q$. Since $Q$ is a connected component this is a contradiction. Therefore $\mathfrak{z}_1$ does not lie in $B$. Hence it follows that $\mathfrak{z}_1 \in \partial Q \cap \partial B \cap G$.
