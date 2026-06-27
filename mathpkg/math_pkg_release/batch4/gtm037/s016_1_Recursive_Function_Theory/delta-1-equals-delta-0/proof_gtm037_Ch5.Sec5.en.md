---
role: proof
locale: en
of_concept: delta-1-equals-delta-0
source_book: gtm037
source_chapter: "Part 1: Recursive Function Theory"
source_section: "5. Arithmetic Hierarchy"
---

We know that $\Delta_0 \subseteq \Delta_1$ (every recursive relation is both $\Sigma_1$ and $\Pi_1$). For the reverse inclusion, suppose $R \in \Delta_1$, say $R$ is $n$-ary. Then there are recursive $(n+1)$-ary relations $S$ and $T$ such that for all $x_0, \ldots, x_{n-1} \in \omega$,

$$(x_0, \ldots, x_{n-1}) \in R \quad \text{iff} \quad \exists y \in \omega[(x_0, \ldots, x_{n-1}, y) \in S],$$
$$(x_0, \ldots, x_{n-1}) \in R \quad \text{iff} \quad \forall y \in \omega[(x_0, \ldots, x_{n-1}, y) \in T].$$

Since $S$ is recursive, the relation defined by $\exists y \in \omega[(x_0, \ldots, x_{n-1}, y) \in S]$ is recursively enumerable (i.e., $\Sigma_1$). Since $T$ is recursive, the relation defined by $\forall y \in \omega[(x_0, \ldots, x_{n-1}, y) \in T]$ is co-recursively enumerable (i.e., $\Pi_1$). Being both recursively enumerable and co-recursively enumerable, $R$ is recursive, so $R \in \Delta_0$. Hence $\Delta_1 \subseteq \Delta_0$, and therefore $\Delta_1 = \Delta_0$.
