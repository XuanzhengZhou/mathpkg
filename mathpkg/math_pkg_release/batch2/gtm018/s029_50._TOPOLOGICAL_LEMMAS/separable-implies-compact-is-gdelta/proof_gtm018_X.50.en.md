---
role: proof
locale: en
of_concept: separable-implies-compact-is-gdelta
source_book: gtm018
source_chapter: "X"
source_section: "50"
---

If a point $x$ of $X$ is not in $C$, then there exist two disjoint open sets separating $x$ and $C$ (since $X$ is a locally compact Hausdorff space, it is completely regular, hence regular). For each $x \notin C$, choose an open neighborhood $V_x$ of $x$ whose closure is disjoint from $C$, i.e., $\overline{V_x} \cap C = \emptyset$. Then

$$C = \bigcap_{x \notin C} (X - \overline{V_x}).$$

Since $X$ is separable, the open cover $\{V_x : x \notin C\}$ of $X - C$ has a countable subcover. Thus $C$ is a countable intersection of closed sets whose complements are the closures of the countably many $V_x$, making $C$ a $G_\delta$. Alternatively, one may apply Theorem C: the result is easy to prove directly, and Theorem C also yields that the class of all compact $G_\delta$'s is closed under finite unions and countable intersections.
