---
role: proof
locale: en
of_concept: minimal-polynomial-of-integral-element-over-integrally-closed
source_book: gtm028
source_chapter: "V"
source_section: "§3. Integrally closed rings"
---

Let $f(x) = 0$ where $f(X) = X^n + a_{n-1}X^{n-1} + \cdots + a_0 \in A[X]$ is a monic polynomial and $x$ is integral over $A$. Let $m(X)$ be the minimal polynomial of $x$ over $K$. Since $m(X)$ divides $f(X)$ in $K[X]$, we may write $f(X) = m(X)h(X)$ where $h(X)$ is a monic polynomial in $K[X]$.

By Theorem 4, the coefficients of $m(X)$ are integral over $A$. Since $A$ is integrally closed, and the coefficients of $m(X)$ belong to $K$ (as $m(X) \in K[X]$), the integral closure property of $A$ implies that $m(X) \in A[X]$.

Similarly, $h(X) \in A[X]$ by the same argument, since $f(X)$ and $m(X)$ have coefficients in $A$, and $h(X) = f(X)/m(X)$ by the division algorithm in $K[X]$. The result follows.
