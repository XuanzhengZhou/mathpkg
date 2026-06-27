---
role: proof
locale: en
of_concept: polynomial-congruence-mod-prime-ideal
source_book: gtm077
source_chapter: "II"
source_section: "27"
---
# Proof of Theorem 82

**Theorem.** A congruence modulo a prime ideal $\mathfrak{p}$

$$x^m + \alpha_1 x^{m-1} + \cdots + \alpha_{m-1} x + \alpha_m \equiv 0 \pmod{\mathfrak{p}}$$

with integer coefficients $\alpha_i$ in $K$ has at most $m$ solutions $x$
which are incongruent modulo $\mathfrak{p}$.

**Proof.** The proof proceeds exactly as in the rational case (Theorem 12 for
rational prime congruences). We argue by induction on $m$.

For $m = 1$, the congruence $x + \alpha_1 \equiv 0 \pmod{\mathfrak{p}}$ has
exactly one solution modulo $\mathfrak{p}$ (namely $x \equiv -\alpha_1$), and
certainly at most $1$.

Assume the statement holds for all polynomials of degree less than $m$. Suppose
$f(x) = x^m + \alpha_1 x^{m-1} + \cdots + \alpha_m$ has $m+1$ pairwise
incongruent solutions $x_1, \ldots, x_{m+1}$ modulo $\mathfrak{p}$. Form the
difference polynomial

$$f(x) - f(x_1) = (x - x_1) g(x)$$

where $g(x)$ is a polynomial of degree $m-1$ with integer coefficients (the
coefficients are integers in $K$ by the usual polynomial division algorithm,
since the leading coefficient of $f$ is $1$).

For each $x_i$ with $i \geq 2$, we have
$f(x_i) \equiv 0 \pmod{\mathfrak{p}}$ and $f(x_1) \equiv 0 \pmod{\mathfrak{p}}$,
hence $(x_i - x_1) g(x_i) \equiv 0 \pmod{\mathfrak{p}}$. Since
$x_i \not\equiv x_1 \pmod{\mathfrak{p}}$ and $\mathfrak{p}$ is a prime ideal,
Theorem 86 (the zero-divisor property for polynomials modulo a prime ideal)
implies $g(x_i) \equiv 0 \pmod{\mathfrak{p}}$.

Thus $g(x)$ has $m$ pairwise incongruent solutions $x_2, \ldots, x_{m+1}$
modulo $\mathfrak{p}$, contradicting the induction hypothesis that a polynomial
of degree $m-1$ has at most $m-1$ solutions. Hence the original polynomial
$f(x)$ has at most $m$ solutions modulo $\mathfrak{p}$.
