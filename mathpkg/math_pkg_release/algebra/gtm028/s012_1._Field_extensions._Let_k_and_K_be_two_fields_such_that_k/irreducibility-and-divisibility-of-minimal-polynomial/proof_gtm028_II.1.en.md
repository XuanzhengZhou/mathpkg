---
role: proof
locale: en
of_concept: irreducibility-and-divisibility-of-minimal-polynomial
source_book: gtm028
source_chapter: "II"
source_section: "1"
---

Assume that $f(X) = f_1(X) f_2(X)$, where $f_1, f_2 \in k[X]$. Since $f(x) = 0$, we have $f_1(x)f_2(x) = 0$. Since $K$ is a field (hence an integral domain without zero divisors), either $f_1(x) = 0$ or $f_2(x) = 0$. Let, say, $f_1(x) = 0$. Since $\partial f_1 \leq \partial f$, and since $f(X)$ is a polynomial of least degree such that $f(x) = 0$, we must have $\partial f_1 = \partial f$, and hence $f_2$ is of degree zero, that is, $f_2$ is a unit in $k[X]$. This shows that $f(X)$ is irreducible.

Let $g(X)$ be a polynomial in $k[X]$ such that $g(x) = 0$. Since $k[X]$ is a euclidean domain (I, \S 17, Theorem 9), division by $f(X)$ yields:
$$g(X) = q(X)f(X) + r(X),$$
where either $r(X) = 0$ or $\partial r < \partial f$. Substituting $x$ for $X$ we have $g(x) = r(x)$, whence $r(x) = 0$. Therefore we cannot have $\partial r < \partial f$, and hence $r(X) = 0$, and $f(X)$ divides $g(X)$. This completes the proof.
