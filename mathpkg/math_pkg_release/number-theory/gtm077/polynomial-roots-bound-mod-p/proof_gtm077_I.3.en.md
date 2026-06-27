---
role: proof
locale: en
of_concept: polynomial-roots-bound-mod-p
source_book: gtm077
source_chapter: "I"
source_section: "3"
---

# Proof of Bound on Roots of Polynomials Modulo a Prime (Theorem 12)

**Statement.** An integral polynomial $f(x)$ of degree $k$ has no more than $k$ incongruent roots modulo a prime $p$, unless $f(x) \equiv 0 \pmod{p}$, in which case all coefficients are divisible by $p$ (and every integer is a root).

**Proof.** We proceed by induction on the degree $k$.

**Base case $k = 0$.** If $f(x) = c_0$ is a constant polynomial, then the congruence $f(x) \equiv 0 \pmod{p}$ becomes $c_0 \equiv 0 \pmod{p}$. If $p \nmid c_0$, there are $0$ solutions, and $0 \leq 0$ holds. If $p \mid c_0$, then $f(x) \equiv 0 \pmod{p}$ for every integer $x$, which is the exceptional case where the polynomial is identically zero modulo $p$. In this case the bound does not apply (or we say there are infinitely many roots). The theorem is true for $k = 0$.

**Inductive step.** Assume the statement holds for all polynomials of degree $\leq k - 1$. Let $f(x)$ be an integral polynomial of degree $k$. If $f(x)$ has no roots modulo $p$, the statement is trivially true. Otherwise, let $a$ be a root of $f(x)$ modulo $p$. By Theorem 10 (Root-Factor Theorem), we can write

$$f(x) \equiv (x - a) f_1(x) \pmod{p},$$

where $f_1(x)$ is an integral polynomial of degree at most $k - 1$.

Now let $b$ be any root of $f(x)$ modulo $p$ with $b \not\equiv a \pmod{p}$. Substituting $x = b$,

$$f(b) \equiv (b - a) f_1(b) \equiv 0 \pmod{p}.$$

Since $p$ is prime and $b - a \not\equiv 0 \pmod{p}$ (because $b \not\equiv a$), the factor $b - a$ is not divisible by $p$. By the prime property, $p$ must divide $f_1(b)$, i.e., $f_1(b) \equiv 0 \pmod{p}$. Equivalently, by Theorem 11, every root of $f(x)$ modulo $p$ is either congruent to $a$ or is a root of $f_1(x)$ modulo $p$.

By the induction hypothesis, $f_1(x)$ has at most $k - 1$ incongruent roots modulo $p$, unless $f_1(x) \equiv 0 \pmod{p}$. If $f_1(x) \not\equiv 0 \pmod{p}$, then $f(x)$ has at most $1 + (k - 1) = k$ incongruent roots modulo $p$ (the root $a$ plus at most $k-1$ roots of $f_1$). If $f_1(x) \equiv 0 \pmod{p}$, then $f(x) \equiv (x - a) \cdot 0 \equiv 0 \pmod{p}$, which is the exceptional case where all coefficients of $f(x)$ are divisible by $p$.

This completes the induction. $\square$

**Remark.** This theorem is the analogue for polynomial congruences of Lagrange's theorem in algebra: a non-zero polynomial over a field has at most its degree many roots. Here the field is $\mathbb{Z}/p\mathbb{Z}$.
