---
role: proof
locale: en
of_concept: solvability-of-linear-equations
source_book: gtm031
source_chapter: "II"
source_section: "7"
---

Consider the left-handed system
$$
\sum_{i=1}^n \xi_i \alpha_{ij} = \delta_j, \quad j = 1, 2, \dots, m
$$
with $\alpha_{ij}, \delta_j \in \Delta$, a division ring. Let $\mathfrak{S}$ be an $m$-dimensional left vector space with basis $(f_1, f_2, \dots, f_m)$. Define vectors
$$
u_i = \sum_{j=1}^m \alpha_{ij} f_j, \quad i = 1, 2, \dots, n,
$$
and $v = \sum_{j=1}^m \delta_j f_j$. Then $(\beta_1, \beta_2, \dots, \beta_n)$ is a solution of the system if and only if
$$
v = \beta_1 u_1 + \beta_2 u_2 + \dots + \beta_n u_n.
$$
Hence the system is solvable if and only if $v$ is linearly dependent on $u_1, u_2, \dots, u_n$. This holds if and only if
$$
\operatorname{rank}(u_1, u_2, \dots, u_n) = \operatorname{rank}(u_1, u_2, \dots, u_n, v),
$$
which is equivalent to the row rank of $(\alpha)$ being equal to the row rank of the augmented matrix. In the commutative case $\Delta = \Phi$, row rank coincides with determinantal rank, yielding the criterion stated in the theorem.
