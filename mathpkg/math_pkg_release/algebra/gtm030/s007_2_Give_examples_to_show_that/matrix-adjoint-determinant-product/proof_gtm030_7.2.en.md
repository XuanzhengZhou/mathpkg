---
role: proof
locale: en
of_concept: matrix-adjoint-determinant-product
source_book: gtm030
source_chapter: "7"
source_section: "2"
---

Let $\operatorname{adj}(a)$ have $(i,j)$-entry $\alpha_{ij} = A_{ji}$, the cofactor of $a_{ji}$. The $(i,j)$-entry of the product $(a)\operatorname{adj}(a)$ is
$$\sum_{k} a_{ik} \alpha_{kj} = \sum_{k} a_{ik} A_{jk}.$$

If $i = j$, this sum is $\det(a)$ by the cofactor expansion formula (7). If $i \neq j$, the sum is $0$ by the alien cofactor formula (8). Thus
$$(a)\operatorname{adj}(a) = \det(a) I_n.$$

The same reasoning for the product $\operatorname{adj}(a)(a)$ using column expansions yields
$$\operatorname{adj}(a)(a) = \det(a) I_n.$$
