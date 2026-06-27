---
role: proof
locale: en
of_concept: deficient-graphs-theta-c12
source_book: gtm054
source_chapter: "8"
source_section: "Section 37"
---

Let $\Gamma = (V, \mathcal{E})$ be a 0-deficient (3, 4)-graph; thus $\nu_0(\Gamma) = 8$. Let $x \in V$. By Lemma C9c, $3 \geq \rho(x) \geq 2$.

Case 1: there exists a vertex of valence 2. Let $\rho(x) = 2$ and let $y$ and $z$ be incident with $x$. If $T = V + \{x, y, z\}$, then by Lemma C9a, $\Gamma_T$ is a 0-deficient (3, 3)-graph, which by Exercise C8b must be a 5-circuit. Thus $\Gamma$ must contain the subgraph shown in Figure C13, together with a set $\mathcal{F}$ of edges such that for each $F \in \mathcal{F}$, one vertex of $F$ is in $\{y, z\}$ and the other is in $\{a, b, c, d, e\}$. Since by C9c each vertex has valence 2 or 3, $y$ and $z$ must each be incident with either one or two edges in $\mathcal{F}$, and each of $a, b, c, d$, and $e$ can be incident with at most one edge in $\mathcal{F}$. We conclude that one, two, or three of the vertices $a, b, c, d$, and $e$ are incident with no edge in $\mathcal{F}$. Without loss of generality we may assume that $a$ is incident with neither $y$ nor $z$. If $c$ (or $d$) were incident with neither $y$ nor $z

We may further assume without loss of generality that $z$ has valence 3. Since $\Gamma$ contains no complete 3-set, $z$ is incident with $b$ and $d$ or with $c$ and $e$. For definiteness say $z$ is incident with $c$ and $e$. Finally, $y$ is incident with $d$ and possibly with $b$. Without the edge $\{y, b\}$ we have $\Theta_8$ and with $\{y, b\}$ we have $\Theta_8'$.

Case 2: all vertices are 3-valent. Let $w \in V$ and suppose $w$ is incident with $x, y,$ and $z$. Let $T = V + \{w, x, y, z\}$. Since $\{x, y, z\}$ must be an independent set, the number of edges in $\Gamma_T$ is $|\mathcal{E}| - (\rho(x) + \rho(y) + \rho(z)) = 12 - 9 = 3$. By Exercise C8c, $\Gamma_T$ is a path of length 3. Thus $\Gamma$ must contain the subgraph in Figure C14, together with six edges each having one vertex in $T$ and the other in $\{x, y, z\}$. Since $\Gamma$ contains no complete 3-set, the two vertices of $\Gamma_T$ joined to each vertex in $\{x, y, z\}$ must be one of the three pairs $\{a, c\}, \{b, d\},$ and $\{a, d\}$. Moreover, each pair must be used exactly once in order to preserve isovalence. For example, the six edges in question could be: $\{x, a\}, \{x, c\}, \{y, b\}, \{y, d\}, \{z, a\}, \{z, d\}$, but any of the 3! possibilities yields the graph $\Theta_8''$.
