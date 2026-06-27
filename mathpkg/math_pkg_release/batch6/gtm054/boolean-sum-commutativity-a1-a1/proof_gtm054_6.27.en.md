---
role: proof
locale: en
of_concept: boolean-sum-commutativity-a1-a1
source_book: gtm054
source_chapter: "6"
source_section: "VIB"
---

If the theorem is true for graphs, then it is obviously true for multi-graphs. Moreover, if it is true for directed graphs, then it is true for graphs, since any graph $(V, \mathcal{E})$ can be replaced by the directed graph $(V, D)$ where $D = \{(x, y) : \{x, y\} \in \mathcal{E}\}$. Thus $(x, y) \in D \Leftrightarrow (y, x) \in D$, and every path in $(V, \mathcal{E})$ corresponds to a directed path in $(V, D)$. The theorem will now be proved for the case $\Gamma = (V, D)$. We assume the hypothesis of the theorem.

Let $x_0$ be some object not in $V$

Every openly-disjoint $m$-family of az-paths in $\Gamma$ yields a feasible flow in $\Gamma'$ whose value at $x_0$ is $m$. Conversely, let $h$ be an integral feasible flow in $\Gamma'$ with $h(x_0) = m$. By IVA17, $h$ is the sum of elementary flows. The supports of these elementary flows correspond to directed circuits in $\Gamma'$ and no two of them have any common vertex except possibly $x_0$. In fact, exactly $m$ of them pass through $x_0$. Hence they correspond to an openly-disjoint $m$-family of az-paths in $\Gamma$. Thus,
