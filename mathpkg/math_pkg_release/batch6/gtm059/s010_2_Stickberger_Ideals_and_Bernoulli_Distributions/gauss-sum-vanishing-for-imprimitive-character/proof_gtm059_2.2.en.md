---
role: proof
locale: en
of_concept: gauss-sum-vanishing-for-imprimitive-character
source_book: gtm059
source_chapter: "2"
source_section: "2"
---

Using the prime power decomposition, we may assume without loss of generality that $m = p^r$ is a prime power. Let $A = \mathbb{Z}(p^r)^\times$ and suppose the conductor of $\chi$ is $p^r$ but the conductor of $\lambda$ divides $p^{r-1}$. Decompose $A$ into cosets:
$$
A = \bigcup_{a} a(1 + p^{r-1}A).
$$
Then
$$
S(\chi, \lambda) = \sum_{a} \chi(a)\lambda(a) \sum_{x \in 1 + p^{r-1}A} \chi(x)\lambda(x).
$$
Since $\chi$ is assumed primitive, it is nontrivial on $1 + p^{r-1}A$, while $\lambda$ is trivial on this subgroup (as its conductor divides $p^{r-1}$). By character orthogonality, the inner sum vanishes, hence $S(\chi, \lambda) = 0$.
