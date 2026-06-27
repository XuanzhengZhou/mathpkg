---
role: proof
locale: en
of_concept: gamma-belong-vertex-b22
source_book: gtm054
source_chapter: "7"
source_section: "Section 33"
---

Since $\Gamma$ contains a 5-critical subgraph on the same vertex set, it is biconnected. By Lemma IIIE21, the edges in the vertex cocycle of $x$ may be denoted by $E_0, E_1, \ldots, E_{\rho(x)-1}$ so that for some triangular imbedding, $E_i$ and $E_{i+1}$ lie on a common region (where subscripts are read modulo $\rho(x)$). Let $E_i = \{x, y_i\}$ for $i = 0, 1, \ldots, \rho(x) - 1$. Since every region is a 3-cycle, $\{y_0, y

incident, since condition (ii) fails. By Lemma B22, each such vertex $u$ is incident with at most two 6-valent vertices. Thus $3 \leq n(u) \leq 5$ for all $u \in U$.

Let us now define $g: V \rightarrow \mathbb{Q}$ by

$$g(x) = \begin{cases} -1 & \text{if } \rho(x) = 5, \\ 0 & \text{if } \rho(x) = 6, \\ \sum_{u \in U(x)} 1/n(u) & \text{if } \rho(x) \geq 7. \end{cases}$$

Appel and Haken refer to $g$ as a "discharging function"; one imagines each vertex of $\Gamma$ as possessing a certain amount of "charge" and that the function $g$ removes one unit of charge from each 5-valent vertex $u$ and redistributes it by transferring $1/n(u)$ units to each of the $n(u)$ vertices incident with $u$ having valence at least 7. Thus there is no net change in "charge" of the whole graph. In other words, $\sum_{x \in V} g(x) = 0$. Now let us define $h: V \rightarrow \mathbb{Q}$ by $h = f + g$, whence it follows that $\sum_{x \in V} h(x) = 12$. We shall obtain a contradiction by showing that $h(x) \leq 0$ for all $x \in V$.

One verifies easily that $h(x) = 0$ if $\rho(x) = 5$ or 6. Let $x \in V$ and suppose $\rho(x) \geq 7$. Since no two 5-valent vertices are incident while $\Gamma_{N(x)}$ is an elementary circuit, it follows that $|U(x)| \leq \rho(x)/2$. Since $n(u) \geq 3$ for all $u \in U(x)$, we have

$$g(x) = \sum_{u \in U(x)} \frac{1}{n(u)} \leq \frac{[\rho(x)/2]}{3} \leq \frac{\rho(x)}{6

sum is the cycle $\{y_0, y_1\}, \{y_1, y_2\}, \ldots, \{y_5, y_0\}$. (The set of vertices on the corresponding circuit is $S_4$.) It follows that $\Theta_{((x_0, \ldots, x_4))}$ has a planar imbedding in which this cycle is a region. Let $\Theta'$ be formed from $\Theta_{((x_0, \ldots, x_4))}$, by adjoining any of the edges $\{y_0, y_2\}, \{y_0, y_3\}, \{y_0, y_4\}$ not already in $\Theta$. Clearly $\Theta'$ is planar. Since $\nu_0(\Theta') < \nu_0(\Theta) = m$, there exists a vertex $k$-coloring $h$ of $\Theta'$ for some $k \leq 4$. Clearly $h$ is also a $k$-coloring of $\Theta_{((x_0, \ldots, x_4))}$. Using colors from the set $\{0, 1, 2, 3\}$, we list in Table B26 the six possible restrictions of $h$ to $S_4$ subject to permutations of the colors or the permutation on $S_4$ given by $(y_1, y_5)(y_2, y_4)$, which is extendable to a vertex-automorphism of $\Gamma_4$. In all but the first case, $h$ is easily extended to a 4-coloring of $\Theta$, as indicated in the table, yielding a contradiction. Hence, the restriction to $S_4$ of every vertex
