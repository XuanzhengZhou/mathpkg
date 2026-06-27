---
role: proof
locale: en
of_concept: localization-preserves-integral-closure
source_book: gtm028
source_chapter: "V"
source_section: "§3. Integrally closed rings"
---

Let $R$ be integrally closed, $S$ a multiplicative subset, and $x \in K$ (the quotient field of $R$) an element integral over $R_S$. Then $x$ satisfies an equation:

$$x^n + (a_{n-1}/s)x^{n-1} + \cdots + a_0/s = 0, \quad a_i \in R,$$

since any finite number of elements of $R_S$ have a common denominator $s \in S$. Multiplying by $s^n$, we obtain:

$$(sx)^n + a_{n-1}(sx)^{n-1} + \cdots + a_0 s^{n-1} = 0,$$

showing that $sx$ is integral over $R$. Since $R$ is integrally closed, $sx \in R$. Writing $sx = z \in R$, we get $x = z/s \in R_S$. Therefore $R_S$ is integrally closed.
