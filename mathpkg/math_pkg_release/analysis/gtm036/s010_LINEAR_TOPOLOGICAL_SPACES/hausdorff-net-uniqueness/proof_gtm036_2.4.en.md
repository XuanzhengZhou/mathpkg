---
role: proof
locale: en
of_concept: hausdorff-net-uniqueness
source_book: gtm036
source_chapter: "2"
source_section: "4"
---
If $X$ is Hausdorff and a net $\{x_\alpha\}$ converges to both $x$ and $y$ with $x \neq y$, then there exist disjoint open neighborhoods $U$ of $x$ and $V$ of $y$. The net must eventually lie in $U$ and also eventually lie in $V$. For sufficiently large indices, the net lies in $U \cap V$, contradicting disjointness. Thus limits are unique.

Conversely, if $X$ is not Hausdorff, there exist distinct points $x$ and $y$ such that every neighborhood of $x$ meets every neighborhood of $y$. Consider the directed set of pairs $(U,V)$ of neighborhoods of $x$ and $y$ respectively, ordered by $(U,V) \geq (U',V')$ iff $U \subseteq U'$ and $V \subseteq V'$. For each such pair, choose $x_{(U,V)} \in U \cap V$. This net converges to both $x$ and $y$, so limits are not unique.
