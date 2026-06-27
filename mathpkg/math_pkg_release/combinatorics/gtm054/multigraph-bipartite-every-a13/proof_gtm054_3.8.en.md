---
role: proof
locale: en
of_concept: multigraph-bipartite-every-a13
source_book: gtm054
source_chapter: "3"
source_section: "IIIA"
---

Let $\Gamma = (V, f, E)$. To say that every circuit has even length is by A8 and A9 to say that $\mathcal{X}(\Gamma)$ is an even space, which is equivalent (IIA8 again) to saying that $E \in \mathcal{X}^{\perp}(\Gamma)$. Equivalently, $E = \sum_{x \in U} f^*(x)$ for some $U \subseteq V$. This means that each edge is incident with exactly one vertex in $U$ and that $\{U, V + U\}$ is the required partition of $V$. Conversely, if $\Gamma$ is bipartite with partition $\{U, V + U\}$, then $E = \sum_{x \in U} f^*(x)$, and one pursues the chain of equivalent statements in the reverse direction.
