---
role: proof
locale: en
of_concept: primitive-group-normal-subgroup-incomplete
source_book: gtm006
source_chapter: "XIV"
source_section: "1"
---

**Proof.** (Result 14.3) Let $\Lambda$ be a primitive permutation group on a set $\mathcal{S}$ of $n$ points and let $\Pi$ contain a normal subgroup $\Sigma \neq 1$. If $\Sigma$ is incomplete, i.e., does not act transitively on $\mathcal{S}$, then the orbits of $\Sigma$ form a system of imprimitivity for $\Lambda$.

Since $\Sigma \trianglelefteq \Lambda$, for any $\lambda \in \Lambda$ and any orbit $\mathcal{O}$ of $\Sigma$, the image $\mathcal{O}^\lambda$ is also an orbit of $\Sigma$: for $x \in \mathcal{O}$ and $\sigma \in \Sigma$, $(x^\lambda)^\sigma = x^{\lambda\sigma} = x^{\sigma'\lambda}$ for some $\sigma' \in \Sigma$ (since $\Sigma \trianglelefteq \Lambda$), so $(x^\lambda)^\sigma \in \mathcal{O}^\lambda$.

Thus $\Lambda$ permutes the orbits of $\Sigma$, which form a partition of $\mathcal{S}$ into blocks of equal size. If $\Sigma$ is not transitive, these blocks are proper subsets of $\mathcal{S}$, constituting a system of imprimitivity. But $\Lambda$ is primitive, so by definition no such non-trivial system of imprimitivity exists unless the blocks are singletons (in which case $\Sigma = 1$) or there is only one block (in which case $\Sigma$ is transitive). Thus if $\Sigma \neq 1$ and $\Sigma$ is not transitive, we obtain a contradiction to primitivity. Hence any non-trivial normal subgroup of a primitive permutation group must be transitive.
