---
role: proof
locale: en
of_concept: interior-of-polygon-is-finite-polyhedron
source_book: gtm047
source_chapter: "2"
source_section: "Separation Properties of Polygons in R^2"
---

Let $L_1, L_2, \ldots, L_n$ be the lines that contain edges of $J$. These lines are finite in number, and each intersects the union of the others in a finite number of points. Note that some sets $L_i \cap I$ may not be connected; this does not matter. Each line $L_i$ decomposes $\mathbf{R}^2$ into two closed half-planes $H_i, H_i'$; and any finite intersection of closed half-planes is closed and convex. Therefore $\bigcup_{i=1}^n L_i$ decomposes $\mathbf{R}^2$ into a finite collection of closed convex regions $R_1, R_2, \ldots, R_m$, such that for each $j$ we have $\operatorname{Fr} R_j \subset \bigcup_{i=1}^n L_i$.

For each $1$-simplex $vv'$ of $\operatorname{Fr} R_j$ we form the $2$-simplex $w_j v v'$ where $w_j$ is an interior point of $R_j$ (see Figure 2.4). This gives a triangulation of $R_j$. The union of these is a triangulation of $\overline{I}$. $\square$
