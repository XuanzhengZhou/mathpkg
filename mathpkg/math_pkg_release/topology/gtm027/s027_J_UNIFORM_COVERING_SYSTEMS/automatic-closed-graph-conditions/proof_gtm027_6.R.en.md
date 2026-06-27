---
role: proof
locale: en
of_concept: automatic-closed-graph-conditions
source_book: gtm027
source_chapter: "6"
source_section: "R"
---

# Proof of Automatic Satisfaction of Closed Graph Conditions

Let $f: G \to H$ be a homomorphism, $H$ Lindelöf, and $G$ non-meager.

For each $V \in \mathcal{V}$, the family $\{f[G] \cap hV : h \in H\}$ is an open cover of $f[G]$ (since $V$ is a neighborhood of $e_H$). Since $H$ is Lindelöf, there exists a countable subcover $\{f[G] \cap h_n V : n \in \omega\}$.

Then $G = \bigcup_n f^{-1}[h_n V]$. Since $G$ is non-meager (by the Baire category theorem for topological groups, a non-meager topological group is a Baire space), some $\overline{f^{-1}[h_n V]}$ has non-void interior, hence is a neighborhood of some point. By translation, $\overline{f^{-1}[V]}$ is a neighborhood of $e_G$. This establishes condition (ii) automatically.

If additionally $g[H] = G$ and $G$ is non-meager, then applying the same argument to $g$ yields condition (ii)* automatically.

For linear topological spaces where $f$ and $g$ are linear, $g[H] = G$, and $G$ is non-meager, both conditions follow: if $V \in \mathcal{V}$, then $\overline{f[G]} \subset V + f[G]$ (by linearity and continuity of addition), and the category argument applies.
