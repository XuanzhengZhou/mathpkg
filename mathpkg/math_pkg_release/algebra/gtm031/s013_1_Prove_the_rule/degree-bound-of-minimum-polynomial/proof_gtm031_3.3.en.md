---
role: proof
locale: en
of_concept: degree-bound-of-minimum-polynomial
source_book: gtm031
source_chapter: "The Theory of a Single Linear Transformation"
source_section: "3"
---

*Proof.* By Theorem 1, there exists a vector $u \in \Re$ whose order $\mu_u(\lambda)$ equals the minimum polynomial $\mu(\lambda)$ of $A$. The degree of $\mu_u(\lambda)$ equals the dimension of the cyclic subspace $\{u\}$, since $(u, uA, \dots, uA^{r-1})$ is a basis for $\{u\}$ where $r = \deg \mu_u(\lambda)$. As $\{u\}$ is a subspace of $\Re$, its dimension cannot exceed $n = \dim \Re$. Therefore

$$\deg \mu(\lambda) = \deg \mu_u(\lambda) = \dim \{u\} \leq n.$$

$\square$
