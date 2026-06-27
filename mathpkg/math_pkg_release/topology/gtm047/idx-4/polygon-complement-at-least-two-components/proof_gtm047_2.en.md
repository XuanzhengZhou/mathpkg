---
role: proof
locale: en
of_concept: polygon-complement-at-least-two-components
source_book: gtm047
source_chapter: "2"
source_section: "Separation Properties of Polygons in R^2"
---

We choose the axes in general position, in the sense that no horizontal line contains more than one of the vertices of $J$. (This can be done, because there are only a finite number of directions that we need to avoid. Hereafter, the phrase "in general position" will be defined in a variety of ways, in a variety of cases. In each case, the intuitive meaning will be the same: general position is a situation which occurs with probability $1$ when certain choices are made at random.)

For each point $P$ of $\mathbf{R}^2$, let $L_P$ be the horizontal line through $P$. The index $\operatorname{Ind} P$ of a point $P$ of $\mathbf{R}^2 - J$ is defined as follows.

(1) If $L_P$ contains no vertex of $J$, then $\operatorname{Ind} P$ is the number of points of $L_P \cap J$ that lie to the left of $P$, reduced modulo $2$. Thus $\operatorname{Ind} P$ is $0$ or $1$.

(2) If $L_P$ contains a vertex of $J$, then $\operatorname{Ind} P$ is the number of points of $L' \cap J$, lying to the left of $P$, reduced modulo $2$, where $L'$ is a horizontal line lying "slightly above" or "slightly below" $L_P$. Here the phrases in quotation marks mean that no vertex of $J$ lies between $L_P$ and $L'$.

The function $f(P) = \operatorname{Ind} P$ is a continuous mapping: if $\operatorname{Ind} P = i$, then $\operatorname{Ind} P' = i$ when $P'$ is sufficiently close to $P$. The set $f^{-1}(0)$ is nonempty; every point above all of $J$ belongs to $f^{-1}(0)$. To show that $f^{-1}(1) \neq \emptyset$, let $Q$ be a point of $J$ such that $L_Q$ contains no vertex of $J$. Let $P_1$ be the leftmost point of $J$ on $L_Q$. Let $P$ be a point of $L_Q$, slightly to the right of $P_1$, in the sense that $P \notin J$, and no point between $P_1$ and $P$ belongs to $J$. Then $\operatorname{Ind} P = 1$.

Therefore $\mathbf{R}^2 - J$ is not connected; it is the union of the disjoint nonempty open sets $f^{-1}(0)$ and $f^{-1}(1)$. $\square$
