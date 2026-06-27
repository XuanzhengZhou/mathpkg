---
role: proof
locale: en
of_concept: uniform-boundedness-theorem-locally-convex
source_book: gtm036
source_chapter: "12"
source_section: "12.4"
---

Let $V$ be a closed, convex and circled neighborhood of $0$ in $H$ (such neighborhoods form a base at $0$ since $H$ is locally convex). Define $W = \bigcap\{f^{-1}[V] : f \in F\}$.

Since each $f$ is continuous and $V$ is closed, each $f^{-1}[V]$ is closed; hence $W$ is closed. Since each $f$ is linear and $V$ is convex and circled, each $f^{-1}[V]$ is convex and circled; hence $W$ is convex and circled.

By Theorem 12.1(iv), since $F$ is pointwise bounded on $A$, the set $W$ absorbs each point of $A$. In view of Corollary 10.3 (the absorption theorem), since $A$ is convex, circled, bounded, sequentially closed and sequentially complete, and $W$ is a closed, convex, circled set that absorbs each point of $A$, the set $W$ absorbs the entire set $A$.

That $W$ absorbs $A$ means: there exists a scalar $t$ such that $A \subset tW$. Then for every $f \in F$, we have $f[A] \subset t f[W] \subset t V$. Thus $F[A] \subset t V$, which means $F[A]$ is bounded in $H$. By Theorem 12.1(iii), this is equivalent to $F$ being uniformly bounded on $A$.
