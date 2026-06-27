---
role: proof
locale: en
of_concept: scalar-product-respecting-gradations-implies-duality
source_book: gtm023
source_chapter: "VI"
source_section: "§1. G-graded vector spaces"
---

By the previous proposition, since $\varphi$ is a scalar product (non-degenerate bilinear form) that respects the $G$-gradations, each restriction $\varphi_k = \varphi|_{E_k \times F_k}$ is non-degenerate. Thus $\varphi_k: E_k \times F_k \rightarrow \Gamma$ is a non-degenerate bilinear form, making $E_k$ and $F_k$ dual vector spaces.

For finite-dimensional dual spaces, $\dim E_k = \dim F_k$ holds for each $k \in G$. In the case $G = \mathbb{Z}$ with positive gradations, the Poincaré series are
$$P_E(t) = \sum_{k=0}^{\infty} \dim E_k \, t^k, \quad P_F(t) = \sum_{k=0}^{\infty} \dim F_k \, t^k.$$
Since $\dim E_k = \dim F_k$ for all $k$, the coefficients coincide and hence $P_E = P_F$.
