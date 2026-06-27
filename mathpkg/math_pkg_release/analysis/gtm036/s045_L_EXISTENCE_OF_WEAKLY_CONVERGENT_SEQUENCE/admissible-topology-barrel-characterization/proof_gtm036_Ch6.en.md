---
role: proof
locale: en
of_concept: admissible-topology-barrel-characterization
source_book: gtm036
source_chapter: "Chapter 6: Admissible Topologies"
source_section: ""
---

Suppose $\mathcal{T}_{\mathcal{S}}$ is an admissible topology for $E$. Recall from Theorem 16.1(iv) that a function $R$ from a topological space $Z$ to $E$ is continuous relative to the $w(E,F)$-topology for $E$ if and only if the map $z \mapsto \langle R(z), f \rangle$ is continuous on $Z$ for each $f \in F$. Applying this theorem to the identity map of $E$, with topology $\mathcal{T}_{\mathcal{S}}$, into $E$ with topology $w(E,F)$, shows that $\mathcal{T}_{\mathcal{S}}$ is stronger than $w(E,F)$.

A local base for $\mathcal{T}_{\mathcal{S}}$ is the family of finite intersections of non-zero scalar multiples of polars of members of $\mathcal{A}$, where $\mathcal{A}$ is a family of $w(F,E)$-bounded subsets of $F$ whose polars define $\mathcal{T}_{\mathcal{S}}$. Since members of $\mathcal{A}$ are bounded, by Theorem 16.4 the polars of members of $\mathcal{A}$ are $w(E,F)$-barrels. The local base just described therefore consists of $w(E,F)$-barrels.

Conversely, if $\mathcal{T}$ is stronger than $w(E,F)$ and has a local base of $w(E,F)$-barrels, then each member of such a local base is the polar of some $w(F,E)$-bounded set (by the bipolar theorem), so $\mathcal{T}$ is a topology of uniform convergence on $w(F,E)$-bounded sets and hence admissible.
