---
role: proof
locale: en
of_concept: gcd-of-polynomials-over-field
source_book: gtm077
source_chapter: "IV"
source_section: "17"
---
# Proof of Theorem 48: Greatest Common Divisor of Polynomials over a Field

Let $f_1(x)$ and $f_2(x)$ be two arbitrary nonzero polynomials over a number field $k$.

Among the polynomials of the form

$$L(x) = u_1(x)f_1(x) + u_2(x)f_2(x),$$

where $u_1(x)$ and $u_2(x)$ run through all polynomials over $k$, choose one with leading coefficient $1$ whose degree is as small as possible. Let $d(x)$ be such a polynomial, and suppose that

$$d(x) = g_1(x)f_1(x) + g_2(x)f_2(x) \tag{33}$$

for some $g_1(x), g_2(x)$ over $k$.

If $d(x)$ is of degree $0$, then $d(x) = 1$, and consequently $d(x)$ divides both $f_1(x)$ and $f_2(x)$. If $d(x)$ is of higher degree, we show it must still divide $f_1(x)$: using the division algorithm (32), write

$$f_1(x) = q(x)d(x) + r(x),$$

where the degree of $r(x)$ is strictly less than that of $d(x)$. The coefficients of $q(x)$ and $r(x)$ can be calculated entirely from those of $f_1(x)$ and $d(x)$ by rational operations, hence $q(x), r(x)$ are also polynomials over $k$. Then

$$r(x) = f_1(x) - q(x)d(x) = f_1(x) - q(x)(g_1(x)f_1(x) + g_2(x)f_2(x)) = (1 - q(x)g_1(x))f_1(x) - q(x)g_2(x)f_2(x),$$

which is again of the form $u_1(x)f_1(x) + u_2(x)f_2(x)$ with coefficients in $k$. If $r(x) \neq 0$, we could make its leading coefficient $1$ by multiplying by a suitable constant from $k$, obtaining a polynomial of the same form with degree smaller than $d(x)$, contradicting the minimality of the degree of $d(x)$. Therefore $r(x) = 0$, which means $d(x) \mid f_1(x)$. By symmetry, $d(x) \mid f_2(x)$.

Now let $h(x)$ be any common divisor of $f_1(x)$ and $f_2(x)$. Then $h(x)$ divides any linear combination $u_1(x)f_1(x) + u_2(x)f_2(x)$, and in particular $h(x) \mid d(x)$. Thus $d(x)$ is a greatest common divisor. The condition that the leading coefficient is $1$ guarantees uniqueness.

We write $(f_1(x), f_2(x)) = d(x)$ and call $f_1(x)$ and $f_2(x)$ *relatively prime* if $d = 1$.
