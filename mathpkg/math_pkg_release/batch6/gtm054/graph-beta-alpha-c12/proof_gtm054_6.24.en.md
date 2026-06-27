---
role: proof
locale: en
of_concept: graph-beta-alpha-c12
source_book: gtm054
source_chapter: "6"
source_section: "Section 24"
---

(a) Clearly every maximal independent vertex set is externally stable.
(b) The argument is the same as in (a).
(c) Consider a smallest externally stable set $V_1$ of vertices of $\Gamma$ and let $V_2 = V + V_1$. Let $\mathcal{F}$ be the subset of $\mathcal{E}$ consisting of edges incident with one vertex in $V_1$ and one vertex in $V_2$. Then $B = \{V_1, V_2\}, \mathcal{F}$ is a bipartite graph, and by the Main Matching Theorem,

$$\beta_{00}(\Gamma) - \delta_1(B) = |V_1| - \delta_1(B) = \alpha_1(B) \leq \alpha_1(\Gamma).$$

It suffices to show that $\delta_1(B) = 0$. Suppose that in $B$, $\delta(U) > 0$ for some $U \subseteq V_1$, and let $W = V_1 + U + N(U)$. Then $|W| < |V_1|$, and since $\Gamma$ has no isolated vertices, $W$ is externally stable, contrary to the definition of $V_1$.
