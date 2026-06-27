---
role: proof
locale: en
of_concept: gamma-mathcal-nonplanar-g11
source_book: gtm054
source_chapter: "4"
source_section: "IVA"
---

By Exercise G7a, $\Gamma$ is triconnected. If $\{x, y\} = E \in \mathcal{E}$ and if $\Gamma_{V+E}$ (the graph obtained by deleting the vertices $x$ and $y$) is not biconnected, then by G7b, $x$ and $y$ are incident with a common vertex of valence 3. It follows from Exercise G10 that there exists at least one edge $E_0 = \{x_1, x_2\}$ such that $\Gamma_{V+E_0}$ is biconnected.

Let $\{E_0, E_1^j, E_2^j, \ldots, E_m^j\}$ be the edges incident with $x_j$ ($j = 1, 2$), and let $\mathcal{E}'$ be the set of edges incident with neither $x_1$ nor $x_2$. Let $x_0$ be an element distinct from all other objects under consideration, let $F_i^j = E_i^j + \{x_0, x_j\}$ for $j = 1, 2; i = 1, \ldots, m_j$, and let $\mathcal{F} = \{F_i^j : j = 1, 2; i = 1, \ldots, m_j\}$. Finally let $\Theta = (V + \{x_0, x_1, x_2\}, \mathcal{E}' \cup \mathcal{F})$. Thus $\Theta$ is isomorphic with a subgraph of the contraction of $\Gamma$ obtained by contracting $\{x_1, x_2\}$ to a single vertex. By assumption $\Theta$ is planar.

Let $Z_1, \ldots, Z_m$ be a planar imbedding of $\Theta$. Since $\Gamma$ is biconnected, $\Theta$ is biconnected, and by E9 and B3, this imbed

By direct computation, exactly $\rho(x_1) + \rho(x_2) - 2$ cycles contain edges in $\mathcal{E}''$. Thus one cycle in the list, say $Z_{n+1}$, is contained entirely in $Z$, i.e., $Z_{n+1} = Z$.

We wish to show that $Z_1, \ldots, Z_k, Z_1', \ldots, Z_n'$ is a planar imbedding of $\Gamma$. These are clearly cycles of $\Gamma$. Every edge in $Z + \mathcal{E}'$ belongs to two of the cycles $Z_1, \ldots, Z_k$. Every edge in $\mathcal{E}''$ belongs to two of the cycles $Z_1', \ldots, Z_n'$, and every edge in $Z$ belongs to one of the cycles from each list. Finally, $Z_1, \ldots, Z_k, Z_1', \ldots, Z_n'$ spans $\mathcal{Z}(\Gamma)$ since these cycles clearly satisfy only one relation and since

$$\dim(\mathcal{Z}(\Gamma)) = \nu_1(\Gamma) - \nu_0(\Gamma) + 1$$
$$= \nu_1(\Theta_{(x_0)} + |\mathcal{E}''|) - (\nu_0(\Theta_{(x_0)}) + 2) + 1$$
$$= (\dim \mathcal{Z}(\Theta_{(x_0)}) + |\mathcal{E}''| - 2 = k + n - 1.$$

The necessity of Kuratowski's Theorem as we have stated it follows from Proposition F9. The sufficiency follows from Proposition G11. We leave the proof of Corollary G2 as an exercise for the reader.
