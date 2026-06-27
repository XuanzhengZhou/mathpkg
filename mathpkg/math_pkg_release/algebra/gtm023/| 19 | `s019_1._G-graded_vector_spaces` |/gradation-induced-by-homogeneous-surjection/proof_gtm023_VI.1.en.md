---
role: proof
locale: en
of_concept: gradation-induced-by-homogeneous-surjection
source_book: gtm023
source_chapter: "VI"
source_section: "§1. G-graded vector spaces"
---

To show that $F = \sum_j F_j$ with $F_j = \varphi E_j$ defines a $G$-gradation in $F$, we notice first that since $\varphi$ is onto,
$$F = \varphi E = \varphi \sum_j E_j = \sum_j F_j.$$

To prove that the decomposition is direct, assume that $\sum_j y_j = 0$ where $y_j \in F_j$. Since $F_j = \varphi E_j$, every $y_j$ can be written in the form $y_j = \varphi x_j$ with $x_j \in E_j$. It follows that $\varphi \sum_j x_j = 0$, whence $\sum_j x_j \in \ker \varphi$.

Since $\ker \varphi$ is a graded subspace of $E$, we obtain $x_j \in \ker \varphi$ for each $j$, whence $y_j = \varphi x_j = 0$. Thus the decomposition $F = \sum_j F_j$ is direct and hence defines a $G$-gradation in $F$.

Clearly, the mapping $\varphi$ is homogeneous of degree zero with respect to this induced gradation, since $\varphi E_j = F_j \subset F_j$. Finally, any $G$-gradation of $F$ such that $\varphi$ is homogeneous of degree zero must assign to the elements of $F_j = \varphi E_j$ the degree $j$. In view of the direct decomposition, this $G$-gradation is uniquely determined by the requirement that $\varphi$ be homogeneous of degree zero.
