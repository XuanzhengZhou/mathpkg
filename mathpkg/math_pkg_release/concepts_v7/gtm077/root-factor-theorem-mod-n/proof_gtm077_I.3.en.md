---
role: proof
locale: en
of_concept: root-factor-theorem-mod-n
source_book: gtm077
source_chapter: "I"
source_section: "3"
---

# Proof of Root-Factor Theorem Modulo $n$ (Theorem 10)

**Statement.** If $a$ is a root of the integral polynomial $f(x)$ modulo $n$, then $f(x)$ is divisible by $x - a$ modulo $n$, and conversely.

**Proof.** Since $f(a) \equiv 0 \pmod{n}$, we have

$$f(x) \equiv f(x) - f(a) \pmod{n}.$$

Now consider the expression $\frac{f(x) - f(a)}{x - a}$. For each positive integer $m$,

$$\frac{x^m - a^m}{x - a} = x^{m-1} + a x^{m-2} + a^2 x^{m-3} + \cdots + a^{m-2} x + a^{m-1}$$

is an integral polynomial in $x$ (with integer coefficients). Since $f(x) - f(a)$ is an integral linear combination of expressions of the form $x^m - a^m$, the quotient

$$g(x) = \frac{f(x) - f(a)}{x - a}$$

is also an integral polynomial. Consequently,

$$f(x) \equiv f(x) - f(a) = (x - a) g(x) \pmod{n},$$

which shows that $f(x)$ is divisible by $x - a$ modulo $n$.

Conversely, if $f(x) \equiv (x - a) g(x) \pmod{n}$ for some integral polynomial $g(x)$, then substituting $x = a$ gives

$$f(a) \equiv (a - a) g(a) = 0 \pmod{n},$$

so $a$ is a root of $f(x)$ modulo $n$. $\square$
