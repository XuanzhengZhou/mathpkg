---
role: exercise
locale: en
chapter: "6"
section: "25"
exercise_number: 8
---

Let $G$ be a finite group, let $H$ be an arbitrary subgroup, and let $m$ be the index of $H$ in $G$. Prove that there exist $x_1, \ldots, x_m \in G$ such that

$$G =

VE {0, 1}-Matrices

In this section $M = [m_{ij}]$ will denote an $r \times s$ matrix where $m_{ij} = 0$ or 1 for all $(i, j) \in \{1, \ldots, r\} \times \{1, \ldots, s\}$. Such a matrix is called a {0, 1}-matrix. By a line of $M$ is meant either a row or a column of $M$.

We shall now define a rather broad "incidence relation" among lines and positions in a {0, 1}-matrix. The reader should perceive that this definition is motivated by the definitions of incidence in multigraphs (§A) and of incidence matrix of a system (§ID).

We say that the $i$th row and $j$th column of $M$ are incident if $m_{ij} = 1$. The $i$th and $j$th rows are incident if their inner product satisfies

$$\sum_{k=1}^{s} m_{ik} m_{jk} > 0.$$

(Thus $m_{ik} = 1 = m_{jk}$ for some $k \in \{1, \ldots, s\}$.) Similarly two columns are incident if their inner product is positive. We say that the position $(i, j)$ is incident with the $i$th row and with the $j$th column. Finally, two positions on a common line are incident.

The number of lines of an $r \times s$ matrix $M$ is denoted by $\pi(M) = r + s$.

If $M$ is an incidence matrix of a system $\Lambda = (V, f, E)$, then the matrix $MM^* = A = [a_{ij}]$ is called a vertex-vertex incidence matrix (or an adjacency matrix) of $\Lambda$. The set $V = \{x_1, \ldots, x_r\}$ may be indexed so that for $i, j \in \{1, \ldots, r\}$,

$$a_{ij} = |\{e \in E: \{x_i, x_j\} \subseteq f(e)\}| = |f^*(x_i) \cap f^*(

V Matchings and Related Structures

Moreover,

$$\rho(x_i) = \sum_{j \neq i} a_{ij} = \sum_{j \neq i} a_{ji}.$$

In the block-block incidence matrix of $\Gamma$, the diagonal entries are all 2 and the others are each 0 or 1. Graphs are not the only systems with the property that the nondiagonal entries in these two matrices are 0 or 1, as we see in the following exercise.
