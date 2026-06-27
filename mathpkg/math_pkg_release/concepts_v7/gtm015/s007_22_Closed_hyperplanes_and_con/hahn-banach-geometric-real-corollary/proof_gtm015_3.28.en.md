---
role: proof
locale: en
of_concept: hahn-banach-geometric-real-corollary
source_book: gtm015
source_chapter: "3"
source_section: "28"
---

# Proof of Existence of continuous linear form positive on open convex set

Let $E$ be a TVS over $\mathbb{R}$, let $A$ be a nonempty open convex set in $E$, and let $M$ be a linear subspace such that $M \cap A = \varnothing$. By (28.1), there exists a closed hyperplane $H$ with $H \supset M$ and $H \cap A = \varnothing$. Let $g$ be a continuous linear form with $H = \{x : g(x) = 0\}$ (so $g = 0$ on $M$). Since $H \cap A = \varnothing$, $0 \notin g(A)$. Since $A$ is convex and $g$ is linear, $g(A)$ is a convex subset of $\mathbb{R}$ not containing $0$, therefore $g(A) \subset (0, \infty)$ or $g(A) \subset (-\infty, 0)$. In the first case $g > 0$ on $A$; in the second case $-g$ is positive on $A$. Thus there exists a continuous linear form (either $g$ or $-g$) that is zero on $M$ and strictly positive on $A$.
