---
role: proof
locale: en
of_concept: hausdorff-theorem-on-total-boundedness
source_book: gtm036
source_chapter: "7"
source_section: "7.6"
---

It is easy to see that a compact set is totally bounded and complete. Conversely, if $A$ is a totally bounded complete subset of a linear topological space, the proof that $A$ is compact proceeds as follows. Let $\mathcal{A}$ be a family of closed subsets of $A$, and suppose that $\mathcal{A}$ has the finite intersection property. Then $\mathcal{A}$ is contained in a maximal family of this sort; for convenience, let $\mathcal{A}$ itself be such a maximal family. It must now be shown that the intersection of all the members of $\mathcal{A}$ is non-void. Since $A$ is complete, the desired result will follow if it is proved that $\mathcal{A}$ contains small sets. Since $A$ can be covered by a finite number of translates of an arbitrarily small open set, it is sufficient to show that if $B_i, i = 1, \cdots, n$, is a finite covering of $A$ by closed subsets of $A$, then for some $i$, $B_i \in \mathcal{A}$. Since $\mathcal{A}$ is maximal, a closed subset $B_i$ of $A$ can fail to belong to $\mathcal{A}$ only because its adjunction to $\mathcal{A}$ destroys the finite intersection property; that is, there is a finite subfamily $\mathcal{B}_i$ of $\mathcal{A}$ whose intersection with $B_i$ is void. If this is the case for each $i$, then there is a finite subfamily (namely $\bigcup \{\mathcal{B}_i : i = 1, \cdots, n\}$) of $\mathcal{A}$ whose intersection is disjoint from every $B_i$ and is therefore void. This contradiction establishes the desired result.
