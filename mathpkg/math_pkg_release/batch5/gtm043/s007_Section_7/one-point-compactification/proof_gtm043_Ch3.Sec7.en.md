---
role: proof
locale: en
of_concept: one-point-compactification
source_book: gtm043
source_chapter: "3"
source_section: "7"
---

Adjoin a single new point, denoted $\infty$, to $X$. Define $X^* = X \cup \{\infty\}$. Declare a subset $U \subset X^*$ to be open if either $U \subset X$ and $U$ is open in $X$, or $\infty \in U$ and $X^* - U$ is a compact subset of $X$. One verifies that this defines a topology on $X^*$ under which $X^*$ is compact (any open cover of $X^*$ includes a neighborhood of $\infty$ whose complement is compact, hence finitely coverable). Since $X$ is locally compact, $X^*$ is Hausdorff (any point $x \in X$ has a compact neighborhood $K$ in $X$, and $X^* - K$ is a neighborhood of $\infty$ disjoint from the interior of $K$). Thus $X^*$ is a compactification of $X$. Consequently, $X$ is a subspace of the compact Hausdorff space $X^*$, and therefore $X$ is completely regular.
