---
role: proof
locale: en
of_concept: endomorphism-ring-free-abelian-matrix
source_book: gtm030
source_chapter: "1"
source_section: "1.11"
---
Let $\eta, \rho \in \mathfrak{E}$ with matrices $(a_{ij})$ and $(b_{ij})$ respectively, so that $e_i\eta = \sum_j a_{ij} e_j$ and $e_i\rho = \sum_j b_{ij} e_j$.

**Injectivity:** If $\eta$ and $\rho$ have the same matrix, then $e_i\eta = e_i\rho$ for all basis elements $e_i$. Since every element of $\mathfrak{G}$ is a unique integer linear combination of the $e_i$, it follows that $\eta = \rho$ on all of $\mathfrak{G}$. Thus the correspondence is one-to-one.

**Addition:** For the pointwise sum $\eta + \rho$, we compute
$$e_i(\eta + \rho) = e_i\eta + e_i\rho = \sum_j a_{ij} e_j + \sum_j b_{ij} e_j = \sum_j (a_{ij} + b_{ij}) e_j.$$
Thus $\eta + \rho$ corresponds to the matrix $(a_{ij}) + (b_{ij})$, the entrywise sum.

**Multiplication (composition):** For the resultant $\eta\rho$,
\begin{align*}
e_i(\eta\rho) &= (e_i\eta)\rho = \left(\sum_j a_{ij} e_j\right)\rho = \sum_j a_{ij} (e_j\rho) \\
&= \sum_j a_{ij} \left(\sum_k b_{jk} e_k\right) = \sum_k \left(\sum_j a_{ij} b_{jk}\right) e_k = \sum_k c_{ik} e_k,
\end{align*}
where $c_{ik} = \sum_j a_{ij} b_{jk}$. This is precisely the $(i,k)$-entry of the matrix product $(a_{ij})(b_{jk})$. Thus $\eta\rho$ corresponds to the matrix product.

**Surjectivity:** Given any integer matrix $(a_{ij})$, define $\eta$ on basis elements by $e_i\eta = \sum_j a_{ij} e_j$ and extend linearly to all of $\mathfrak{G}$. This defines an endomorphism whose matrix is $(a_{ij})$. Therefore the correspondence is onto $I_n$.

Hence $\mathfrak{E} \cong I_n$, the ring of $n \times n$ integer matrices.
