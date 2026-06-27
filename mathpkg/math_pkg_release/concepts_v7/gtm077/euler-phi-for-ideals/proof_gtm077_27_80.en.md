---
role: proof
locale: en
of_concept: euler-phi-for-ideals
source_book: gtm077
source_chapter: "II"
source_section: "27"
---
# Proof of Theorem 80: Euler's Totient Function for Ideals

We must show:
1. If $(\mathfrak{a}, \mathfrak{b}) = 1$, then $\varphi(\mathfrak{a}\mathfrak{b}) = \varphi(\mathfrak{a}) \cdot \varphi(\mathfrak{b})$.
2. $\varphi(\mathfrak{a}) = N(\mathfrak{a}) \prod_{\mathfrak{p} \mid \mathfrak{a}} \left(1 - \frac{1}{N(\mathfrak{p})}\right)$,
   where $\mathfrak{p}$ runs through the distinct prime ideal divisors of $\mathfrak{a}$.

**Proof of (1).** Let $\alpha$ be chosen such that $(\alpha, \mathfrak{a}\mathfrak{b}) = \mathfrak{a}$
and $\mathfrak{a} \mid \alpha$, and $\beta$ such that
$(\beta, \mathfrak{a}\mathfrak{b}) = \mathfrak{b}$ and $\mathfrak{b} \mid \beta$.

Let $\xi$ run through a reduced residue system modulo $\mathfrak{b}$ (i.e.,
$\varphi(\mathfrak{b})$ representatives of classes relatively prime to
$\mathfrak{b}$), and $\eta$ run through a reduced residue system modulo
$\mathfrak{a}$ ($\varphi(\mathfrak{a})$ representatives). Then the numbers

$$\alpha\xi + \beta\eta$$

are all relatively prime to $\mathfrak{a}\mathfrak{b}$, pairwise incongruent
modulo $\mathfrak{a}\mathfrak{b}$, and exhaust all classes relatively prime to
$\mathfrak{a}\mathfrak{b}$. The proof is analogous to that of Theorem 79, with
the additional observation that $(\alpha\xi + \beta\eta, \mathfrak{a}\mathfrak{b}) = 1$
whenever $(\xi, \mathfrak{b}) = 1$ and $(\eta, \mathfrak{a}) = 1$, because any
common prime ideal divisor would have to divide either $\mathfrak{a}$ or
$\mathfrak{b}$, leading to a contradiction. Hence
$\varphi(\mathfrak{a}\mathfrak{b}) = \varphi(\mathfrak{a}) \cdot \varphi(\mathfrak{b})$.

**Proof of (2).** By the multiplicativity just established and unique
factorization of ideals into prime powers, it suffices to prove the formula for
a prime power $\mathfrak{p}^\nu$. The number of residue classes modulo
$\mathfrak{p}^\nu$ that are *not* relatively prime to $\mathfrak{p}^\nu$ is
$N(\mathfrak{p}^\nu) / N(\mathfrak{p}) = N(\mathfrak{p})^{\nu - 1}$ (these are
the classes divisible by $\mathfrak{p}$). Therefore

$$\varphi(\mathfrak{p}^\nu) = N(\mathfrak{p}^\nu) - \frac{N(\mathfrak{p}^\nu)}{N(\mathfrak{p})}
= N(\mathfrak{p}^\nu) \left(1 - \frac{1}{N(\mathfrak{p})}\right).$$

Combining this with multiplicativity gives the general formula

$$\varphi(\mathfrak{a}) = N(\mathfrak{a}) \prod_{\mathfrak{p} \mid \mathfrak{a}} \left(1 - \frac{1}{N(\mathfrak{p})}\right).$$
