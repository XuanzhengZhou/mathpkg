---
role: proof
locale: en
of_concept: weierstrass-preparation-theorem
source_book: gtm059
source_chapter: "5"
source_section: "2"
---

**Proof.** Apply the Weierstrass Division Theorem (Theorem 2.1) with $g(X) = X^n$. There exist unique $q(X) \in A[[X]]$ and $r(X) \in A[X]$ with $\deg r < n$ such that

$$X^n = q(X) f(X) + r(X).$$

Write $f(X) = a_n X^n + \sum_{k \neq n} a_k X^k$ where $a_n \in A^\times$ and $a_0, \dots, a_{n-1} \in \mathfrak{m}$. Reducing modulo $\mathfrak{m}$, we have $\bar{f}(X) = \bar{a}_n X^n$ (since all lower coefficients vanish mod $\mathfrak{m}$), so $\bar{q}(X) \cdot \bar{a}_n X^n = X^n$ in $(A/\mathfrak{m})[[X]]$, giving $\bar{q}(X) = \bar{a}_n^{-1}$. Thus $q(X)$ is a unit in $A[[X]]$ (its constant term is a unit modulo $\mathfrak{m}$, hence a unit in $A$ by completeness).

Now from $X^n = q f + r$ we obtain $q f = X^n - r$. Set $P(X) = X^n - r(X)$ and $u(X) = q(X)^{-1}$. Then

$$f(X) = u(X)^{-1} (X^n - r(X)) = P(X) \cdot u(X)$$

with $u$ a unit in $A[[X]]$. Since $r(X)$ has degree $< n$ and all coefficients of $r$ lie in $\mathfrak{m}$ (which follows from reducing the equation modulo $\mathfrak{m}$), $P(X) = X^n - r(X)$ is a distinguished polynomial.

For uniqueness, suppose $f = P_1 u_1 = P_2 u_2$ with distinguished polynomials $P_1, P_2$ of degree $n$ and units $u_1, u_2$. Then $P_1 = P_2 (u_2 u_1^{-1})$. Applying the division theorem to divide $P_1$ by $P_2$ gives a unique quotient and remainder; since both are monic of the same degree and the quotient is a unit, we must have $P_1 = P_2$ and $u_1 = u_2$.

The integer $n$ is called the **Weierstrass degree** of $f$, and the polynomial $P(X)$ is called the **Weierstrass polynomial** associated to $f$.
