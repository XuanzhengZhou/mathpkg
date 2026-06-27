---
role: proof
locale: en
of_concept: weierstrass-preparation-theorem
source_book: gtm059
source_chapter: "12"
source_section: "2"
---

Apply the Weierstrass Division Theorem (Theorem 1.1) with $g(X) = X^n$. There exist unique $q \in A[[X]]$ and $r \in A[X]$ of degree $< n$ such that

$$X^n = q(X) f(X) + r(X).$$

Since $f$ is $\mathfrak{m}$-regular of order $n$, we have $f(0) \in \mathfrak{m}$; reducing modulo $\mathfrak{m}$ shows that $q(X)$ is a unit in $A[[X]]$. Indeed, modulo $\mathfrak{m}$ we have $f(X) \equiv a_n X^n \pmod{\mathfrak{m}}$ with $a_n$ a unit, so $q(0)$ is a unit in $A/\mathfrak{m}$ and hence $q(X)$ is a unit in $A[[X]]$.

Then

$$f(X) = q(X)^{-1} (X^n - r(X)) = q(X)^{-1} P(X)$$

where $P(X) = X^n - r(X) = X^n + b_{n-1}X^{n-1} + \dots + b_0$ with $b_i \in \mathfrak{m}$ (since the coefficients of $r$ lie in $\mathfrak{m}$ by the division algorithm). Setting $u(X) = q(X)^{-1}$, we obtain the desired factorization

$$f(X) = P(X) \cdot u(X).$$

Uniqueness follows from the uniqueness in the Division Theorem.
