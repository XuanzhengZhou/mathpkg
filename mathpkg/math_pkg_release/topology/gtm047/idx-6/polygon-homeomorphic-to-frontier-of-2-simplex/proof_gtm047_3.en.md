---
role: proof
locale: en
of_concept: polygon-homeomorphic-to-frontier-of-2-simplex
source_book: gtm047
source_chapter: "3"
source_section: "The Schönflies theorem for polygons in R^2"
---

Let $I$ be the interior of $J$, and let $K$ be a triangulation of $\bar{I}$. Any free 2-simplex of $K$ can be removed by a homeomorphism $h: \mathbb{R}^2 \leftrightarrow \mathbb{R}^2$.

**Case 1.** Suppose that $v_0v_1v_2$ is free, with $v_0v_1v_2 \cap \operatorname{Fr}|K| = v_0v_2$. We take $v_3, v_4$, and $v_5$ as in the figure, so that they and $v_1$ are collinear, with $v_3$ and $v_4$ "very close" to $v_1$ and $v_5$ respectively, so that the constructed homeomorphism pushes the free simplex out of the triangulation while leaving points outside a small neighborhood unchanged.

By repeated application of this removal process, the triangulation can be reduced to a single 2-simplex, giving the desired homeomorphism $h$.
