---
role: proof
locale: en
of_concept: bicollar-neighborhood-existence
source_book: gtm047
source_chapter: "31"
source_section: "Bicollar neighborhoods; an extension of the Loop theorem"
---

Let $d_1, d_2, \ldots, d_n$ be a sequence of polyhedral 2-cells in $B$, with disjoint interiors, such that $B = \bigcup_{j=1}^{n} d_j$ and such that the union of any subcollection of these 2-cells is a 2-manifold with boundary. Then there is a polyhedral 3-cell $C_1$ in $M^3$, and a PLH $\rho_1: d_1 \times [0, 1] \leftrightarrow C_1$, such that $C_1 \cap B = d_1$ and $\rho_1(P, 0) = P$ for each $P$.

Suppose (inductively) that we have given

$$\rho_i: \left( \bigcup_{j=1}^{i} d_j \right) \times [0, 1] \leftrightarrow W_i \subset M^3,$$

such that $W_i \cap B = \bigcup_{j=1}^{i} d_j$ and $\rho_i(P, 0) = P$ for each $P$. Let $e_{i+1} = d_{i+1} \cap \bigcup_{j \leqslant i} d_j$, so that $e_{i+1}$ is a finite union of disjoint arcs. Let

$$d'_{i+1} = d_{i+1} \cap \rho_i(e_{i+1} \times [0, 1]).$$

Then $d'_{i+1}$ is a 2-cell, lying in $\text{Bd } \text{Cl}(M^3 - W_i)$. Therefore there is a 3-cell $C_{i+1}$, lying in $\text{Cl}(M^3 - W_i)$, such that $C_{i+1} \cap \text{Bd } \text{Cl}(M^3 - W_i) = d'_{i+1}$. Now extend $\rho_i$ to get $\rho_{i+1}: \left( \bigcup_{j=1}^{i+1} d_j \right) \times [0, 1] \leftrightarrow W_{i+1}$, preserving the conditions for $\rho_i$. The final $\rho_n$ obtained by this process is the desired $\rho$.
