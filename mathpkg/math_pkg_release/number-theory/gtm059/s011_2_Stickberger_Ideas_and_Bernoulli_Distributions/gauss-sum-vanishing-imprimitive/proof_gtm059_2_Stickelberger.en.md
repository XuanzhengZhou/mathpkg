---
role: proof
locale: en
of_concept: gauss-sum-vanishing-imprimitive
source_book: gtm059
source_chapter: "2"
source_section: "Stickelberger Ideals and Bernoulli Distributions"
---

**Proof of Theorem 1.1.**

Using the prime power decomposition, we may assume without loss of generality that $m = p^r$ is a prime power. Let $A = p^r \mathbb{Z}_p$ denote the corresponding local ring.

Also without loss of generality, we may assume the conductor is $d = p^\rho$ for some integer $\rho \ge 1$, and that the character $\chi$ factors through $\mathbb{Z}/p^\rho\mathbb{Z}$ but not through any smaller modulus.

Decompose the group $\mathbb{Z}/p^r\mathbb{Z}$ into cosets of the subgroup $p^{r-\rho} \mathbb{Z}/p^r\mathbb{Z}$:
$$\mathbb{Z}/p^r\mathbb{Z} = \bigcup_{a} \left(a + p^\rho \mathbb{Z}/p^r\mathbb{Z}\right).$$

The Gauss sum can then be written as a double sum:
$$S(\chi, n) = \sum_{a} \chi(a) \zeta^{na} \sum_{y \in p^\rho \mathbb{Z}/p^r\mathbb{Z}} \chi(1+y) \zeta^{ny}.$$

Since $\chi$ is assumed primitive of conductor $p^\rho$, it is non-trivial on the subgroup $1 + p^{\rho-1} \mathbb{Z}/p^r\mathbb{Z}$. By character orthogonality on this subgroup, the inner sum over each coset vanishes:
$$\sum_{y \in p^\rho \mathbb{Z}/p^r\mathbb{Z}} \chi(1+y) \zeta^{ny} = 0.$$

Thus the total Gauss sum $S(\chi, n) = 0$, proving the theorem.
