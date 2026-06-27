---
role: proof
locale: en
of_concept: between-theorem-for-semicontinuous-functions
source_book: gtm027
source_chapter: "5"
source_section: "X. The Between Theorem for Semi-Continuous Functions"
---

# Proof of the Between Theorem for Semi-Continuous Functions

Let $g$ and $h$ be, respectively, lower and upper semi-continuous real-valued functions on a paracompact space $X$, and suppose that $h(x) < g(x)$ for all $x$ in $X$. We construct a continuous real-valued function $p$ on $X$ such that $h(x) < p(x) < g(x)$ for each $x$.

Let $\mathcal{U}$ be the family of all open subsets $U$ of $X$ such that $\sup_{y \in U} h(y) < \inf_{y \in U} g(y)$. Because $X$ is paracompact and $h$ and $g$ are semi-continuous, $\mathcal{U}$ is an open cover of $X$.

Since $X$ is paracompact, there exists a partition of unity $\mathcal{F}$ subordinate to $\mathcal{U}$. For each $f \in \mathcal{F}$, choose $k_f$ such that if $f(x) \neq 0$, then $h(x) < k_f < g(x)$. This is possible because $f$ is supported in some $U \in \mathcal{U}$, and on $U$ we have $\sup h < \inf g$.

Define $p(x) = \sum \{k_f f(x) : f \in \mathcal{F}\}$. The value of $p$ at a point $x$ is a convex combination (weighted average) of numbers $k_f$, all of which lie strictly between $h(x)$ and $g(x)$. Since a convex combination of numbers in $(h(x), g(x))$ remains in $(h(x), g(x))$, we have $h(x) < p(x) < g(x)$ for each $x$.

The function $p$ is continuous because it is a sum of continuous functions $k_f f(x)$, and the sum is locally finite (since the partition of unity is locally finite).
