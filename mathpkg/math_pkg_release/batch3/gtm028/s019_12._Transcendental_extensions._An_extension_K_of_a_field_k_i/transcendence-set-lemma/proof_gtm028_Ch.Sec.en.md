---
role: proof
locale: en
of_concept: transcendence-set-lemma
source_book: gtm028
source_chapter: "II. Elements of Field Theory"
source_section: "§12. Transcendental Extensions"
---

Suppose that $x$ is transcendental over $k(L)$ and let $x_1, x_2, \dots, x_n$ be any elements of $L'$. If all the $x_i$ are already in $L$, they are algebraically independent over $k$. Assume that $x_n = x$ and let $f(X_1, X_2, \dots, X_n)$ be a polynomial, with coefficients in $k$, such that $f(x_1, x_2, \dots, x_n) = 0$. Then $x$ is a root of the polynomial $f(x_1, x_2, \dots, x_{n-1}, X)$ in $k(x_1, x_2, \dots, x_{n-1})[X]$. This polynomial must be zero since $x$ is transcendental over $k(L)$. Hence, if
$$f(X_1, X_2, \dots, X_n) = A_0(X_1, X_2, \dots, X_{n-1})X_n^g + \cdots + A_g(X_1, X_2, \dots, X_{n-1}),$$
then we must have $A_i(x_1, x_2, \dots, x_{n-1}) = 0$, $i = 0, 1, \dots, g$. Since $x_1, x_2, \dots, x_{n-1}$ are algebraically independent over $k$, the polynomials $A_i(X_1, X_2, \dots, X_{n-1})$ must be zero. This implies that also $f(X_1, X_2, \dots, X_n)$ is the zero polynomial.

Conversely, assume that $L'$ is a transcendence set. Let $F(X)$ be a nonzero polynomial in $k(L)[X]$ such that $F(x) = 0$. Clearing denominators, we obtain a polynomial relation among $x$ and finitely many elements of $L$ with coefficients in $k$, contradicting that $L'$ is a transcendence set. Hence $x$ is transcendental over $k(L)$.
