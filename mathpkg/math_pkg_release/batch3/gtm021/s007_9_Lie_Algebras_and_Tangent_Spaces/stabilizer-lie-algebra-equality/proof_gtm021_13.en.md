---
role: proof
locale: en
of_concept: stabilizer-lie-algebra-equality
source_book: gtm021
source_chapter: "13"
source_section: "Correspondence Between Groups and Lie Algebras"
---
Take a basis $v_1, \ldots, v_n$ of $V$ such that $v_1, \ldots, v_m$ span $W$ (resp. such that $v_1 = v$).

For $G_W$: The condition $x(W) = W$ means the matrix of $x$ in this basis has block upper triangular form:
$$\begin{pmatrix} A & B \\ 0 & D \end{pmatrix}$$
where $A \in \operatorname{GL}(m)$, $D \in \operatorname{GL}(n-m)$, and $B$ is an arbitrary $m \times (n-m)$ matrix. This is an affine open subset of the linear variety defined by the vanishing of the lower-left block, which has dimension $m^2 + (n-m)^2 + m(n-m) = n(n-m) + m^2$. The Lie algebra $\mathfrak{g}_W$ consists of all matrices with arbitrary upper-left, upper-right, and lower-right blocks, but zero lower-left block -- this has exactly the same dimension $n(n-m) + m^2$. Since $\mathcal{L}(G_W) \subset \mathfrak{g}_W$ always holds (by differentiating the defining condition), equality of dimensions forces $\mathcal{L}(G_W) = \mathfrak{g}_W$.

For $G_v$: After translating by the identity matrix, $G_v$ consists of matrices of the form $I + N$ where $N$ has first column zero. This is an affine open subset of a linear variety of dimension $n^2 - n$, and $\mathfrak{g}_v$ is the space of matrices with first column zero, also of dimension $n^2 - n$. The same dimension argument gives equality.
