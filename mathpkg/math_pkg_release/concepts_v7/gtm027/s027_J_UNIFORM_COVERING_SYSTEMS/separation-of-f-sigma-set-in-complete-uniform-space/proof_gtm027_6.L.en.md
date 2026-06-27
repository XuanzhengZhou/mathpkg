---
role: proof
locale: en
of_concept: separation-of-f-sigma-set-in-complete-uniform-space
source_book: gtm027
source_chapter: "6"
source_section: "L"
---

# Proof of Separation of $F_\sigma$ Sets in Complete Uniform Spaces

Let $(X, \mathfrak{U})$ be a complete uniform space, let $F$ be an $F_\sigma$ (a countable union of closed sets), and let $x \in X \setminus F$.

Write $F = \bigcup_{n \in \omega} F_n$ where each $F_n$ is closed. Since $x \notin F$, we have $x \notin F_n$ for each $n$.

For each $n$, since $F_n$ is closed, there exists a uniformly continuous function $f_n: X \to [0, 1]$ such that $f_n(x) = 0$ and $f_n(y) = 1$ for all $y \in F_n$ (this follows from complete regularity of uniform spaces). Define

$$f(y) = \sum_{n=0}^{\infty} 2^{-n-1} f_n(y).$$

Then $f$ is uniformly continuous, $f(x) = 0$, and $f(y) > 0$ for all $y \in F$ (since each $y \in F$ belongs to some $F_n$, hence $f_n(y) = 1$, giving $f(y) \geq 2^{-n-1} > 0$).

Consequently, there is an open set $V = \{y : f(y) > 0\}$ containing $F$ with $x \notin V$. Using the device of 6.K(a), one can construct a uniformity $\mathfrak{V}$ for $V$ such that $(V, \mathfrak{V})$ is complete and the topology of $\mathfrak{V}$ is identical with the relativized topology of $\mathfrak{U}$.

The construction uses the fact that $V$ is a cozero set (a countable union of closed sets in a complete uniform space can be separated from a point outside it by a continuous function). The uniformity $\mathfrak{V}$ is obtained by restricting the hyperspace construction to $V$.
