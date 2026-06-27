---
role: proof
locale: en
of_concept: bipartite-even-circuits-theorem
source_book: gtm054
source_chapter: "III"
source_section: "A"
---

Let $\Gamma = (V, f, E)$ be a multigraph.

To say that every circuit has even length is, by Propositions A8 and A9, to say that $\mathcal{X}(\Gamma)$ (the cycle space) is an even space. By IIA8, this is equivalent to saying that $E \in \mathcal{X}^{\perp}(\Gamma)$ (the edge set is in the orthogonal complement of the cycle space).

Equivalently, $E = \sum_{x \in U} f^*(x)$ for some $U \subseteq V$. This means that each edge is incident with exactly one vertex in $U$, so that $\{U, V \setminus U\}$ is the required bipartition of $V$: every edge has one endpoint in $U$ and one endpoint in $V \setminus U$.

Conversely, if $\Gamma$ is bipartite with partition $\{U, V \setminus U\}$, then $E = \sum_{x \in U} f^*(x)$, and one follows the chain of equivalent statements in the reverse direction to conclude that every circuit has even length.
