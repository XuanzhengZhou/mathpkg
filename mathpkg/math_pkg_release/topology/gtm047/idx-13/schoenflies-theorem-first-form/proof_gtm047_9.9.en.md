---
role: proof
locale: en
of_concept: schoenflies-theorem-first-form
source_book: gtm047
source_chapter: "9"
source_section: "9"
---

Let $G_1, G_2, \ldots$ be as in Theorem 3 (a sequence of finite collections of arcs refining $J$), and let $H_1, H_2, \ldots$ be as in Theorem 4 (the corresponding collections of linear intervals radiating into $I$). For each $g \in G_1$, with $\text{Bd } g = \{v_0, v_1\}$, let $v_i v_i'$ ($i = 0, 1$) be the element of $H_1$ that contains $v_i$, and let $b_g$ be a broken line, as in Theorem 5, joining two points $w_0, w_1$ of $v_0 v_0'$ and $v_1 v_1'$.

We take the sets $b_g$ in sufficiently small neighborhoods of the arcs $g$ so that:
1. Different sets $b_g$ intersect only in common end-points, and
2. $b_g \cup v_0 w_0 \cup g \cup v_1 w_1 \subset N(v_0, 1)$.

By making slight changes in the sets $b_g$ we can ensure that:
3. Consecutive sets $b_g$ have the same end-points (i.e., we use the same point $w_0$ on each interval $v_0 v_0'$).

It follows that the union of the sets $b_g$ is a polygon $J_0$, with $J$ in its exterior. Let $C_0$ be the closure of the interior of $J_0$. Then $C_0$ is a 2-cell, by the polygonal form of the Schönflies theorem.

We now copy this total configuration in the unit disk $B^2 \subset \mathbf{R}^2$. Let $J'$ be the unit circle $\text{Fr } B^2$, and let $\phi$ be a homeomorphism $J \leftrightarrow J'$. For each $i$, let $G_i'$ be the set of all arcs of the type $g' = \phi(g)$ ($g \in G_i$). For each $i$, let $A_i$ be the annular region

$$\left\{ P \;\middle|\; \frac{i}{i+1} \leqslant \|P\| \leqslant \frac{i+1}{i+2} \right\}.$$

For each arc $g'$ in $J'$, let $B_{g'}$ be the join of $g'$ with the origin, that is, the union of all linear intervals joining the origin to a point of $g'$. For each $g'$ in each $G_i'$, let

$$C_{g'} = A_i \cap B_{g'}.$$

This gives a collection $C_i'$ of 2-cells. Let $L_i$ be the union of the boundaries of the elements of $C_i$. Similarly $L_i'$ for $C_i'$. It is now a straightforward matter to define a homeomorphism

$$\phi: \bigcup L_i \leftrightarrow \bigcup L_i',$$

such that for each $g$, $\phi(\text{Bd } C_g) = \text{Bd } C_{g'}$, where $g' = \phi(g)$. Let $J_0' = \phi(J_0)$, and let $C_0'$ be the closure of the interior of $J_0'$. Since all of the sets $C_0, C_0', C_g, C_{g'}$ are 2-cells, the homeomorphism $\phi$ can be extended so that $\phi(C_0) = C_0'$ and $\phi(C_g) = C_{g'}$ for each $g$ (Theorem 5.6). Finally, this $\phi$ fits together with the given $\phi: J \leftrightarrow J'$ to give a homeomorphism $\phi: \bar{I} \leftrightarrow B^2$, establishing that $\bar{I}$ is a 2-cell.
