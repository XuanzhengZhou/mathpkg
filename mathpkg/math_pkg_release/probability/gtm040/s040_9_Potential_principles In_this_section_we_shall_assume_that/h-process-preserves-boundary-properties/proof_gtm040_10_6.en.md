---
role: proof
locale: en
of_concept: h-process-preserves-boundary-properties
source_book: gtm040
source_chapter: "10"
source_section: "6"
---

For (1), $\sum_{i \in S^h} \pi_i^h K^h(i, x) = \sum_i \pi_i h_i K(i, x) / h_i = \pi K(\cdot, x)$.

For (2), $\sum_{j \in S^h} P_{ij}^h K^h(j, x) = \sum_j (P_{ij} h_j / h_i)(K(j, x) / h_j) = (1/h_i) \sum_j P_{ij} K(j, x) = PK(\cdot, x)_i / h_i$.

For (3), if $K^h(i, x) = c_3 h_i^{(3)} + c_4 h_i^{(4)}$ is a convex combination for $i \in S^h$, then $K(i, x) = c_3 h_i^{(3)} h_i + c_4 h_i^{(4)} h_i$, extending by zero outside $S^h$. Both extended functions are regular and normalized, giving a convex decomposition of $K(\cdot, x)$. The converse follows similarly.
