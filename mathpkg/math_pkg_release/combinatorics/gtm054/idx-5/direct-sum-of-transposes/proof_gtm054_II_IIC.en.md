---
role: proof
locale: en
of_concept: direct-sum-of-transposes
source_book: gtm054
source_chapter: "II"
source_section: "IIC"
---

**Proof of C14 Proposition.**

Let $M_i$ be an incidence matrix for $\Lambda_i$ for $i = 1, \ldots, k$. Then the incidence matrix $M$ of $\bigoplus_{i=1}^{k} \Lambda_i$ is the block diagonal matrix
$$M = \begin{bmatrix}
M_1 & 0 & \cdots & 0 \\
0 & M_2 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & M_k
\end{bmatrix}.$$
Its transpose $M^*$ has the same block diagonal form with $M_i^*$ replacing $M_i$ for $i = 1, \ldots, k$. But the block diagonal matrix with blocks $M_i^*$ is precisely the incidence matrix of $\bigoplus_{i=1}^{k} \Lambda_i^*$. Hence $(\bigoplus_{i=1}^{k} \Lambda_i)^* = \bigoplus_{i=1}^{k} \Lambda_i^*$.
