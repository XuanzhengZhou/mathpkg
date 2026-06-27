---
role: proof
locale: en
of_concept: prime-z-filter-unique-cluster-point
source_book: gtm043
source_chapter: "3"
source_section: "7"
---

Suppose $p$ and $q$ are distinct cluster points of a prime $z$-filter $\mathcal{F}$. Since $X$ is completely regular, there exists a neighborhood of $p$ of the form $X - Z$, where $Z$ is a zero-set containing $q$. Since $V \cup Z = X$, either $V$ or $Z$ belongs to the prime $z$-filter $\mathcal{F}$. But $Z$ cannot belong to $\mathcal{F}$, because $p \notin Z$. So $V \in \mathcal{F}$. Thus $\mathcal{F}$ contains a neighborhood of $p$ disjoint from a member of $\mathcal{F}$ (namely $Z$), which contradicts that $q$ is a cluster point. Therefore $\mathcal{F}$ can have at most one cluster point.

As a consequence, in a completely regular space, a $z$-ultrafilter can have at most one cluster point. It need not have any: the family of all zero-sets in $\mathbf{R}$ whose complements are bounded is a $z$-filter without a cluster point, and any $z$-ultrafilter containing it (which exists by the maximal principle) also has no cluster point.
