---
role: proof
locale: en
of_concept: decomposition-in-quadratic-fields
source_book: gtm077
source_chapter: "V"
source_section: "29"
---
# Proof of Theorem 89: Decomposition Law for Quadratic Fields

Let $K = \mathbb{Q}(\sqrt{d})$ where $d$ is a squarefree integer. The discriminant $D$ of $K$ is given by

$$D = \begin{cases} 4d, & \text{if } d \equiv 2, 3 \pmod{4}, \\ d, & \text{if } d \equiv 1 \pmod{4}. \end{cases}$$

A basis for the ring of integers is

$$1, \frac{D + \sqrt{D}}{2}.$$

Let $p$ be a rational prime not dividing $D$.

**First direction.** Suppose the congruence

$$x^2 \equiv D \pmod{4p} \tag{45}$$

has a rational integer solution $x = r$. Set

$$\mathfrak{a} = \left(p, r - \frac{D + \sqrt{D}}{2}\right).$$

Then

$$\mathfrak{a}\mathfrak{a}' = \left(p^2, p\left(r - \frac{D + \sqrt{D}}{2}\right), p\left(r - \frac{D - \sqrt{D}}{2}\right), \frac{(2r - D)^2 - D}{4}\right).$$

The last term is $\frac{(2r-D)^2 - D}{4}$, which is divisible by $p$ by the hypothesis $r^2 \equiv D \pmod{4p}$. Thus we can factor out $(p)$:

$$\mathfrak{a}\mathfrak{a}' = (p)\left(p, r - \frac{D - \sqrt{D}}{2}, r - \frac{D + \sqrt{D}}{2}, \frac{(2r-D)^2 - D}{4p}\right).$$

The ideal factor shown is actually $(1)$, because it contains $p$ and the difference between the second and third generators, which is $\sqrt{D}$. Since $p$ and $D$ are relatively prime (as $p \nmid D$), this ideal therefore contains two coprime numbers $p$ and $D$, and hence equals the full ring.

Consequently $\mathfrak{a}\mathfrak{a}' = (p)$, and since $\mathfrak{a}$ and $\mathfrak{a}'$ are proper ideals whose product equals $(p)$, they must be prime ideals. Moreover they are distinct because their GCD contains both $p$ and $D$, which are coprime. Setting

$$\mathfrak{p} = \left(p, r - \frac{D + \sqrt{D}}{2}\right), \quad \mathfrak{p}' = \left(p, r - \frac{D - \sqrt{D}}{2}\right),$$

we obtain the splitting $(p) = \mathfrak{p}\mathfrak{p}'$ into two distinct prime ideals.

**Second direction.** Conversely, suppose $p$ splits in $K(\sqrt{D})$ into two distinct prime factors. Then there exists an integer

$$\omega = \frac{x + \sqrt{D}}{2}$$

which is a solution of (45) and such that $\omega/p$ is not an integer, because $((\omega - \omega')/p)^2 = D/p^2$ is not an integer. Since $p$ does not divide $\omega$ or its conjugate $\omega'$ individually, but does divide their product $\omega\omega'$ (as $p \mid N(\omega)$), the ideal $(p)$ cannot be prime in $K(\sqrt{D})$. Thus $p$ splits in $K(\sqrt{D})$ into two prime factors which are distinct from one another, and the congruence (45) is solvable.
