---
role: proof
locale: en
of_concept: k-isomorphism-of-simple-extensions-same-minimal-polynomial
source_book: gtm028
source_chapter: "II"
source_section: "1"
---

Assume that $x$ and $x'$ are roots of one and the same irreducible polynomial $f(X)$ in $k[X]$. Let $n = \partial f$. By Theorem 2, every element of $k(x)$ has a unique expression of the form $c_0 x^{n-1} + c_1 x^{n-2} + \cdots + c_{n-1}$ with $c_i \in k$. Similarly, every element of $k(x')$ has a unique expression $c_0 x'^{n-1} + c_1 x'^{n-2} + \cdots + c_{n-1}$.

Define a mapping $\sigma : k(x) \to k(x')$ by
$$\sigma(c_0 x^{n-1} + c_1 x^{n-2} + \cdots + c_{n-1}) = c_0 x'^{n-1} + c_1 x'^{n-2} + \cdots + c_{n-1}.$$
This is well-defined because of the uniqueness of the representation in both fields, and it is clearly a $(1,1)$ mapping (bijection).

It is clear that $\sigma$ transforms each element of $k$ into itself and that $x\sigma = x'$. So it remains to show that $\sigma$ is an isomorphism, i.e., it preserves both addition and multiplication.

\textit{Addition:} For any $\xi, \eta \in k(x)$, it is obvious that $(\xi + \eta)\sigma = \xi\sigma + \eta\sigma$, since addition is performed coefficient-wise and $\sigma$ acts coefficient-wise.

\textit{Multiplication:} Let $\xi = r(x)$, $\eta = s(x)$, and $\xi\eta = t(x)$, where $r(X), s(X), t(X)$ are polynomials in $k[X]$ of degrees $\leq n-1$. We have then $\xi\sigma = r(x')$, $\eta\sigma = s(x')$, and $(\xi\eta)\sigma = t(x')$.

Since $x$ is a root of $r(X)s(X) - t(X)$, we must have $r(X)s(X) - t(X) = A(X)f(X)$, where $A(X) \in k[X]$ (by Theorem 1). Since also $f(x') = 0$, substituting $x'$ for $X$ gives $r(x')s(x') = t(x')$. Hence $(\xi\sigma)(\eta\sigma) = (\xi\eta)\sigma$. This completes the proof of the direct part.

\textit{Converse:} If a $k$-isomorphism carries $x$ to $x'$, then $f(x') = f(x)\sigma = 0\sigma = 0$, so $x'$ is a root of $f(X)$ as well.
