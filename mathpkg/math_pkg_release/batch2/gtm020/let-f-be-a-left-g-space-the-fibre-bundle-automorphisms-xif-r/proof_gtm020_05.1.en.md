---
locale: en
of_concept: let-f-be-a-left-g-space-the-fibre-bundle-automorphisms-xif-r
role: proof
source_book: gtm020
source_chapter: 5. Local Coordinate Description of Fibre Bundles
source_section: '1'
---

By (1.1), fibre bundle automorphisms are quotients of $(b, s, y) \mapsto (b, g(b)s, y)$. Since $(b, g(b)s, y) \bmod G = (b, g(b)y)$, the fibre bundle automorphisms are of the form $(b, y) \mapsto (b, g(b)y) = h_g(b, y)$.

Note that for $h_g(b, y) = (b, g(b)y)$ and $h_{g'}(b, y) = (b, g'(b)y)$ we have $h_{g'}h_g = h_{g'}g$, and $h_g$ is the identity if and only if $g(b) = 1$ for each $b \in B$.

2. Charts and Transition Functions

Let $G$ be a group, and let $Y$ be a left $G$-space. In this section, all principal bundles are $G$-bundles, and all fibre bundles have fibre $Y$. For a space $B$, let $\theta(B)$ denote the product fibre bundle $(B \times Y, p, B)$. We view the total space of a restricted bundle $\eta|A$ as a subspace of the total space of $\eta$.

Since we have yet to relate formally the concepts of vector bundle and fibre bundle, the above definitions and results are stated for both concepts. A result of

A fibre bundle is locally trivial if and only if it has an atlas of charts. Then it has a unique complete atlas. The covering associated with the atlas $\{(h_i, V_i)\}$ is the open covering $\{V_i\}$. A vector bundle is defined in terms having an atlas of charts [see 3(1.1)].

Let $\{(h_i, V_i)\}$ with $i \in I$ be an atlas for a fibre (vector) bundle $\eta$. We restrict $h_i$ and $h_j$ to $V_i \cap V_j$ and apply Proposition (2.2). There exists a unique map $g_{i,j}: V_i \cap V_j \rightarrow G$ such that $h_j(b, y) = h_i(b, g_{i,j}(b)y)$ for $(b, y) \in (V_i \cap V_j) \times Y$. The functions $g_{i,j}$ on $V_i \cap V_j$ have the following properties:

(T1) For each $b \in V_i \cap V_j \cap V_k$, the relation $g_{i,k}(b) = g_{i,j}(b)g_{j,k}(b)$ holds.

(T2) For each $b \in V_i$, the map $g_{i,i}(b)$ is equal to the identity in $G$.

(T3) For each $b \in V_i \cap V_j$, the relation $g_{i,j}(b) = g_{j,i}(b)$ holds.

Properties (T1) to (T3) follow from the fact that $g_{i,j}$ is the only map satisfying the relation $h_j(b, y) = h_i(b, g_{i,j}(b)y)$.
