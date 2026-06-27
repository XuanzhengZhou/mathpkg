---
role: exercise
locale: en
chapter: "10"
section: "Bi-uniform topological groups"
exercise_number: 9
---

# Exercise 10.9

With notation as in (10.8), let $G$ be the group of upper triangular $3 \times 3$ real matrices with $1$'s on the diagonal, equipped with the metric $d$ inherited from $\mathbb{R}^9$. Then $G$ is a metrizable complete group, $d$ is a complete compatible metric on $G$, but $\mathcal{U}_d$ is distinct from both $\mathcal{U}_s$ and $\mathcal{U}_r$.

For example, to see that $\mathcal{U}_d \neq \mathcal{U}_s$, consider the matrices

$$A_n = \begin{pmatrix} 1 & n & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}, \quad B_n = \begin{pmatrix} 1 & n & 0 \\ 0 & 1 & 1/n \\ 0 & 0 & 1 \end{pmatrix}$$

for $n = 1, 2, 3, \ldots$. Then

$$d(A_n, B_n) = 1/n, \quad d(A_n^{-1}B_n, I) = 1,$$

therefore $\mathcal{U}_d \neq \mathcal{U}_s$ by (6.9).
