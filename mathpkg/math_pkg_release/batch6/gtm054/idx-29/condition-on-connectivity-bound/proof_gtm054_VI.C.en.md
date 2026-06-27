---
role: proof
locale: en
of_concept: condition-on-connectivity-bound
source_book: gtm054
source_chapter: "VI"
source_section: "C"
---

Suppose $\kappa(\Gamma) \leq 2n - 2$. Then there exists a set $S \subseteq V$ with $|S| \leq 2n-2$ that separates $\Gamma$. Since $\Gamma$ satisfies $O_n$, we have $|V| \geq 2n$. Choose vertices $a_1, \ldots, a_n, z_1, \ldots, z_n$ in different components after removing $S$ such that the condition $O_n$ forces openly-disjoint paths between the pairs $(a_i, z_i)$. But with at most $2n-2$ vertices in $S$, the pigeonhole principle forces at least two paths to intersect in $S$, contradicting the openly-disjoint property. Therefore $\kappa(\Gamma) \geq 2n - 1$.
