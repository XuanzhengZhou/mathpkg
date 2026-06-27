---
role: proof
locale: en
of_concept: elementary-basis-transformations-matrix-effect
source_book: gtm023
source_chapter: "3"
source_section: "4. Elementary transformations"
---

The matrix $M(\varphi) = (\alpha_\nu^\mu)$ of a linear mapping $\varphi: E \to F$ with respect to bases $x_\nu\ (\nu = 1, \dots, n)$ of $E$ and $y_\mu\ (\mu = 1, \dots, m)$ of $F$ is defined by

$$\varphi(x_\nu) = \sum_{\mu=1}^{m} \alpha_\nu^\mu y_\mu.$$

Thus the $\nu$-th column of $M(\varphi)$ consists of the coordinates of $\varphi(x_\nu)$.

(I.1.) Interchanging $x_i$ and $x_j$ simply swaps the $i$-th and $j$-th columns of $M(\varphi)$, since the coordinates of $\varphi(x_i)$ and $\varphi(x_j)$ are exchanged. In terms of the codomain basis, this has the effect of interchanging rows $i$ and $j$ in the matrix representation when viewed from the dual perspective of coordinates.

(I.2.) Interchanging $y_k$ and $y_l$ exchanges the $k$-th and $l$-th coordinate positions, which corresponds to interchanging columns $k$ and $l$ in $M(\varphi)$.

(II.1.) Replacing $x_i$ by $x_i + \lambda x_j$ gives

$$\varphi(x_i + \lambda x_j) = \varphi(x_i) + \lambda \varphi(x_j).$$

In coordinates, the $i$-th column (row-vector $a_i$) is replaced by $a_i + \lambda a_j$.

(II.2.) Replacing $y_k$ by $y_k + \lambda y_l$ changes the expression of vectors in terms of the new basis. The $k$-th coordinate of every image vector is adjusted, leading to the replacement of column-vector $b_k$ by $b_k + \lambda b_l$.
