---
role: proof
locale: en
of_concept: separation-closed-convex-compact-convex
source_book: gtm015
source_chapter: "3"
source_section: "34"
---

# Proof of Strict separation of closed convex and compact convex sets

Let $E$ be a locally convex TVS over $\mathbb{R}$, let $A$ and $B$ be nonempty convex sets with $A \cap B = \varnothing$, and suppose that $A$ is closed and $B$ is compact.

Since $A$ is closed and $B$ is compact, there exists a convex, symmetric neighborhood $V$ of $\theta$ such that $(A + V) \cap B = \varnothing$. Then $A + V$ is an open convex set disjoint from $B$. By Theorem (30.6), there exists a closed hyperplane $H$ strictly separating $A + V$ and $B$ (since $A+V$ is open). In particular, $H$ strictly separates $A$ and $B$.

More precisely, there exist a continuous linear form $g$ and a real number $\alpha$ such that $g < \alpha$ on $A$ and $g > \alpha$ on $B$.
