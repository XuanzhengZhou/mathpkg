---
role: proof
locale: en
of_concept: structure-of-simple-algebraic-extension
source_book: gtm028
source_chapter: "II"
source_section: "1"
---

Since $x$ is algebraic over $k$, let $f(X)$ be the minimal polynomial of $x$, of degree $n$. The proof proceeds in two parts.

\textbf{Part 1: $k(x) = k[x]$.} By definition, $k(x)$ is the quotient field of $k[x]$ inside $K$. Thus $k[x] \subseteq k(x)$. To show the reverse inclusion, it suffices to prove that $k[x]$ is already a field. Since $k[x]$ is a commutative ring with identity, we need only show that every nonzero element has a multiplicative inverse in $k[x]$.

Let $\xi \in k[x]$, $\xi \neq 0$. Then $\xi = g(x)$ for some $g(X) \in k[X]$. Since $\xi \neq 0$, $g(x) \neq 0$, so $f(X)$ does not divide $g(X)$ (otherwise $g(x) = 0$ by $f(x) = 0$). Since $f(X)$ is irreducible, $f(X)$ and $g(X)$ are relatively prime in the principal ideal domain $k[X]$. Hence there exist polynomials $h(X), A(X) \in k[X]$ such that
$$h(X)g(X) + A(X)f(X) = 1.$$
Substituting $x$ for $X$ and using $f(x) = 0$, we obtain $h(x) \cdot g(x) = 1$. Thus $h(x) = \xi^{-1} \in k[x]$, proving that $k[x]$ is a field and hence $k(x) = k[x]$.

\textbf{Part 2: Unique representation.} Let $\xi \in k(x) = k[x]$. Then $\xi = h(x)$ for some $h(X) \in k[X]$. Divide $h(X)$ by $f(X)$ in $k[X]$ (Euclidean algorithm):
$$h(X) = q(X)f(X) + r(X),$$
where $r(X) = 0$ or $\partial r < n$. Substituting $x$ for $X$ and using $f(x) = 0$ yields $\xi = r(x)$. Thus $\xi$ is a linear combination of $1, x, \ldots, x^{n-1}$ with coefficients in $k$.

To prove uniqueness, suppose $c_0 x^{n-1} + \cdots + c_{n-1} = c_0' x^{n-1} + \cdots + c_{n-1}'$ with $c_i, c_i' \in k$. Then the polynomial $p(X) = (c_0 - c_0')X^{n-1} + \cdots + (c_{n-1} - c_{n-1}')$ satisfies $p(x) = 0$ and has degree $< n$. By Theorem 1(b), $f(X)$ must divide $p(X)$. But $\partial f = n > \partial p$ unless $p(X) = 0$. Hence $p(X) = 0$, so $c_i = c_i'$ for all $i$. This proves uniqueness, and shows $[k(x) : k] = n$ with basis $1, x, \ldots, x^{n-1}$.
