---
role: proof
locale: en
of_concept: quadratic-field-decomposition
source_book: gtm077
source_chapter: "V"
source_section: "29"
---
# Proof of Theorem 89: Decomposition Law for Quadratic Fields

Let $K = \mathbb{Q}(\sqrt{d})$ with $d$ squarefree and discriminant $D$. We have

$$D = \begin{cases} 4d, & d \equiv 2, 3 \pmod{4}, \\ d, & d \equiv 1 \pmod{4}, \end{cases}$$

and an integral basis $1, \frac{D + \sqrt{D}}{2}$.

Let $p$ be a rational prime with $p \nmid D$.

**Splitting case.** Assume $x^2 \equiv D \pmod{4p}$ has a solution $x = r$. Define

$$\mathfrak{a} = \left(p, r - \frac{D + \sqrt{D}}{2}\right).$$

Then

$$\mathfrak{a}\mathfrak{a}' = \left(p^2, p\left(r - \frac{D + \sqrt{D}}{2}\right), p\left(r - \frac{D - \sqrt{D}}{2}\right), \frac{(2r - D)^2 - D}{4}\right).$$

By the congruence condition $r^2 \equiv D \pmod{4p}$, the last term is an integer divisible by $p$. Factoring out $(p)$:

$$\mathfrak{a}\mathfrak{a}' = (p)\left(p, r - \frac{D - \sqrt{D}}{2}, r - \frac{D + \sqrt{D}}{2}, \frac{(2r-D)^2 - D}{4p}\right).$$

The ideal in brackets contains $p$ and the difference between its second and third generators, namely $\sqrt{D}$. Since $\gcd(p, D) = 1$, it contains two coprime numbers $p$ and $D$, hence equals $(1)$. Therefore $\mathfrak{a}\mathfrak{a}' = (p)$. Thus

$$\mathfrak{p} = \left(p, r - \frac{D + \sqrt{D}}{2}\right), \quad \mathfrak{p}' = \left(p, r - \frac{D - \sqrt{D}}{2}\right)$$

are distinct prime ideals with $(p) = \mathfrak{p}\mathfrak{p}'$.

**Converse.** If $p$ splits, set $\omega = (x + \sqrt{D})/2$ where $x$ is a solution of (45). Then $\omega/p$ is not integral (since $((\omega - \omega')/p)^2 = D/p^2$ is not integral), yet $p \mid \omega\omega'$. Hence $(p)$ is not prime in $K$, so $p$ splits.

**Ramification.** If $q$ is an odd prime divisor of $D$ (equivalently $q \mid d$), set

$$\mathfrak{q} = \left(q, \frac{D + \sqrt{D}}{2}\right).$$

Then $\mathfrak{q}^2 = (q)$, showing that $q$ ramifies in $K$.
