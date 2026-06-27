---
role: proof
locale: en
of_concept: linear-independence-of-u-alpha
source_book: gtm036
source_chapter: "0"
source_section: "D"
---

Let $S$ be an infinite set, fix distinct elements $a_1, a_2, \ldots \in S$, and for each scalar $\alpha$ with $\alpha \neq 0$, $|\alpha| \leq 1$, define $u_\alpha$ as above. Suppose a finite linear combination vanishes:
$$
\sum_{i=1}^{m} c_i \, u_{\alpha_i} = 0,
$$
with distinct $\alpha_i$ and non-zero scalars $c_i$. Evaluating at $x = a_n$ for each $n \in \mathbb{N}$ gives
$$
\sum_{i=1}^{m} c_i \, \alpha_i^n = 0 \quad \text{for all } n \in \mathbb{N}.
$$

This is a system of infinitely many linear equations in the $m$ unknowns $c_1, \ldots, c_m$. The first $m$ equations yield a Vandermonde system:
$$
\begin{pmatrix}
1 & 1 & \cdots & 1 \\
\alpha_1 & \alpha_2 & \cdots & \alpha_m \\
\alpha_1^2 & \alpha_2^2 & \cdots & \alpha_m^2 \\
\vdots & \vdots & \ddots & \vdots \\
\alpha_1^{m-1} & \alpha_2^{m-1} & \cdots & \alpha_m^{m-1}
\end{pmatrix}
\begin{pmatrix}
c_1 \\ c_2 \\ c_3 \\ \vdots \\ c_m
\end{pmatrix} = 0.
$$

Since the $\alpha_i$ are distinct, the Vandermonde determinant is non-zero, so the only solution is $c_1 = c_2 = \cdots = c_m = 0$. Therefore the family $\{u_\alpha\}$ is linearly independent. The cardinality of this family equals the cardinality $c$ of the set of scalars $\alpha$ satisfying $0 < |\alpha| \leq 1$, which is the cardinality of the scalar field.
