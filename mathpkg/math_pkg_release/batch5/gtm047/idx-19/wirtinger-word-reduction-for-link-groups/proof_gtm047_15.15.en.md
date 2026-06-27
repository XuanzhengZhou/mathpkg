---
role: proof
locale: en
of_concept: wirtinger-word-reduction-for-link-groups
source_book: gtm047
source_chapter: "15"
source_section: "15"
---

Let

$$f: [0, 1]^2 \to \mathbf{R}^3 - L$$

be a homotopy from the given word path $p$ to the constant path $e$. Let

$$\rho: \mathbf{R}^3 \to \mathbf{R}^2, \quad (x, y, z) \mapsto (x, y, 0)$$

be the projection. Then $\rho(L)$ is a finite polyhedron, $= |L'|$ for some $L'$, and any crossing point in the diagram of $L$ is automatically a vertex of $L'$. We choose $K$ as a sufficiently fine triangulation of $[0, 1]^2$ so that (1) no set $\rho f(\sigma)$ ($\sigma \in K$) contains more than one vertex of $L'$. Then we make small adjustments in $f$ (if need be), preserving (1), so that (2) if $\sigma \in K$, and $P_0 \notin f(\sigma)$, then $f|\sigma$ is a linear homeomorphism. Finally, by a slight change in the direction of the $z$-axis, preserving (1) and (2), we arrange so that (3) if $\sigma^2 \in K$, and $P_0 \notin f(\sigma^2)$, then $\rho f(\sigma^2)$ is a 2-simplex $\tau^2$, no edge of $\tau^2$ contains a vertex of $L'$, and no vertex of $\tau^2$ lies in $|L'| = \rho(L)$. (Note that under (1), $\operatorname{Int} \tau^2$ contains at most one vertex of $L'$, and hence contains at most one crossing point of the diagram of $L$. Note also that (3) is a condition of "general position," in the sense that the directions for the $z$-axis for which (3) does not hold form a finite union of arcs in the 2-sphere.)

Using the mapping $f$, we can pass from $p$ to $e$ by a finite number of steps, each of which deletes a free 2-simplex from a triangulated 2-cell. At each stage, we have a triangulated 2-cell; part of its boundary (the upper edge of $[0, 1]^2$) is mapped onto $P_0$; $f$, on the rest of the boundary, defines a closed path $q$; and when we pass to the next stage, the corresponding closed path $q'$ is homotopic to $q$.

In each such step, the generator word for $q'$ differs from that for $q$ by an insertion or deletion of one of the prescribed forms $g_i r_j^{\pm 1} g_i^{-1}$, $g_i g_i^{-1}$, or $g_i^{-1} g_i$. For example, to replace $g_k g_j^{-1}$ by $g_i^{-1} g_k$ in a generator word, we would insert

$$g_i^{-1} g_k g_j g_k^{-1} = (g_k g_j^{-1} g_k^{-1} g_i)^{-1} = g_i^{-1} r^{-1} g_i,$$

which is of the prescribed form. The other cases are similar. By repeated application of such steps through the entire sequence of simplicial cancellations, the original generator word is reduced to the identity $e$.
