---
role: proof
locale: en
of_concept: cocycle-space-characterization
source_book: gtm054
source_chapter: "III"
source_section: "D"
---

If $\mathcal{A} = \mathcal{Z}^\perp(\Gamma)$, we have seen that the sets $f^*(x)$ for $x \in V$ satisfy condition (a) and condition (b).

Conversely, assume the existence of $C_1, \ldots, C_m \in \mathcal{A}$ satisfying (a) and (b). Let $V = \{1, \ldots, m\}$ and define $f: E \rightarrow \mathcal{P}(V)$ by
$$f(e) = \{i \in V: e \in C_i\}, \quad \text{for all } e \in E.$$
By (b), the system $\Gamma = (V, f, E)$ is a multigraph. Since $f^*(i) = C_i$ for all $i \in V$, we have $\mathcal{A} = \mathcal{Z}^\perp(\Gamma)$.

For the connectedness claim: if the constructed multigraph is not connected, one can identify vertices to obtain a connected multigraph with the same cocycle space.
