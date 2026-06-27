---
role: proof
locale: en
of_concept: nonzeromodp-product-nonzero
source_book: gtm077
source_chapter: "I"
source_section: "3"
---
# Proof of Theorem 13: Product of Nonzero Polynomials modulo $p$

**Theorem.** If $f(x)$ and $g(x)$ are integral polynomials and $f(x) g(x) quiv 0 \pmod{p}$ for a prime $p$, then either $f(x) quiv 0 \pmod{p}$ or $g(x) quiv 0 \pmod{p}$.

*Proof.* We prove the contrapositive. Suppose that neither $f(x) quiv 0 \pmod{p}$ nor $g(x) quiv 0 \pmod{p}$. This means that not all coefficients of $f(x)$ are divisible by $p$, and not all coefficients of $g(x)$ are divisible by $p$.

Reduce $f(x)$ and $g(x)$ modulo $p$ by deleting all terms whose coefficients are divisible by $p$. Let the resulting non-zero polynomials be

$$f_1(x) quiv f(x) \pmod{p}, \qquad g_1(x) quiv g(x) \pmod{p},$$

where neither $f_1$ nor $g_1$ is identically zero modulo $p$. By construction, all non-zero coefficients of $f_1$ and $g_1$ are not divisible by $p$.

Consider the product $f_1(x) g_1(x)$. The highest-degree term of this product is the product of the leading term of $f_1(x)$ and the leading term of $g_1(x)$. Let the leading coefficients be $a 
otquiv 0 \pmod{p}$ and $b 
otquiv 0 \pmod{p}$ respectively. Since $p$ is prime and divides neither $a$ nor $b$, it does not divide their product:

$$a b 
otquiv 0 \pmod{p}.$$

Thus the leading coefficient of $f_1(x) g_1(x)$ is not divisible by $p$, so the product is not identically zero modulo $p$. Consequently,

$$f(x) g(x) quiv f_1(x) g_1(x) 
otquiv 0 \pmod{p}.$$

We have shown that if neither factor is $quiv 0 \pmod{p}$, then the product is not $quiv 0 \pmod{p}$. The contrapositive is exactly the statement of the theorem.

This theorem establishes that the ring of polynomials modulo a prime $p$ is an integral domain—a fact essential for the proof of Gauss's Lemma on primitive polynomials. $\square$

