---
role: proof
locale: en
of_concept: max-flow-min-cut-theorem-vertex-form
source_book: gtm054
source_chapter: "IV"
source_section: "19"
---

The proof proceeds by reduction to the edge-capacitated Max-Flow–Min-Cut Theorem (C6). Given a directed graph $(V, D)$ with vertex capacity $j$, construct a network $(X, k)$ where each vertex $x \in V$ is replaced by two vertices $x^1, x^2$ connected by an edge $e_x$ of capacity $j(x)$. The edge set $Y$ and capacity $k$ are defined so that each edge $(x, y) \in D$ of the original graph corresponds to an edge from $x^2$ to $y^1$ with infinite capacity. 

Given a feasible flow $h$ in $(V, D)$, define $\bar{h}: Y \to \mathbb{N}$ by:

$$\bar{h}(x^i, y^i) = 0 \quad \text{for all } x, y \in V,\ i \in \{1, 2\},$$
$$\bar{h}(x^1, y^2) = h(x, y) \quad \text{for all } x, y \in V,$$
$$\bar{h}(x^2, y^1) = \begin{cases} h(x) & \text{if } x = y, \\ 0 & \text{if } x \neq y. \end{cases}$$

The mapping $h \mapsto \bar{h}$ is a bijection from the set of feasible flows on $(V, D)$ onto the set of feasible flows on $(X, k)$. Since $h(x_0) = \bar{h}(e_0)$ where $e_0 = (x_0^2, x_0^1)$, the maximum flow values coincide. The vertex-cut $U$ in $(V, D)$ corresponds to a cut $C$ in $(X, k)$ of the form $C = \sum_{x^i \in S} g^*(x^i)$ for some subset $S \subseteq X$ with $x_0^1 \in S$ and $x_0^2 \notin S$. The equivalence of the vertex form and the edge form then follows from Theorem C6.
