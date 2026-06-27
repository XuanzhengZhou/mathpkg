---
role: proof
locale: en
of_concept: incidence-matrix-properties
source_book: gtm006
source_chapter: "3"
source_section: "5"
---

Let $A$ be the incidence matrix of a projective plane of order $n$. Then $b_{ii}$ is the scalar product of the $i$-th row of $A$ with itself. Since $a_{ik} = 1$ if and only if $P_i$ is on $l_k$, and each point lies on exactly $n+1$ lines, we have $b_{ii} = n + 1$.

For $i \neq j$, $b_{ij}$ is the scalar product of the $i$-th row of $A$ with the $j$-th row of $A$, which equals the number of $k$ such that $a_{ik} = a_{jk} = 1$. This counts the number of lines incident with both $P_i$ and $P_j$. Since any two distinct points determine a unique line, $b_{ij} = 1$ for $i \neq j$.

Thus $AA' = nI + J$ where $I$ is the identity matrix and $J$ is the all-ones matrix of size $v = n^2 + n + 1$.
