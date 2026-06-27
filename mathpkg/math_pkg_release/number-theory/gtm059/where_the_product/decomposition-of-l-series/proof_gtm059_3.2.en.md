---
role: proof
locale: en
of_concept: decomposition-of-l-series
source_book: gtm059
source_chapter: "3"
source_section: "2"
---

The proof proceeds by verifying the Euler product factorization prime by prime. For each prime $p$, let $(p) = \mathfrak{p}_1^{e_1} \cdots \mathfrak{p}_g^{e_g}$ be the decomposition of $p$ into prime ideals of $K$, with $N\mathfrak{p}_i = p^{f_i}$. The Euler factor of $\zeta_K(s)$ at $p$ is

$$\prod_{\mathfrak{p} \mid p} \left(1 - \frac{1}{N\mathfrak{p}^s}\right)^{-1} = \prod_{i=1}^g \left(1 - \frac{1}{p^{f_is}}\right)^{-e_i}.$$

On the other hand, the characters $\chi$ of the Galois group correspond to characters on the decomposition group at $p$. When $p \nmid m$ (the conductor), each character $\chi$ yields the factor $(1 - \chi(p)p^{-s})^{-1}$ in the Dirichlet $L$-series. By the representation theory of finite abelian groups (applied to the Galois group of $K/\mathbb{Q}$), the identity

$$\prod_{i=1}^g (1 - T^{\,f_i})^{-e_i} = \prod_{\chi} (1 - \chi(p) T)$$

holds, where $T = p^{-s}$ and the right-hand product runs over all characters of the Galois group. Substituting the primitive characters inducing these characters yields the factorization into primitive $L$-series. References: [La] Chapter XII, [1].
