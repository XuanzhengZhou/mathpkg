---
role: proof
locale: en
of_concept: gamma-planar-vertex-b5
source_book: gtm054
source_chapter: "7"
source_section: "Section 32"
---

Let $x_1, \ldots, x_m$ be the vertices incident with $x_0$ and let $h: V + \{x_0\} \rightarrow \{1, 2, 3, 4\}$ be a $\chi_0(\Gamma_{x_0})$-coloring of $\Gamma_{x_0}$. If $|h[V + \{x_0\}]| < 4$, then it is clear that $h$ can be extended to a vertex $n$-coloring of $\Gamma$ with $n \leq 4$. Hence it may be assumed that $m = 4$ and that $h$ is a 4-coloring of $\Gamma_{x_0}$ such that $h(x_i) = i$ ($i = 1, 2, 3, 4$). If $\chi_0(\Gamma) > 4$, then there exists a 5-coloring $h_0: V \rightarrow \{0, 1, \ldots, 4\}$ of $\Gamma$ such that

$$h_0(x) = \begin{cases} 0 & \text{if } x = x_0; \\ h(x) & \text{if } x \in V + \{x_0\}. \end{cases}$$

Without loss of generality, assume that there are faces $Z_i$ incident with edges $\{x_0, x_i\}$ and $\{x_0, x_{i+1}\}$ ($i = 1, \ldots, 4$; $x_5 = x_1$). We again invoke Lemma A11b and continue exactly as in the proof of Theorem B3.

If a planar graph $\Gamma$ were a counter-example to the Four-Color Conjecture, then by B5, any subgraph of $\Gamma$ obtained by deleting vertices of valence 4 or
