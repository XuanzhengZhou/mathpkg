---
role: proof
locale: en
of_concept: h-process-kernel-formula
source_book: gtm040
source_chapter: "10"
source_section: "5"
---

If $h_i = 0$ and $h_j > 0$, then $h_i \geq \sum_k P_{ik}^{(n)} h_k \geq P_{ij}^{(n)} h_j$, so $P_{ij}^{(n)} = 0$ and $N_{ij} = 0$. Consequently,
$$(\pi^h N^h)_j = \sum_{i \in S^h} \pi_i h_i (N_{ij} h_j / h_i) = h_j \sum_{i \in S} \pi_i N_{ij} = h_j (\pi N)_j.$$
For the kernel,
$$K^h(i, j) = N_{ij}^h / (\pi^h N^h)_j = \frac{N_{ij} h_j / h_i}{h_j (\pi N)_j} = K(i, j) / h_i.$$
