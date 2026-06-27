---
role: proof
locale: en
of_concept: uniformly-locally-compact-decomposition
source_book: gtm027
source_chapter: "6"
source_section: "T"
---

# Proof: Decomposition of Uniformly Locally Compact Spaces

Let $(X, \mathfrak{U})$ be a uniformly locally compact space. By part (a), for each $U \in \mathfrak{U}$ and each $x \in X$, the set $C(x) = \bigcup_{n \in \omega} U^n[x]$ is clopen.

Since $U[x]$ is compact for a suitably chosen $U$, each component of the "uniform connectedness" relation defined by $U$ is clopen and, by part (c), $\sigma$-compact (being connected in the induced uniformity).

The space $X$ is then partitioned into the clopen $\sigma$-compact components. These form a disjoint open family. Since each such component is $\sigma$-compact (hence Lindelöf, hence paracompact), and the family itself is disjoint, $X$ is paracompact.

Thus each uniformly locally compact space is the union of a disjoint open family of $\sigma$-compact subspaces, and is therefore paracompact.
