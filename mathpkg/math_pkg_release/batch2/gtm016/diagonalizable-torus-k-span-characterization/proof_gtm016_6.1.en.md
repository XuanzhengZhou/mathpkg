---
role: proof
locale: en
of_concept: diagonalizable-torus-k-span-characterization
source_book: gtm016
source_chapter: "6"
source_section: "1"
---

One direction is clear from 6.1.12. For the other, suppose that $T$ is diagonalizable on $V$, so that $V = \sum_{\alpha \in R} V_\alpha(T)$ (direct) where $R = \{\alpha \in T^* \mid V_\alpha(T) \neq \{0\}\}$. Since $R$ separates the points of $T$, $R$ contains a basis $\alpha_1, \ldots, \alpha_n$ for $T^*$. Let $t_1, \ldots, t_n$ be a dual basis for $T$. Then $\alpha_j(t_i) = \delta_{ij}$ and $\alpha_j(t_i^p) = \alpha_j(t_i)^p = \delta_{ij}$ for all $i, j$. Thus, $\alpha_j(t_i^p) = \alpha_j(t_i)$ for all $i, j$. Since the $\alpha_j$ separate the points of $T$, it follows that $t_i^p = t_i$ for all $i$, so that $T$ is the $k$-span of $T_\pi$.
