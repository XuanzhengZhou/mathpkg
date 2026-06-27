---
role: proof
locale: en
of_concept: every-subset-mathcal-c1
source_book: gtm054
source_chapter: "2"
source_section: "IIC"
---

Let $S \in \mathcal{A}$. We proceed by induction on $|S|$. If $S = \varnothing$, then $S$ is the sum over the empty collection. Let $n$ be a positive integer, and assume the conclusion holds for $T$ whenever $T \in \mathcal{A}$ and $|T| < n$. Now assume $|S| = n$. By Proposition B11, there exists an elementary set $M \subseteq S$. Thus $|S + M| = |S| - |M| < n$, and by the induction hypothesis, there exist pairwise-disjoint subsets $M_1, \ldots, M_k \in M(\mathcal{A})$ such that $S + M = M_1 + \ldots + M_k$. Hence $S = M_1 + \ldots + M_k + M$ is the required sum.

The incommensurability of $M(\mathcal{A})$ plays an important role in proving the next result.
