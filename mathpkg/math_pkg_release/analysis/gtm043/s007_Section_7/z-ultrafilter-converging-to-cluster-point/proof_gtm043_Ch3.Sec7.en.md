---
role: proof
locale: en
of_concept: z-ultrafilter-converging-to-cluster-point
source_book: gtm043
source_chapter: "3"
source_section: "7"
---

Let $\mathcal{E}$ denote the $z$-filter of all zero-set-neighborhoods of $p$. Since $p$ is a cluster point of $\mathcal{F}$, every neighborhood of $p$ meets every member of $\mathcal{F}$. In particular, for any zero-set-neighborhood $Z$ of $p$ and any member $F$ of $\mathcal{F}$, we have $Z \cap F \neq \emptyset$, so $Z \cap F$ is a nonempty zero-set. Consider the collection $\mathcal{G} = \mathcal{F} \cup \mathcal{E}$. This collection has the finite intersection property: any finite intersection of members of $\mathcal{G}$ contains a member of $\mathcal{F}$ intersected with a finite intersection of zero-set-neighborhoods of $p$, which is nonempty because $p$ is a cluster point. Extend $\mathcal{G}$ to a $z$-ultrafilter $\mathcal{U}$ (by the maximal principle). Then $\mathcal{U}$ contains both $\mathcal{F}$ and $\mathcal{E}$. Since $\mathcal{U}$ contains all zero-set-neighborhoods of $p$, by 3.16(a), $\mathcal{U}$ converges to $p$. Thus at least one $z$-ultrafilter containing $\mathcal{F}$ converges to $p$.
