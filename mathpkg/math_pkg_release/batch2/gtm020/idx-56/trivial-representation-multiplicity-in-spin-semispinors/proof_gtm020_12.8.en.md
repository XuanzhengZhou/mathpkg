---
role: proof
locale: en
of_concept: trivial-representation-multiplicity-in-spin-semispinors
source_book: gtm020
source_chapter: "12"
source_section: "12.8"
---

For $\Delta_m$ ($m = 2r$ or $2r+1$), consider the roots $z_1 + z_1^{-1}, \ldots, z_r + z_r^{-1}$ of the associated polynomial. The constant term is $(-1)^r P(0, \ldots, 0) = (-1)^r \prod_{1 \leq j \leq r} (z_j + z_j^{-1})$. By (5.1) there is a polynomial $f_r$ of degree $r$ with $x^r + x^{-r} = f_r(x + x^{-1})$. Since $0 = z_j^r + z_j^{-r} = f_r(z_j + z_j^{-1})$, the $r$ roots of $f_r$ are $z_1 + z_1^{-1}, \ldots, z_r + z_r^{-1}$.

To calculate the constant term, substitute $x = i$. Then $x + x^{-1} = i + i^{-1} = 0$, and

$$f_r(0) = f_r(i + i^{-1}) = i^r + i^{-r} = i^r(1 + (-1)^r).$$

Evaluating for different $r \bmod 4$:
- $r \equiv 0 \pmod{4}$: $i^r = 1$, $1 + (-1)^r = 2$, so multiplicity is $2$.
- $r \equiv 2 \pmod{4}$: $i^r = -1$, $1 + (-1)^r = 2$, so multiplicity is $-2$.
- $r \equiv 1, 3 \pmod{4}$: $1 + (-1)^r = 0$, so multiplicity is $0$.

Using this result together with (11.7) and the relation $\Delta_{2r} = \Delta_{2r}^+ + \Delta_{2r}^-$, one obtains a second proof that $\Delta_{8r}^+$ and $\Delta_{8r}^-$ are real and that $\Delta_{8r+4}^+$ and $\Delta_{8r+4}^-$ are quaternionic.
