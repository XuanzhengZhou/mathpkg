---
role: proof
locale: en
of_concept: lemma-11
source_book: gtm026
source_chapter: "1"
source_section: "1.17"
---

$S$ is a subsemigroup if $SS \subset S$. Let $F$ be a nonempty closed subsemigroup. By a similar proof to the one above, $F$ possesses a minimal closed subsemigroup $S$. For $p$ in $S$, $\varnothing \neq pS \subset S$, $(pS)(pS) \subset pSSS \subset pS$ and $pS$ is closed, so $pS = S$ and there exists $u$ in $S$ with $pu = p$. Set $R = \{s \in S: us = u\}$. $R$ is clearly a subsemigroup. As the equalizer of the continuous functions $L_u$ and “constantly $u$,” $R

compactible. For suppose $G$ were provided with a compact Hausdorff topology with all $L_p$ continuous. Since $(L_p)^{-1} = L_q$ with $q = p^{-1}$, $L_p$ is a homeomorphism. Since $\{p\}L_r = \{q\}$ if $r = p^{-1}q$, if any point of $G$ is isolated then all are and $G$ is discrete, a contradiction. It suffices, then, to make the following observation: Every countably infinite compact Hausdorff space has at least one isolated point. For let $X$ be such a space. By the Baire theorem [Kelley '55, Theorem 6.34] every countable family of dense open sets has dense intersection. Since the family of all sets with a finite complement has empty intersection, there exists a finite set $F$ whose complement is not dense. Consequently, there exists a nonempty open subset $G$ of $F$. If $x$ is in $G$, $x$ is an isolated point since $\{x\}$ is the intersection of the open sets $G$, $X - \{x_1\}, \ldots, X - \{x_n\}$ where $G - \{x\} = \{x_1, \ldots, x_n\}$.

1.19 Distal Transformation Groups. A compact transformation group $X$ with phase group $G$ is distal if whenever $x \neq y$ in $X$ there exists a neighborhood $\alpha$ of the diagonal in $X \times X$ such that $(xg, yg) \notin \alpha$ for all $g$ in $G$. The reader should recall that a compact Hausdorff space is uniquely uniformizable with the neighborhoods of the diagonal as the entourages. In the case when $X$ is metric, the condition is “there exists $\varepsilon > 0$ such that $d(xg, yg) > \varepsilon$ for all $g$.” In other words, “distinct points were far apart in the past and will remain far apart in the future.” For example, let $X$ be the annulus, that is the subset of the plane of all points whose polar coordinates $(r, \theta)$ satisfy

First suppose $(X, \xi)$ is distal and consider $p$ in $E$ and $x \neq y$ in $X$. There exists an open neighborhood of the diagonal $\alpha$ such that $(xg, yg) \notin \alpha$ for all $g$ in $G$. $p$ is the pointwise limit of a net $g_i$ with each $g_i$ in $G$. As $\alpha$ is open, $(xp, yp) \notin \alpha$ and in particular $xp \neq yp$. Conversely, suppose each $p$ in $E$ is injective and consider $x \neq y$ in $X$. Suppose that for all neighborhoods of the diagonal $\alpha$, there were some $g_\alpha$ in $G$ with $(xg_\alpha, yg_\alpha) \in \alpha$. By compactness, there exists a subnet $g_\beta$ which converges to some $p$ in $E$. Since the intersection of all closed $\beta$ is the diagonal and since $(xp, yp)$ is in every closed $\beta$, $x = y$.

We have motivated:
