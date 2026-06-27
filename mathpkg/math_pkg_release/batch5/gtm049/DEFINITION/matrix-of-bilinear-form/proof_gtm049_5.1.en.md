---
role: proof
locale: en
of_concept: matrix-of-bilinear-form
source_book: gtm049
source_chapter: "V"
source_section: "5.1"
---

**Proof.** Suppose that an ordered basis $(a_1, \ldots, a_n)$ of $V$ is given and that the vectors $a, b$ have coordinate rows $x = (x_1, \ldots, x_n)$, $y = (y_1, \ldots, y_n)$, respectively, with respect to this ordered basis. Then, by the bilinearity of $\sigma$,

$$\sigma(a, b) = \sum_{i,j} s_{ij} x_i y_j,$$

where $s_{ij} = \sigma(a_i, a_j)$. If $S$ is the $n \times n$ matrix $(s_{ij})$, we may rewrite this equation in matrix form as

$$\sigma(a, b) = x S y^t.$$

We call $S$ the matrix of $\sigma$ with respect to $(a_1, \ldots, a_n)$ and shall use the notation $(\sigma; (a_i)) = S$. The polynomial $\sum s_{ij} X_i Y_j$ is called the bilinear polynomial of $\sigma$ with respect to $(a_1, \ldots, a_n)$.

To prove (1), the mapping $\sigma \rightarrow (\sigma; (a_i))$ is clearly linear: if $\sigma, \tau \in \mathcal{B}(V)$ and $x \in F$, then $(\sigma + \tau)(a_i, a_j) = \sigma(a_i, a_j) + \tau(a_i, a_j)$ and $(x\sigma)(a_i, a_j) = x\sigma(a_i, a_j)$, so the matrix assignment is linear. The mapping is injective because if $(\sigma; (a_i)) = 0$, then $\sigma(a_i, a_j) = 0$ for all $i, j$, and by bilinearity $\sigma(a, b) = 0$ for all $a, b \in V$, so $\sigma = 0$. It is surjective because given any matrix $S = (s_{ij}) \in F^{n \times n}$, we can define $\sigma$ by $\sigma(a, b) = x S y^t$, which is bilinear and satisfies $\sigma(a_i, a_j) = s_{ij}$. The same argument works for (2), using the vector space of bilinear polynomials instead.
