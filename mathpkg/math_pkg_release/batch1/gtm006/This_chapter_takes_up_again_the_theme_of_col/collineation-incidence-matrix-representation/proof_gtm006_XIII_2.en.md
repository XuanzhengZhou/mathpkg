---
role: proof
locale: en
of_concept: collineation-incidence-matrix-representation
source_book: gtm006
source_chapter: "XIII"
source_section: "2"
---

Let $A = (a_{ij})$ be an incidence matrix of the finite projective plane $\mathcal{P}$, where $a_{ij} = 1$ if point $P_i$ lies on line $l_j$ and $a_{ij} = 0$ otherwise. Let $\alpha$ be a collineation of $\mathcal{P}$, and let $P = (p_{ij})$ and $Q = (q_{jk})$ be permutation matrices representing the action of $\alpha$ on points and lines respectively, defined by:
$$
p_{ij} = \begin{cases} 1 & \text{if } P_i^{\alpha} = P_j \\ 0 & \text{otherwise} \end{cases}, \qquad
q_{jk} = \begin{cases} 1 & \text{if } l_j^{\alpha^{-1}} = l_k \\ 0 & \text{otherwise} \end{cases}.
$$

We must show that $PA = AQ$. Consider the $(i,k)$-entry of $PA$:
$$
(PA)_{ik} = \sum_{j} p_{ij} a_{jk} = a_{xk}
$$
where $x$ is uniquely determined by $p_{ix} = 1$, i.e., $P_i^{\alpha} = P_x$. Similarly, the $(i,k)$-entry of $AQ$ is:
$$
(AQ)_{ik} = \sum_{j} a_{ij} q_{jk} = a_{iy}
$$
where $y$ is uniquely determined by $q_{yk} = 1$, i.e., $l_y = l_k^{\alpha}$.

We must show $a_{xk} = a_{iy}$. By definition:
$$
a_{xk} = 1 \Leftrightarrow P_x \in l_k \Leftrightarrow P_i^{\alpha} \in l_k \Leftrightarrow P_i \in l_k^{\alpha^{-1}} \Leftrightarrow P_i \in l_y \Leftrightarrow a_{iy} = 1.
$$
Thus $a_{xk} = a_{iy}$ for all $i,k$, so $PA = AQ$.
