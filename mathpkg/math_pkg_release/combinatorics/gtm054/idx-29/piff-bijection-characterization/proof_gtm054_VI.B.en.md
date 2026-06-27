---
role: proof
locale: en
of_concept: piff-bijection-characterization
source_book: gtm054
source_chapter: "VI"
source_section: "B"
---

As in earlier proofs in this chapter, we may assume that $\Gamma = (V, D)$.

Suppose that an $m$-family $\mathcal{F}$ of disjoint $AZ$-paths has been given. Since we have not assumed that $A$ and $Z$ are disjoint, $\mathcal{F}$ may contain some paths of length $0$. Any vertex comprising such a trivial path belongs to neither $V \setminus Z$ nor $V \setminus A$, and so we may assume that if $x \in V \setminus Z$, then either $x$ lies on no path in $\mathcal{F}$ or there exists an edge $(x, x')$ on some path in $\mathcal{F}$. In the former case, let $b(x) = x$ and in the latter case let $b(x) = x'$. The paths are disjoint and, except for the trivial ones, they are $[A \cap (V \setminus Z)][Z \cap (V \setminus A)]$-paths. Hence $b$ is a bijection.

Conversely, let the bijection $b$ be given. The condition defines a set of edges (or directed edges) from $V \setminus Z$ to $V \setminus A$, which together with the fixed points yields the required $m$-family of disjoint $AZ$-paths.
