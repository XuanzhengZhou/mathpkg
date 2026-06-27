---
role: proof
locale: en
of_concept: classification-of-0-deficient-3-4-graphs
source_book: gtm054
source_chapter: "VIII"
source_section: "C"
---

Let $\Gamma = (V, \mathcal{E})$ be a $0$-deficient $(3,4)$-graph; thus $\nu_0(\Gamma) = n(3,4)-1 = 8$. Let $x \in V$. By Lemma C9c, $3 \geq \rho(x) \geq 2$.

**Case 1: there exists a vertex of valency 2.** Let $\rho(x) = 2$ and let $y$ and $z$ be the vertices incident with $x$. Set $T = V \setminus \{x, y, z\}$. By Lemma C9a, $\Gamma_T$ is a $0$-deficient $(3,3)$-graph, which by Exercise C8b must be a $5$-circuit. Thus $\Gamma$ contains as a subgraph the $5$-circuit on vertices $a, b, c, d, e$ (the set $T$), together with $x$ connected to $y, z$, and a set $\mathcal{F}$ of edges such that for each $F \in \mathcal{F}$, one vertex of $F$ is in $\{y, z\}$ and the other is in $\{a, b, c, d, e\}$.

Since each vertex has valence $2$ or $3$ by C9c, $y$ and $z$ must each be incident with either one or two edges in $\mathcal{F}$, and each of $a, b, c, d, e$ can be incident with at most one edge in $\mathcal{F}$. One, two, or three of the vertices $a, b, c, d, e$ are incident with no edge in $\mathcal{F}$. Without loss of generality, $a$ is incident with neither $y$ nor $z$.

Assume without loss of generality that $z$ has valence $3$ (since $\Gamma$ is $3$-regular only on average). Since $\Gamma$ contains no complete $3$-set, $z$ is incident with $b$ and $d$ or with $c$ and $e$; for definiteness say $z$ is incident with $c$ and $e$. Finally, $y$ is incident with $d$ and possibly with $b$. Without the edge $\{y, b\}$ we obtain the graph $\Theta_8$, and with $\{y, b\}$ we obtain $\Theta_8'$.

**Case 2: all vertices are $3$-valent.** Let $w \in V$ and suppose $w$ is incident with $x, y, z$. Let $T = V \setminus \{w, x, y, z\}$. Since $\{x, y, z\}$ must be an independent set (otherwise $\Gamma$ would contain a triangle), the number of edges in $\Gamma_T$ is $|\mathcal{E}| - (\rho(x) + \rho(y) + \rho(z)) = 12 - 9 = 3$ (since $|\mathcal{E}| = 3 \times 8 / 2 = 12$ by $3$-regularity). By Exercise C8c, $\Gamma_T$ is a path of length $3$ (the unique $1$-deficient $(3,3)$-graph with exactly three edges).

Thus $\Gamma$ contains as a subgraph a path of length $3$ on vertices $a, b, c, d$ (the set $T$), together with six edges each having one vertex in $T$ and the other in $\{x, y, z\}$. Since $\Gamma$ contains no triangle, the two vertices of $T$ joined to each vertex in $\{x, y, z\}$ must be one of the three pairs $\{a, c\}$, $\{b, d\}$, and $\{a, d\}$. Each pair must be used exactly once to preserve $3$-regularity. Any of the $3!$ assignments yields the graph $\Theta_8''$.
