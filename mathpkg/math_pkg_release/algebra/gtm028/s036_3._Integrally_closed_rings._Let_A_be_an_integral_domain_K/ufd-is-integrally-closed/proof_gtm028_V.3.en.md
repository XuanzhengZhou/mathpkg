---
role: proof
locale: en
of_concept: ufd-is-integrally-closed
source_book: gtm028
source_chapter: "V"
source_section: "3. Integrally closed rings"
---

Let $A$ be a unique factorization domain and let $K$ be its field of quotients. Let $x/y \in K$ (with $x, y \in A$, $y \neq 0$) be integral over $A$. We may assume that $x$ and $y$ have no common irreducible factor. There exists an equation of integral dependence:

$$\left(\frac{x}{y}\right)^n + a_{n-1}\left(\frac{x}{y}\right)^{n-1} + \cdots + a_1\left(\frac{x}{y}\right) + a_0 = 0, \quad a_i \in A.$$

Multiplying by $y^n$, we obtain

$$x^n + a_{n-1} x^{n-1} y + \cdots + a_1 x y^{n-1} + a_0 y^n = 0.$$

Hence $x^n = -y(a_{n-1}x^{n-1} + \cdots + a_1 x y^{n-2} + a_0 y^{n-1})$, so $y$ divides $x^n$ in $A$. Since $x$ and $y$ have no common irreducible factor, the unique factorization property forces $y$ to be a unit in $A$. Therefore $x/y \in A$, proving that $A$ is integrally closed.
