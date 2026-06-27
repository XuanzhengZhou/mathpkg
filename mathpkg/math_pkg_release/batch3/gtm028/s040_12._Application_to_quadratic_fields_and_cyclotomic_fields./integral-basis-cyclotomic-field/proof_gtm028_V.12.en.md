---
role: proof
locale: en
of_concept: integral-basis-cyclotomic-field
source_book: gtm028
source_chapter: "V"
source_section: "12"
---

Let $z$ be a primitive $p$-th root of unity and let $R'$ be the ring of algebraic integers in $\mathbb{Q}(z)$. Clearly $z \in R'$.

For $r = 2, 3, \ldots, p-1$, consider the element $\frac{1 - z^r}{1 - z}$. This element belongs to $R'$ since it equals the sum $1 + z + \cdots + z^{r-1}$, which is a sum of algebraic integers. Its inverse $\frac{1 - z}{1 - z^r}$ is also in $R'$: let $r'$ be an integer such that $rr' \equiv 1 \pmod{p}$ (which exists since $p \nmid r$). Then $z = (z^r)^{r'}$, and
$$\frac{1 - z}{1 - z^r} = 1 + z^r + z^{2r} + \cdots + z^{(r'-1)r} \in R'.$$
Therefore $\frac{1 - z^r}{1 - z}$ is a unit in $R'$ for each $r = 2, \ldots, p-1$.

Now consider the factorization:
$$p = F(1) = 1 + 1 + \cdots + 1 = \sum_{i=0}^{p-1} 1^i = (1 - z)(1 - z^2) \cdots (1 - z^{p-1}).$$

Since each factor $(1 - z^r)$ is $(1 - z)$ times a unit, we have the equality of ideals:
$$R'p = R'(1 - z)^{p-1}.$$

The formula $\sum e_i f_i = [\mathbb{Q}(z) : \mathbb{Q}]$ (Corollary to Theorem 21 of §9) concerning the decomposition of a prime ideal shows that $p-1 \leq [\mathbb{Q}(z) : \mathbb{Q}]$. Since $z$ satisfies the irreducible polynomial $F(Z) = Z^{p-1} + \cdots + Z + 1$ over $\mathbb{Q}$, we have $[\mathbb{Q}(z) : \mathbb{Q}] \leq p-1$. Hence $[\mathbb{Q}(z) : \mathbb{Q}] = p-1$.

The fact that $p^{p-2}$ is the discriminant of $R'$ over $\mathbb{Z}$ and that $\{1, z, \ldots, z^{p-2}\}$ is an integral basis follows from Theorem 30 (the general discriminant formula for cyclotomic fields).
