---
role: proof
locale: en
of_concept: norm-of-cyclotomic-binomial
source_book: gtm050
source_chapter: "4"
source_section: "4.4"
---

**Proof.** Let $\alpha$ be a primitive $\lambda$-th root of unity. The norm of an element $\gamma \in \mathbb{Z}[\alpha]$ is defined as the product of its $\lambda-1$ conjugates obtained by applying the Galois automorphisms $\alpha \mapsto \alpha^j$ for $j = 1, 2, \ldots, \lambda-1$. Thus for $\gamma = x\alpha + y$,

$$
N(x\alpha + y) = \prod_{j=1}^{\lambda-1} (x\alpha^j + y).
$$

Consider the polynomial identity in the indeterminate $t$:

$$
t^\lambda - 1 = (t - 1)\prod_{j=1}^{\lambda-1} (t - \alpha^j).
$$

Substituting $t = -y/x$ (for $x \neq 0$) and multiplying by $x^\lambda$ yields

$$
x^\lambda \left( \left(-\frac{y}{x}\right)^\lambda - 1 \right) = x^\lambda \left( -\frac{y}{x} - 1 \right) \prod_{j=1}^{\lambda-1} \left( -\frac{y}{x} - \alpha^j \right).
$$

Simplifying the left side gives $(-1)^\lambda y^\lambda - x^\lambda$, and the right side gives $(-y - x) \prod_{j=1}^{\lambda-1} (-y - x\alpha^j)$. After adjusting signs, we obtain

$$
x^\lambda + y^\lambda = (x + y) \prod_{j=1}^{\lambda-1} (x\alpha^j + y),
$$

where the sign $(-1)^{\lambda-1}$ accounts for extracting $(-1)$ from each of the $\lambda-1$ factors. Since $\lambda$ is an odd prime (the cases considered by Kummer), $(-1)^{\lambda-1} = 1$, yielding the formula

$$
N(x\alpha + y) = \frac{x^\lambda + y^\lambda}{x + y}.
$$

For example, when $\lambda = 7$, $N(\alpha + 2) = \frac{1^7 + 2^7}{1 + 2} = \frac{129}{3} = 43$, which is indeed prime.
