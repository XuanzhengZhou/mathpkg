---
role: proof
locale: en
of_concept: prime-modulus-factor-theorem
source_book: gtm077
source_chapter: "I"
source_section: "3"
---

# Proof of Root-Factor Property for Prime Moduli (Theorem 11)

**Statement.** If $f(x) \equiv g(x) g_1(x) \pmod{p}$, where $p$ is a prime, then each root of $f(x)$ modulo $p$ is a root of at least one of the two polynomials $g(x)$, $g_1(x)$ modulo $p$.

**Proof.** Let $a$ be an integer such that $f(a) \equiv 0 \pmod{p}$. From the hypothesis $f(x) \equiv g(x) g_1(x) \pmod{p}$, substituting $x = a$ yields

$$g(a) \cdot g_1(a) \equiv f(a) \equiv 0 \pmod{p}.$$

Thus the prime $p$ divides the product $g(a) \cdot g_1(a)$. Since $p$ is prime, the fundamental property of primes in the integers implies that $p$ must divide at least one of the factors. Hence

$$g(a) \equiv 0 \pmod{p} \quad \text{or} \quad g_1(a) \equiv 0 \pmod{p},$$

which means that $a$ is a root of $g(x)$ modulo $p$ or a root of $g_1(x)$ modulo $p$ (or both). $\square$

**Remark.** This theorem shows that for a prime modulus $p$, the polynomial ring $(\mathbb{Z}/p\mathbb{Z})[x]$ behaves like a polynomial ring over a field: a product vanishing at a point implies that at least one factor vanishes at that point. This property does not hold for composite moduli; for example, $x = 4$ is a root of $x^2 \equiv 0 \pmod{4}$, but $4$ is not a root of $x \equiv 0 \pmod{4}$ nor of $x \equiv 0 \pmod{4}$ taken separately, illustrating that $x^2$ cannot be split as $(x)(x)$ in a way that forces one factor to vanish.
