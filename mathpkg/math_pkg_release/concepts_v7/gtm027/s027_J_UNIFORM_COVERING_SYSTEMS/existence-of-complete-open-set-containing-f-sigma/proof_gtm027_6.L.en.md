---
role: proof
locale: en
of_concept: existence-of-complete-open-set-containing-f-sigma
source_book: gtm027
source_chapter: "6"
source_section: "L"
---

# Proof of Existence of Complete Open Set Containing an $F_\sigma$ Set

From part (b), let $F$ be an $F_\sigma$ in a complete uniform space $(X, \mathfrak{U})$ and let $x \in X \setminus F$. There exists a continuous real-valued function $f$ on $X$ which is positive on $F$ and $0$ at $x$.

Set $V = \{y \in X : f(y) > 0\}$. Then $V$ is an open set containing $F$ with $x \notin V$.

Using the device of 6.K(a), one constructs a uniformity $\mathfrak{V}$ for $V$ such that $(V, \mathfrak{V})$ is complete and the topology of $\mathfrak{V}$ is identical with the relativized topology of $\mathfrak{U}$. The construction uses the embedding of $V$ as a closed subset of the product $X \times \mathbb{R}^{\omega}$ via the map

$$y \mapsto (y, f_1(y), f_2(y), \ldots)$$

where $f_n$ are appropriately chosen. Since $X$ is complete and $V$ corresponds to a closed subset of a complete space under this embedding, $(V, \mathfrak{V})$ is complete.
