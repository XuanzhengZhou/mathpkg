---
role: proof
locale: en
of_concept: irreducible-polynomial-divisor
source_book: gtm077
source_chapter: "IV"
source_section: "17"
---
# Proof of Theorem 49: Irreducible Polynomial with Common Root Divides

Let $f(x)$ be a polynomial irreducible over the number field $k$, and suppose $f(x)$ and $g(x)$ (also a polynomial over $k$) have a common root $x = \alpha$.

By Theorem 48, the greatest common divisor $(f(x), g(x))$ is a polynomial over $k$. Since $\alpha$ is a common root of both $f(x)$ and $g(x)$, the polynomial $x - \alpha$ divides both $f(x)$ and $g(x)$ in some extension field. Consequently, $x - \alpha$ divides their greatest common divisor $(f(x), g(x))$, which implies that $(f(x), g(x))$ is not a constant; in particular, $(f(x), g(x)) \neq 1$.

On the other hand, since $f(x)$ is irreducible over $k$, its only polynomial factors over $k$ are of the form $c f(x)$ where $c \in k$ is a constant. Since $(f(x), g(x))$ divides $f(x)$ and is not a constant, it must be that $(f(x), g(x)) = c f(x)$ for some nonzero constant $c \in k$.

Therefore $f(x) \mid g(x)$, and consequently every root of $f(x)$ is also a root of $g(x)$.

In particular, an irreducible polynomial over $k$ of degree $n$ has exactly $n$ distinct roots. For if it had a multiple root $\alpha$, then $\alpha$ would be a common root of $f(x)$ and its derivative $f'(x)$, which is also a polynomial over $k$ but of degree $n - 1$. By the theorem just proved, $f(x)$ would have to divide $f'(x)$, which is impossible since $\deg f' < \deg f$.
