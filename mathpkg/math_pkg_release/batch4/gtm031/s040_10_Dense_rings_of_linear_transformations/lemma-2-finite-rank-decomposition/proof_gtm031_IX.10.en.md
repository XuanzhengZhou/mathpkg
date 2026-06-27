---
role: proof
locale: en
of_concept: lemma-2-finite-rank-decomposition
source_book: gtm031
source_chapter: "IX"
source_section: "10"
---
Let $F$ be a transformation of finite rank with $\mathfrak{R}F = [u_1, u_2, \cdots, u_m]$ where the $u_i$ are linearly independent. Write $F = \sum_{i=1}^m \phi_i \times u_i$ for suitable $\phi_i \in \mathfrak{R}^*$. Let $F_j = \sum_k \psi_{jk} \times v_{jk}$ be transformations in $\mathfrak{A}$ as in the hypothesis, where the $v_{jk}$ are linearly independent for each fixed $j$.

Since the $\phi_i$ and $\psi_{jk}$ are linear functions on $\mathfrak{R}$, we can write $\phi_i = \sum_{j,k} \psi_{jk} \mu_{jk,i}$ for suitable $\mu_{jk,i} \in \Delta$. Since $\mathfrak{A}$ is dense and the $v_{jk}$ for fixed $j$ are linearly independent, we can find $A_{ji} \in \mathfrak{A}$ such that
$$v_{jk} A_{ji} = \mu_{jk,i} u_i$$
for $k = 1, 2, \cdots$ and $i = 1, 2, \cdots, m$.

Now consider the transformation $\sum_{j,i} F_j A_{ji}$, which belongs to $\mathfrak{J} \cap \mathfrak{A}$ since $\mathfrak{J} \cap \mathfrak{A}$ is an ideal in $\mathfrak{A}$. We compute:
$$\sum_{j,i} F_j A_{ji} = \sum_{j,i} \left( \sum_k \psi_{jk} \times v_{jk} \right) A_{ji} = \sum_{i,j,k} \psi_{jk} \times v_{jk} A_{ji}$$
$$= \sum_{i,j,k} \psi_{jk} \times \mu_{jk,i} u_i = \sum_i \left( \sum_{j,k} \psi_{jk} \mu_{jk,i} \right) \times u_i$$
$$= \sum_i \phi_i \times u_i = F.$$

Thus $F \in \mathfrak{J} \cap \mathfrak{A}$, as required.
