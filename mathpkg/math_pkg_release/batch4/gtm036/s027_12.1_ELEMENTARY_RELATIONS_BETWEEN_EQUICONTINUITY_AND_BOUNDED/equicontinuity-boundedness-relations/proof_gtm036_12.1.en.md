---
role: proof
locale: en
of_concept: equicontinuity-boundedness-relations
source_book: gtm036
source_chapter: "12"
source_section: "12.1"
---

For the equivalences within (ii): By definition, $F$ is bounded in the topology of uniform convergence on bounded sets precisely when $F$ is uniformly bounded on each bounded set.

For the equivalences within (iii): $F$ is uniformly bounded on $A$ means by definition that $F[A]$ is bounded. The equivalence with boundedness in the topology of uniform convergence on $A$ follows from the definition of that topology: the sets $\{f : f[A] \subset V\}$ for neighborhoods $V$ of $0$ in $H$ form a base of neighborhoods of $0$. The condition that $\bigcap\{f^{-1}[V] : f \in F\}$ absorbs $A$ is equivalent to: for each neighborhood $V$ of $0$ in $H$, there exists a scalar $t$ such that $A \subset t \bigcap\{f^{-1}[V] : f \in F\}$, which means $F[A] \subset t^{-1}V$, i.e., $F[A]$ is bounded.

For the equivalence in (iv): $F$ is pointwise bounded on $A$ means $\{f(x) : f \in F\}$ is bounded for each $x \in A$, which is equivalent to: for each $x \in A$ and each neighborhood $V$ of $0$ in $H$, $\bigcap\{f^{-1}[V] : f \in F\}$ absorbs $\{x\}$ (each point of $A$).

The implication (i) $\Rightarrow$ (ii): If $F$ is equicontinuous, then for each neighborhood $V$ of $0$ in $H$, $\bigcap\{f^{-1}[V] : f \in F\}$ is a neighborhood of $0$ in $E$. This neighborhood absorbs every bounded set $B \subset E$, hence $F$ is uniformly bounded on each bounded set.

The implication (iii) $\Rightarrow$ (iv) is immediate: if $\bigcap\{f^{-1}[V] : f \in F\}$ absorbs $A$, then it certainly absorbs each singleton $\{x\}$ for $x \in A$. The implication that uniform boundedness on $A$ implies pointwise boundedness on $A$ also follows because $F[A]$ bounded implies each $F[x] \subset F[A]$ is bounded.
