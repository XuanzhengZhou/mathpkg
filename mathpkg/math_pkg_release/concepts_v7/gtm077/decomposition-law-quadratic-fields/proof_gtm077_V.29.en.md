---
role: proof
locale: en
of_concept: decomposition-law-quadratic-fields
source_book: gtm077
source_chapter: "V"
source_section: "29"
---
# Proof of the Decomposition Law for Rational Primes in Quadratic Fields

Let $K = \mathbb{Q}(\sqrt{d})$ where $d$ is a squarefree integer. The discriminant $D$ of $K$ is

$$D = \begin{cases} 4d, & \text{if } d \equiv 2, 3 \pmod{4}, \\ d, & \text{if } d \equiv 1 \pmod{4}. \end{cases}$$

An integral basis is $1, \frac{D + \sqrt{D}}{2}$.

Let $p$ be a rational prime not dividing $D$.

**Case 1: $p$ splits.** Suppose the congruence

$$x^2 \equiv D \pmod{4p}$$

has a rational integer solution $x = r$. Set

$$\mathfrak{a} = \left(p, r - \frac{D + \sqrt{D}}{2}\right).$$

Computing the product with its conjugate:

$$\mathfrak{a}\mathfrak{a}' = \left(p^2, p\left(r - \frac{D + \sqrt{D}}{2}\right), p\left(r - \frac{D - \sqrt{D}}{2}\right), \frac{(2r - D)^2 - D}{4}\right).$$

Since $r^2 \equiv D \pmod{4p}$, the last term is divisible by $p$, and we can factor $(p)$ out:

$$\mathfrak{a}\mathfrak{a}' = (p)\left(p, r - \frac{D - \sqrt{D}}{2}, r - \frac{D + \sqrt{D}}{2}, \frac{(2r-D)^2 - D}{4p}\right).$$

The bracketed ideal contains $p$ and the difference of the second and third generators, which equals $\sqrt{D}$. Since $\gcd(p, D) = 1$, this ideal contains two coprime numbers and thus equals $(1)$. Hence $\mathfrak{a}\mathfrak{a}' = (p)$, and we obtain the two distinct prime ideals

$$\mathfrak{p} = \left(p, r - \frac{D + \sqrt{D}}{2}\right), \quad \mathfrak{p}' = \left(p, r - \frac{D - \sqrt{D}}{2}\right)$$

satisfying $(p) = \mathfrak{p}\mathfrak{p}'$. These are distinct because $(\mathfrak{p}, \mathfrak{p}')$ contains $p$ and $D$, which are coprime.

Conversely, if $(p) = \mathfrak{p}\mathfrak{p}'$ with $\mathfrak{p} \neq \mathfrak{p}'$, then the integer $\omega = (x + \sqrt{D})/2$ with $x$ a solution of (45) satisfies $\omega/p \notin \mathcal{O}_K$, so $p$ does not divide $\omega$ nor $\omega'$ individually but divides their product $\omega\omega'$. Hence $(p)$ is not prime in $K$, implying it splits.

**Case 2: Quadratic residue formulation.** For odd $p \nmid d$, the solvability of $x^2 \equiv d \pmod{p}$ is equivalent to the Legendre symbol $\left(\frac{d}{p}\right) = 1$. When this holds, $p$ splits. When $\left(\frac{d}{p}\right) = -1$, the congruence is unsolvable and $p$ remains prime (inert) in $K$. When $p \mid d$, the prime $p$ ramifies: $(p) = \mathfrak{p}^2$.
