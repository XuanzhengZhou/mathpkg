---
role: proof
locale: en
of_concept: bound-space-quotient-of-direct-sum
source_book: gtm036
source_chapter: "19"
source_section: "19.7"
---

If $U$ is a neighborhood of $0$ in $E$, then for each member $A$ of $\mathcal{A}$ there is a non-zero scalar $a$ such that $aA \subset U$, because $\mathcal{A}$ consists of bounded sets. Hence $T^{-1}[U]$ contains a non-zero scalar multiple of $A$ in $E_A$ for every $A$ in $\mathcal{A}$, and therefore $T^{-1}[U]$ is a neighborhood of $0$ relative to the direct sum topology. Hence $\mathcal{T}$ is weaker than the quotient topology.

On the other hand, if $V$ is a neighborhood of $0$ relative to the quotient topology, then $T^{-1}[V] \cap E_A$ is a neighborhood of $0$ in the subspace $E_A$ of the direct sum; hence $T^{-1}[V]$ contains a non-zero scalar multiple of $A$, and it follows that $V$ contains a non-zero scalar multiple of $A$. Thus $V$ absorbs bounded sets, for $\mathcal{A}$ was supposed to be a dual base for the family of bounded sets, and consequently $V$ is a $\mathcal{T}$-neighborhood of $0$. The quotient topology is therefore weaker than $\mathcal{T}$, and the two topologies coincide.
