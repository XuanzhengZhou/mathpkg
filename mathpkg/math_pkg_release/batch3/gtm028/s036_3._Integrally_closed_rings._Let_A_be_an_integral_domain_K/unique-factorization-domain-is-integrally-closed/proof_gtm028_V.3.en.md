---
role: proof
locale: en
of_concept: unique-factorization-domain-is-integrally-closed
source_book: gtm028
source_chapter: "V"
source_section: "§3. Integrally closed rings"
---

Let $A$ be a UFD with quotient field $K$, and let $x/y \in K$ (where $x, y \in A$, $y \neq 0$, and the fraction is in lowest terms, i.e., $x$ and $y$ have no common prime factor) be integral over $A$. Then there exists an equation of integral dependence:

$$(x/y)^n + a_{n-1}(x/y)^{n-1} + \cdots + a_0 = 0, \quad a_i \in A.$$

Multiplying by $y^n$, we obtain:

$$x^n + a_{n-1}x^{n-1}y + \cdots + a_0 y^n = 0.$$

Thus $y$ divides $x^n$ in $A$. However, since $x$ and $y$ are coprime (no common prime factor by uniqueness of factorization), and $y$ divides $x^n$, every prime factor of $y$ must divide $x$. By coprimality, $y$ has no prime factors, so $y$ is a unit. Hence $x/y \in A$, proving that $A$ is integrally closed.
