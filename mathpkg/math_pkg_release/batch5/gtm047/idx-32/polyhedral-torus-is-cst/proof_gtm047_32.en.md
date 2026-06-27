---
role: proof
locale: en
of_concept: polyhedral-torus-is-cst
source_book: gtm047
source_chapter: "32"
source_section: "Section 32"
---

By the definition of a torus, we have $S = \bigcup_{i=1}^{4} C_i^3$, where each $C_i$ is a 3-cell, and these 3-cells are arranged in cyclic order in $S$, as in Theorems 23.20 and 23.21, except that they are not necessarily polyhedra. Consider the two components $M_1^3$ and $M_2^3$ of $S - (C_1^3 \cup C_2^3)$. Each $M_i^3$ is a 3-manifold with boundary, and each of the sets $\operatorname{Bd} M_i^3$ is the interior of an annulus in $\operatorname{Bd} S$. By Theorem 8.2, each $M_i^3$ has a rectilinear triangulation $K_i$, so that $M_i^3$ becomes a PL 3-manifold with boundary. And each $M_i^3$ is simply connected. By the Loop theorem it follows that $M_i^3$ contains a polyhedral 2-cell $\Delta_i$ such that $\Delta_i \cap \operatorname{Bd} M_i^3 = \operatorname{Bd} \Delta_i$ and $\operatorname{Bd} \Delta_i$ is not contractible in $\operatorname{Bd} M_i^3$.

(This is the only point in the proof at which we use the hypothesis that $S$ is a polyhedron in $\mathbf{R}^3$.)

By Theorem 23.8, $\operatorname{Bd} S = \operatorname{Fr} S$. Let $E = \mathbf{R}^3 - S$. By Theorem 26.3, $\operatorname{Bd} S$ has a bicollar neighborhood $N$. Let $N' = N - S$. Then $N'$ is connected. Since every point of $E$ can be joined, by a broken line in $E$, to a point of $N'$, it follows that $E$ is connected. Since $\operatorname{Bd} D_i^3 \subset S$ ($i = 1, 2$), we have $D_i^3 \subset S$, so that (1) $D_1^3 \cup D_2^3 \subset S$. Since $A_i \subset \operatorname{Fr} S$ ($i = 1, 2$), we have (2) $\operatorname{Int} D_1^3 \cap \operatorname{Int} D_2^3 = \varnothing$. Finally, let $P$ be a point of $\operatorname{Int} S$, and suppose that $P \notin D_1^3$. Since $\mathbf{R}^3 - D_1^3$ is connected, $P$ can be joined to a point of $E$ by a broken line in $\mathbf{R}^3 - D_1^3$. Therefore $P$ can be joined to a point $Q$ of $\operatorname{Bd} S$ by a broken line in $S - D_1^3$. Since $Q \in A_2$, it follows that $P \in D_2^3$. Thus we have (3) $S \subset D_1^3 \cup D_2^3$.

By (1), (2), and (3), $\Delta_1$ and $\Delta_2$ decompose $S$ into two combinatorial 3-cells $D_1^3$ and $D_2^3$, with $D_1^3 \cap D_2^3 = \Delta_1 \cap \Delta_2$. We now define $\phi: \sigma^2 \times [0, 1] \to S$ by identifying the two faces $\Delta_1$ and $\Delta_2$ appropriately, yielding a PL identification mapping that exhibits $S$ as a combinatorial solid torus.
