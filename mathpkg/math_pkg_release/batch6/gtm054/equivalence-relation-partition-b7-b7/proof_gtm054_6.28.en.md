---
role: proof
locale: en
of_concept: equivalence-relation-partition-b7-b7
source_book: gtm054
source_chapter: "6"
source_section: "Section 28"
---

As in earlier proofs in this chapter, we may assume that $\Gamma = (V, D)$.

Suppose that an $m$-family $\mathcal{F}$ of disjoint AZ-paths has been given. Since we have not assumed that $A$ and $Z$ are disjoint, $\mathcal{F}$ may contain some paths of length 0. Any vertex comprising such a trivial path belongs to neither $V + Z$ nor $V + A$, and so we may assume that if $x \in V + Z$, then either $x$ lies on no path in $\mathcal{F}$ or there exists an edge $(x, x')$ on some path in $\mathcal{F}$. In the former case, let $b(x) = x$ and in the latter case let $b(x) = x'$. The paths are disjoint and, except for the trivial ones, they are $[A \cap (V + Z)][Z \cap (V + A)]$-paths. Hence $b$ is a bijection.

Conversely, let the bijection $b$

Thus $\Gamma$ is connected if and only if $\Gamma$ is 1-connected. If $\Gamma$ is $n$-connected and $0 \leq m \leq n$, then $\Gamma$ is $m$-connected.

If $\Gamma$ is $n$-connected but not $(n + 1)$-connected, we say that $\Gamma$ has connectivity (sometimes called "vertex-connectivity") equal $n$, and we write,

$$\kappa(\Gamma) = n.$$

For example, $\kappa(K_n) = n - 1$ for $n = 2, 3, \ldots$.
