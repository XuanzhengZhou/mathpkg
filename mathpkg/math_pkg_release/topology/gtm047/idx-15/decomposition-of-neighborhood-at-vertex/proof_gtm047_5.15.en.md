---
role: proof
locale: en
of_concept: decomposition-of-neighborhood-at-vertex
source_book: gtm047
source_chapter: "5"
source_section: "15"
---

If this is false, then $N_v - \bigcup e'_j$ has a component $V$, different from each of the sets $I_i$. Therefore $\operatorname{Fr} V \subset \bigcup e'_j$. But $\operatorname{Fr} V$ cannot lie in any one set $e'_j$, because no arc separates $\mathbf{R}^2$. Let $P$ and $Q$ be points of $e'_i - \{v\}$ and $e'_j - \{v\}$ respectively, lying in $\operatorname{Fr} V$, with $i \neq j$. Let $X$ and $Y$ be points of $J_v - \{w_k\}$, such that $\{X, Y\}$ separates $w_i$ from $w_j$ in $J_v$. By two applications of the Schönflies theorem, there is an arc $A$ from $X$ to $Y$, intersecting $J_v$ only at $X$ and $Y$, and intersecting $\bigcup e'_k$ only at $v$. Then $P$ and $Q$ lie in different components of $N_v - A$, contradicting that they both lie in $\operatorname{Fr} V$ (since $A$ does not separate them from each other in $V$).

Therefore $\operatorname{Fr} V$ must lie in a single $e'_j$, which is impossible. Hence $N_v = \bigcup \overline{I}_i$.
