---
role: proof
locale: en
of_concept: gauss-lemma-primitive
source_book: gtm077
source_chapter: "I"
source_section: "3"
---

# Proof of Gauss's Lemma on Primitive Polynomials (Theorem 13a)

**Preliminary: Theorem 13.** If $f(x)$ and $g(x)$ are integral polynomials and $f(x) g(x) \equiv 0 \pmod{p}$ for a prime $p$, then either $f(x) \equiv 0 \pmod{p}$ or $g(x) \equiv 0 \pmod{p}$.

*Proof of Theorem 13.* Suppose, to the contrary, that neither $f(x) \equiv 0 \pmod{p}$ nor $g(x) \equiv 0 \pmod{p}$. This means that not all coefficients of $f(x)$ are divisible by $p$, and not all coefficients of $g(x)$ are divisible by $p$.

Reduce $f(x)$ and $g(x)$ modulo $p$ by discarding all terms whose coefficients are divisible by $p$. Let $f_1(x)$ and $g_1(x)$ be the resulting non-zero polynomials (i.e., $f(x) \equiv f_1(x) \pmod{p}$ and $g(x) \equiv g_1(x) \pmod{p}$, where neither $f_1$ nor $g_1$ is identically zero modulo $p$, and all their coefficients are not divisible by $p$ after reduction). Then

$$f_1(x) g_1(x) \equiv f(x) g(x) \equiv 0 \pmod{p}.$$

Consider the highest-degree term of the product $f_1(x) g_1(x)$. It is the product of the leading term of $f_1(x)$ and the leading term of $g_1(x)$. Let these leading coefficients be $a \not\equiv 0 \pmod{p}$ and $b \not\equiv 0 \pmod{p}$ respectively. Since $p$ is prime, $ab \not\equiv 0 \pmod{p}$.

But the product $f_1(x) g_1(x) \equiv 0 \pmod{p}$, which means every coefficient of $f_1(x) g_1(x)$ is divisible by $p$, including the leading coefficient $ab$. This contradicts $ab \not\equiv 0 \pmod{p}$. Therefore our assumption was false, and either $f(x) \equiv 0 \pmod{p}$ or $g(x) \equiv 0 \pmod{p}$. $\square$

**Definition.** An integral polynomial is called *primitive* if its coefficients are relatively prime, i.e., if for every prime $p$, the polynomial is not identically zero modulo $p$.

**Theorem 13a (Gauss's Lemma).** The product of two primitive polynomials is again a primitive polynomial.

*Proof.* Let $f(x)$ and $g(x)$ be primitive integral polynomials. Suppose, for contradiction, that their product $h(x) = f(x) g(x)$ is not primitive. Then there exists a prime $p$ such that all coefficients of $h(x)$ are divisible by $p$, i.e.,

$$h(x) = f(x) g(x) \equiv 0 \pmod{p}.$$

By Theorem 13, this implies either $f(x) \equiv 0 \pmod{p}$ or $g(x) \equiv 0 \pmod{p}$. But this contradicts the assumption that $f(x)$ and $g(x)$ are primitive (since for a primitive polynomial, no prime divides all its coefficients simultaneously). Therefore $h(x)$ must be primitive. $\square$
