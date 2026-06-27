---
role: proof
locale: en
of_concept: disjoint-arcs-same-frontier-component
source_book: gtm047
source_chapter: "4"
source_section: "4"
---

In Figure 4.5, we have shown $\bar{I}$ as a rectangular region, with $P$ and $R$ as the midpoints of a pair of opposite sides. See Theorem 3.5 and Problem 3.5.

By a brick-decomposition of the plane we mean a collection $G = \{g_i\}$ of polyhedral disks ($=2$-cells) such that (1) $\bigcup_{i=1}^{\infty} g_i = \mathbf{R}^2$, (2) if two sets $g_i$ and $g_j$ intersect, then their intersection is a broken line lying in the frontier of each of them, and (3) every point has a neighborhood which intersects at most three of the sets $g_i$. One way to get such a collection is to cut up the plane by horizontal lines and vertical segments so as to get a sort of "infinite brick wall," as shown in Figure 4.6.

In general, given a set $M$ in a metric space $[X, d]$, the diameter $\delta M$ of $M$ is the least upper bound of the numbers $d(P, Q)$ $(P, Q \in M)$. (Thus $\delta M$ may be $\infty$.) If $G$ is a collection of subsets of $X$, then the mesh of $G$ is the least upper bound of the numbers $\delta g$ ($g \in G$).

Evidently we can construct a brick-decomposition $G$ of $\mathbf{R}^2$ with mesh as small as we please. In any case, the union of any subcollection of $G$ is a 2-manifold with boundary. In the present case, we use bricks which are rectangular regions, with sides parallel to the edges of $\operatorname{Fr} I$, such that $\bar{I}$ is the union of a subcollection of them. And we use bricks of sufficiently small diameter so that no one of them intersects both $A_1$ and $A_2$. (See Problem 1.12.)

Let $N$ be the union of all bricks in the decomposition that intersect $A_1$. Then $N$ is a 2-manifold with boundary, and so also is the set

$$N' = N \cap \bar{I}.$$

Let $J$ be the component of $\operatorname{Fr} N'$ that contains $P$. Then $J$ is a 1-sphere. Let $B_1$ be the component of $J \cap \operatorname{Fr} I$ that contains $P$. Then $B_1$ is a broken line between two points $T$ and $U$, where $T, U \in \operatorname{Fr} I$, $T$ lies below $P$ and $R$, and $U$ lies above $P$ and $R$. Let $B_2$ be the other broken line between $T$ and $U$ in $J$. Let $V$ be the last point of $B_2$ (in the order from $T$) that lies in $\operatorname{Fr} I$ and lies below $P$ and $R$; and let $W$ be the first point of $B_2$ that follows $V$ and lies in $\operatorname{Fr} I$. Then $W$ lies above $P$ and $R$ in $\operatorname{Fr} I$.

Let $B$ be the broken line between $V$ and $W$ in $B_2$. Then $B \cap \operatorname{Fr} I = \{V, W\}$. Thus $V$ and $W$...
