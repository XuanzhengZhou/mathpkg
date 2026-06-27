---
role: proof
locale: en
of_concept: polynomial-root-divisibility-mod
source_book: gtm077
source_chapter: "I"
source_section: "3"
---
# Proof of Theorem 10: Root and Divisibility by $x-a$ modulo $n$

**Theorem.** If $a$ is a root of the integral polynomial $f(x)$ modulo $n$ (i.e., $f(a) quiv 0 \pmod{n}$), then $f(x)$ is divisible by $x - a$ modulo $n$, and conversely.

*Proof.* Since $f(a) quiv 0 \pmod{n}$, we have

$$f(x) quiv f(x) - f(a) \pmod{n}.$$

Now consider the difference $f(x) - f(a)$. For any monomial $x^m$, the factorisation

$$rac{x^m - a^m}{x - a} = x^{m-1} + a x^{m-2} + a^2 x^{m-3} + 