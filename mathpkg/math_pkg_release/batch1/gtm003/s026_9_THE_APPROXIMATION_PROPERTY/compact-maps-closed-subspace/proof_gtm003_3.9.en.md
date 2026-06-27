---
role: proof
locale: en
of_concept: compact-maps-closed-subspace
source_book: gtm003
source_chapter: "Chapter III"
source_section: "9. The Approximation Property. Compact Maps"
---

The subset of $\mathcal{L}(E, F)$ consisting of all compact maps is evidently a subspace $M$. Let $u$ be in the closure of $M$ in $\mathcal{L}_b(E, F)$, and let $B$ be the unit ball of $E$. Given any $0$-neighborhood $W$ in $F$, there exists $v \in M$ such that $u(x) - v(x) \in W$ for all $x \in B$. Since $v(B)$ is precompact in $F$, there exist finitely many points $y_1, \ldots, y_n \in F$ such that $v(B) \subset \bigcup_{i=1}^{n} (y_i + W)$. It follows that $u(B) \subset \bigcup_{i=1}^{n} (y_i + 2W)$, showing $u(B)$ is precompact in $F$. Hence $u$ is compact, and $M$ is closed.
