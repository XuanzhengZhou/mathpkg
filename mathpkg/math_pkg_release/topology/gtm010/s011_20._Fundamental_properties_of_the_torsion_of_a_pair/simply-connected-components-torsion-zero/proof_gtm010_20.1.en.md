---
role: proof
locale: en
of_concept: simply-connected-components-torsion-zero
source_book: gtm010
source_chapter: "20"
source_section: "20"
---

Clearly it suffices to prove this when $K$ is connected. Let $c$ be a component of $K-L$. Then $c$ is closed in $K-L$, so $\bar{c} \subset L \cup c$ and $L \cup c$ is a closed set. If $e$ is a cell of $K$ which meets $c$, then $e$ cannot lie totally in $L$, so $e \cap L = \emptyset$. Hence $e \subset K-L$ and consequently $e \subset c$. Thus $L \cup c$ is a subcomplex of $K$ and $c = (L \cup c) - L$.

Let $p: \tilde{K} \to K$ be a universal covering with $G$ the group of covering homeomorphisms. Since $c$ is simply connected, it lifts homeomorphically to $\tilde{K}$. Let $C$ be one lift of $c$. The lifts $\{gC \mid 1 \neq g \in G\}$ are pairwise disjoint. For each cell $e_\alpha$ of $c$, let $\tilde{\varphi}_\alpha$ be a lift of a characteristic map such that $\tilde{\varphi}_\alpha(\mathring{I}^p) \subset C$. Doing this for all components $c$ of $K-L$ gives a preferred basis for $C(\tilde{K}, \tilde{L})$.

With this basis, the boundary matrix has entries that are either 0 or elements of $G$, and the resulting complex has zero torsion.
