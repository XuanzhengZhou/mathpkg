---
role: proof
locale: en
of_concept: connectivity-upper-bound
source_book: gtm054
source_chapter: "VI"
source_section: "C"
---

If $\Gamma$ is complete with $|V| = n$, then any set $S \subseteq V$ of size $n-2$ leaves a subgraph on $2$ vertices, which is connected (since the two remaining vertices are adjacent). Hence $\Gamma$ is $(n-1)$-connected. But $\Gamma$ cannot be $n$-connected because removing $n-1$ vertices leaves a single vertex (which is trivially connected), yet removing all $n$ vertices is impossible — the condition $|V| \geq n+1$ for $n$-connectedness fails. Thus $\kappa(\Gamma) = n - 1 = |V| - 1$.

Conversely, if $\kappa(\Gamma) = |V| - 1$, then $\Gamma$ must be $(|V|-1)$-connected. In particular, removing any set of $|V|-2$ vertices leaves a connected subgraph on $2$ vertices, so those two vertices must be adjacent. Hence every pair of vertices is adjacent, and $\Gamma$ is complete.
