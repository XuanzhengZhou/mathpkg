---
role: proof
locale: en
of_concept: existence-of-simple-extension-for-irreducible-polynomial
source_book: gtm028
source_chapter: "II"
source_section: "1"
---

It suffices to prove the theorem for monic polynomials $f(X)$. Let $n$ be the degree of $f(X)$, $n \geq 1$. By Theorem 2, if there exists an extension $k(x)$ such that $x$ is a root of $f(X)$, then the elements of $k(x)$ are all expressible in the form $c_0 x^{n-1} + c_1 x^{n-2} + \cdots + c_{n-1}$ with $c_i \in k$. This suggests the following constructive procedure.

Consider the subset $\Delta$ of $k[X]$ consisting of the zero polynomial and of all polynomials in $k[X]$ of degree $\leq n-1$. This subset $\Delta$ is a subgroup of the additive group of $k[X]$. It is, however, not closed under the ordinary multiplication in $k[X]$. We shall make the additive group $\Delta$ into a field by introducing in $\Delta$ a new multiplication, denoted by $\circ$, and we shall show that the field thus obtained is the desired extension.

Let $g(X), h(X) \in \Delta$. To define the new product $g(X) \circ h(X)$, multiply $g(X)$ and $h(X)$ in $k[X]$ and divide the resulting polynomial by $f(X)$, obtaining a remainder $r(X)$ which is either zero or of degree $\leq n-1$:
$$g(X)h(X) = q(X)f(X) + r(X).$$
We set $g(X) \circ h(X) = r(X)$.

\textit{Well-definedness and ring axioms:} The remainder $r(X)$ is uniquely determined by the division algorithm in $k[X]$. The operation $\circ$ is commutative (since ordinary multiplication is) and associative: if $l(X) \in \Delta$, we have
$$g(X)h(X)l(X) = [q(X)f(X) + r(X)]l(X) = q(X)l(X)f(X) + r(X)l(X).$$
Dividing $r(X)l(X)$ by $f(X)$ gives remainder $r'(X)$, which is precisely $r(X) \circ l(X)$. On the other hand, $g(X) \circ (h(X) \circ l(X))$ also yields $r'(X)$. Thus $\circ$ is associative. Distributivity follows similarly.

The identity element $1 \in k[X]$ (a constant polynomial of degree 0) is also the identity of $\Delta$ under $\circ$. Thus $\Delta$ is a commutative ring with identity.

\textit{$\Delta$ is a field:} Let $g(X) \in \Delta$, $g(X) \neq 0$. Since $\partial g < n$ and $f(X)$ is irreducible, $g(X)$ and $f(X)$ are relatively prime. Hence there exist polynomials $h(X), A(X) \in k[X]$ such that
$$h(X)g(X) + A(X)f(X) = 1.$$
We may assume $\partial h \leq n-1$: if not, write $h(X) = B(X)f(X) + h_1(X)$ with $\partial h_1 \leq n-1$; then
$$h_1(X)g(X) + (A(X) + B(X)g(X))f(X) = 1.$$
Hence $h(X) \in \Delta$. For these $g(X)$ and $h(X)$, we have
$$g(X)h(X) = (-A(X))f(X) + 1,$$
so $g(X) \circ h(X) = 1$. Thus every nonzero element of $\Delta$ has a multiplicative inverse, and $\Delta$ is a field.

\textit{Identifying $k$ and the root:} If $g(X), h(X) \in \Delta$ and their ordinary product $g(X)h(X)$ has degree $< n$, then $g(X) \circ h(X) = g(X)h(X)$. In particular, if $c \in k$ and $m < n$, then $c \circ X^m = c X^m$. The element $X \in \Delta$ (which is of degree $1 \leq n-1$) satisfies $f(X) \circ = 0$ in $\Delta$, since $f(X) \equiv 0 \pmod{f(X)}$ yields remainder $0$. Identifying the constant polynomials in $\Delta$ with $k$ and denoting the element $X \in \Delta$ by $x$, the field $\Delta$ is precisely $k(x)$, and $f(x) = 0$.
