---
role: proof
locale: en
of_concept: lattice-sublattice-uniform-closure-approximation
source_book: gtm036
source_chapter: "24"
source_section: "24.4"
---

If $h$ belongs to the uniform closure of $A$, then for any $\epsilon > 0$ there exists $g \in A$ with $\|g - h\|_\infty < \epsilon/2$. Then $g - \epsilon/2 \leq h \leq g + \epsilon/2$, and taking $g' = g - \epsilon/2$ (which need not belong to $A$, but a suitable modification works) shows the condition is necessary. The essential content is the converse.

Assume that for each $x \in X$ and $\epsilon > 0$ there exists $g \in A$ such that $g(x) = h(x)$ and $g(y) \leq h(y) + \epsilon$ for all $y \in X$. Given $\epsilon > 0$, for each $x \in X$ choose $g_x \in A$ such that $g_x(x) = h(x)$ and $g_x(y) \leq h(y) + \epsilon$ for all $y \in X$.

For each $y \in X$, there exists an open neighborhood $U_{x,y}$ of $y$ such that $g_x(z) \geq h(y) - \epsilon$ for $z \in U_{x,y}$, by continuity of $g_x$ and the inequality $g_x(y) \leq h(y) + \epsilon$ together with the fact that $g_x(x) = h(x)$. By compactness of $X$, for fixed $x$ there exist $y_1, \ldots, y_n$ such that $X = \bigcup_{i=1}^n U_{x,y_i}$. Define $V_x = \bigcap_{i=1}^n U_{x,y_i}$. Then $V_x$ is an open neighborhood of $x$ and
$$
g_x(y) \geq h(y) - \epsilon \quad \text{for all } y \in V_x.
$$

Since $X$ is compact, there exist $x_1, \ldots, x_m$ such that $X = \bigcup_{j=1}^m V_{x_j}$. Set
$$
g = g_{x_1} \vee g_{x_2} \vee \cdots \vee g_{x_m}.
$$
Since $A$ is closed under finite suprema, $g \in A$. Moreover, for any $y \in X$,
$$
h(y) - \epsilon \leq g(y) \leq h(y) + \epsilon,
$$
because $y \in V_{x_j}$ for some $j$ implies $g(y) \geq g_{x_j}(y) \geq h(y) - \epsilon$, and each $g_{x_j}(y) \leq h(y) + \epsilon$. Hence $\|g - h\|_\infty \leq \epsilon$, proving that $h$ belongs to the uniform closure of $A$.
