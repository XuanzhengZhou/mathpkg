---
role: proof
locale: en
of_concept: theorem-12
source_book: gtm077
source_chapter: "I"
source_section: "3"
---
# Proof of Theorem 12: Bound on the Number of Roots modulo a Prime

**Theorem.** An integral polynomial $f(x)$ of degree $k \geq 0$ has at most $k$ incongruent roots modulo a prime $p$, unless $f(x) quiv 0 \pmod{p}$, in which case all coefficients of $f(x)$ are divisible by $p$ and every integer is a root.

*Proof.* We proceed by induction on the degree $k$.

**Base case: $k = 0$.** Then $f(x) = c_0$ is a constant polynomial. The congruence $c_0 quiv 0 \pmod{p}$ has either
- $0$ solutions, if $p 
mid c_0$ (since the congruence is never satisfied), or
- every integer as a solution, if $p \mid c_0$ (the polynomial is identically zero modulo $p$).

In the first case the number of roots is $0 \leq 0 = k$, and in the second case the theorem's exception applies. So the statement holds for $k = 0$.

**Inductive step.** Assume the theorem holds for all polynomials of degree $\leq k - 1$ (with $k \geq 1$). Let $f(x)$ be an integral polynomial of degree $k$ that is not identically zero modulo $p$ (i.e., not all coefficients are divisible by $p$).

If $f(x)$ has no root modulo $p$, then the number of roots is $0 \leq k$, and the statement is satisfied.

Otherwise, let $a$ be a root of $f(x)$ modulo $p$, so $f(a) quiv 0 \pmod{p}$. By the proof of Theorem 10, we can factor

$$f(x) quiv (x - a) f_1(x) \pmod{p},$$

where $f_1(x)$ is an integral polynomial of degree at most $k - 1$.

Now let $b$ be any root of $f(x)$ modulo $p$ with $b 
otquiv a \pmod{p}$. Substituting $x = b$ gives

$$(b - a) f_1(b) quiv f(b) quiv 0 \pmod{p}.$$

Since $b 
otquiv a \pmod{p}$, we have $b - a 
otquiv 0 \pmod{p}$. Because $p$ is prime and does not divide $b - a$, it must divide $f_1(b)$. Hence $f_1(b) quiv 0 \pmod{p}$; i.e., $b$ is a root of $f_1(x)$ modulo $p$.

Therefore every root of $f(x)$ modulo $p$ is congruent either to $a$ or to a root of $f_1(x)$ modulo $p$. By the induction hypothesis, $f_1(x)$ has at most $k - 1$ incongruent roots modulo $p$. Consequently, $f(x)$ has at most

$$1 + (k - 1) = k$$

incongruent roots modulo $p$. This completes the induction. $\square$

This theorem is fundamental for the theory of polynomial congruences: it shows that, modulo a prime, a non-zero polynomial of degree $k$ can vanish at no more than $k$ distinct residue classes—just as in ordinary algebra over a field.

