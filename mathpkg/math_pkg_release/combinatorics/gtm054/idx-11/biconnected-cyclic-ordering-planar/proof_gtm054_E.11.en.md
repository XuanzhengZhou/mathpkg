---
role: proof
locale: en
of_concept: biconnected-cyclic-ordering-planar
source_book: gtm054
source_chapter: "E"
source_section: "11"
---

Let $Z_1, \ldots, Z_k$ be a planar imbedding for $\Gamma$, and let $x$ be a vertex of $\Gamma$. By reordering if necessary, we may suppose that $Z_1, \ldots, Z_h$ are the cycles of the imbedding which contain edges incident with $x$.

Since $\Gamma$ is biconnected, the imbedding is elementary by B3 and E9. Hence for $i = 1, \ldots, h$, the cycle $Z_i$ contains exactly two edges belonging to $f^*(x)$ (the set of edges incident with $x$). These two edges determine the adjacency pattern around $x$: each region $Z_i$ that touches $x$ contributes a consecutive pair of incident edges. Traversing the cyclic order of regions around $x$ yields a cyclic ordering $e_0, e_1, \ldots, e_{\rho(x)-1}$ of the edges incident with $x$ with the property that $e_i$ and $e_{i+1}$ belong to a common region $Z_j$.
