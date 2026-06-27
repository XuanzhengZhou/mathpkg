---
role: proof
locale: en
of_concept: lemma-12-39
source_book: gtm040
source_chapter: "12"
source_section: "5"
---

Since $Q' > 0$ is a strictly positive matrix on the finite set $S$, by the Perron-Frobenius theorem there exists a positive eigenvalue $\bar{c} > 0$ equal to the spectral radius of $Q'$, and an associated strictly positive eigenvector $\bar{h} > 0$ satisfying $Q' \bar{h} = \bar{c} \bar{h}$. Define $Q$ by
$$
Q_{ij} = \frac{Q'_{ij} \bar{h}_j}{\bar{c} \bar{h}_i}.
$$
Then $Q_{ij} > 0$ for all $i,j$, and for each $i$,
$$
\sum_{j \in S} Q_{ij} = \sum_{j \in S} \frac{Q'_{ij} \bar{h}_j}{\bar{c} \bar{h}_i} = \frac{(Q' \bar{h})_i}{\bar{c} \bar{h}_i} = \frac{\bar{c} \bar{h}_i}{\bar{c} \bar{h}_i} = 1,
$$
so $Q$ is a stochastic matrix. Moreover, $Q'$ and $Q$ are equivalent in the sense that $Q'_{ij} = \bar{c} (\bar{h}_i / \bar{h}_j) Q_{ij}$, which is precisely the equivalence relation characterizing homogeneous neighbor potentials that determine the same Gibbs field. The normalization $\bar{c} = 1$ can be arranged by choosing the appropriate representative from the equivalence class; this yields the canonical stochastic matrix $Q$ associated with $Q'$.
