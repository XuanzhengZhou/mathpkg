---
role: proof
locale: en
of_concept: identity-of-matrix-ring
source_book: gtm030
source_chapter: "7"
source_section: "2"
---

The element
$$I_n = \begin{bmatrix} 1 & 0 & \cdots & 0 \\ 0 & 1 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & 1 \end{bmatrix}$$
has $1$ on the diagonal and $0$ elsewhere. For any matrix $A = (a_{ij}) \in \Re_n$, the $(i,j)$-entry of $I_n A$ is
$$\sum_{k} \delta_{ik} a_{kj} = a_{ij}$$
since $\delta_{ik} = 1$ when $k = i$ and $0$ otherwise. Similarly, the $(i,j)$-entry of $A I_n$ is
$$\sum_{k} a_{ik} \delta_{kj} = a_{ij}.$$
Thus $I_n A = A I_n = A$, so $I_n$ is the multiplicative identity in $\Re_n$.
