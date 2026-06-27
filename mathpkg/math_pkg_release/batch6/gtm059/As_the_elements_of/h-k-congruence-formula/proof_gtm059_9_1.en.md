---
role: proof
locale: en
of_concept: h-k-congruence-formula
source_book: gtm059
source_chapter: "9"
source_section: "1. A Local Pairing with the Logarithmic Derivative"
---

Without loss of generality we may assume that $m = n + 1$. We first deal with the case when $n$ is a unit. We find

$$
h_K(s) \equiv T_K(s)_n(s) \pmod{n}
$$

$$
= \sum_{i=0}^{K} a_i(s) T_i(s)
$$

by **DL 4**

$$
= \sum_{i=0}^{K} a_i(s) T_i(s)
$$

by **DL 3**.

The sums are taken over $s \in \operatorname{Gal}(K)$. For such $s$ we must have

$$
a(s) \equiv 1 \pmod{n^{K+1}}
$$

because substituting $[a(s)]$ in the identity $a(s) = \sum_{i=0}^{K} a_i(s) T_i(s)$ with $s = \pi^{-n+1} = \pi^{-(n+1)}$ yields the desired congruence.

When the Frobenius power series associated with the Lubin-Tate group is in fact a polynomial

$$
[a(s)] X(s) = X(s) + \cdots + X^n
$$

and the coefficient of $X^n$ is exactly $1$ (as is the case for the basic Lubin-Tate group and the formal multiplicative group), a stronger property holds.
