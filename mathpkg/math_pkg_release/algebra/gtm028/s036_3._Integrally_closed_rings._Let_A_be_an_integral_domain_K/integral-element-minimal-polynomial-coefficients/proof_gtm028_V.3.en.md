---
role: proof
locale: en
of_concept: integral-element-minimal-polynomial-coefficients
source_book: gtm028
source_chapter: "V"
source_section: "§3. Integrally closed rings"
---

Let $x$ be integral over $A$ and let $f(X) = X^m + a_1 X^{m-1} + \cdots + a_m = 0$ be an equation of integral dependence for $x$ over $A$. Since $f(X)$ is a monic polynomial with coefficients in $A$, it is also a polynomial over $K$. The minimal polynomial $g(X)$ of $x$ over $K$ divides $f(X)$ in $K[X]$, so $g(X) \mid f(X)$.

Let $\{x_1, \dots, x_n\}$ be a complete set of conjugates of $x$ over $K$, meaning the roots of $g(X)$ in an algebraic closure of $K$ (each repeated according to the degree of inseparability). Then $g(X) = \prod_i (X - x_i)$.

Since $f(x) = 0$, and $f$ has coefficients in $A \subset K$, conjugates over $K$ preserve polynomial equations with coefficients in $K$. Hence $f(x_i) = 0$ for all conjugates $x_i$, so each $x_i$ is integral over $A$.

The coefficients of $g(X) = \prod_i (X - x_i)$ are symmetric polynomials in the $x_i$. Since the $x_i$ are integral over $A$, and integral elements over $A$ form a ring (Theorem 1, §1), the elementary symmetric functions of the $x_i$ are integral over $A$. Thus all coefficients of $g(X)$ are integral over $A$.

If $A$ is integrally closed, then every element of $K$ integral over $A$ already belongs to $A$. Hence the coefficients of $g(X)$, which are integral over $A$ and belong to $K$, must lie in $A$. Therefore $g(X) \in A[X]$.
