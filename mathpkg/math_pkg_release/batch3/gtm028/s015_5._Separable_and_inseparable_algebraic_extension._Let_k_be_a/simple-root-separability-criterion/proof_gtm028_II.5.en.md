---
role: proof
locale: en
of_concept: simple-root-separability-criterion
source_book: gtm028
source_chapter: "II"
source_section: "5. Separable and inseparable algebraic extension"
---

Let $f(X)$ be the minimal polynomial of $x$ over $k$. If $x$ is separable over $k$, then $f'(X) \neq 0$. Since $f(x) = 0$, differentiating the relation $f(X) = (X - x)^s f_1(X)$ in $K[X]$ (where $s$ is the multiplicity of $x$ as a root of $f$) yields $f'(X) = s(X - x)^{s-1}f_1(X) + (X - x)^s f_1'(X)$. If $s > 1$, then $f'(x) = 0$. But $f'(X) \neq 0$ and $f(X)$ is the minimal polynomial of $x$, so $f(X)$ divides $f'(X)$, which is impossible since $\deg f' < \deg f$. Hence $s = 1$ and $x$ is a simple root.

Conversely, if $x$ is a simple root of $f(X)$ in $K[X]$, then $f(X) = (X - x)f_1(X)$ with $f_1(x) \neq 0$. Then $f'(x) = f_1(x) \neq 0$, so $f'(X) \neq 0$ and $f(X)$ is separable, hence $x$ is separable over $k$.

For the second statement: if $g(x) = 0$, then $f(X)$ divides $g(X)$, so $g(X) = A(X)f(X)$ for some $A(X) \in k[X]$. Then $g'(X) = A'(X)f(X) + A(X)f'(X)$, and evaluating at $x$ gives $g'(x) = A(x)f'(x)$. If $x$ is inseparable over $k$, then $f'(X) = 0$, so $f'(x) = 0$ and consequently $g'(x) = 0$.
