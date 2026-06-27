---
role: proof
locale: en
of_concept: kernel-of-homogeneous-mapping-is-graded-subspace
source_book: gtm023
source_chapter: "VI"
source_section: "§1. G-graded vector spaces"
---

Let $\varrho_j: E \rightarrow E_j$ and $\sigma_j: F \rightarrow F_j$ denote the projection operators in $E$ and $F$ induced by the gradations of $E$ and $F$. Since $\varphi$ is homogeneous of degree $k$, we have $\varphi E_j \subset F_{j+k}$, which implies the commutation relation
$$\sigma_{k+j} \circ \varphi = \varphi \circ \varrho_j.$$
Now let $x \in \ker \varphi$ and decompose $x = \sum_j x_j$ with $x_j \in E_j$. Then
$$0 = \varphi(x) = \sum_j \varphi(x_j).$$
Since $\varphi(x_j) \in F_{j+k}$ and the sum over distinct $j+k$ is direct, each $\varphi(x_j) = 0$, so each $x_j \in \ker \varphi$. Hence $\ker \varphi = \sum_j (\ker \varphi \cap E_j)$, which is precisely the condition for $\ker \varphi$ to be a $G$-graded subspace.
