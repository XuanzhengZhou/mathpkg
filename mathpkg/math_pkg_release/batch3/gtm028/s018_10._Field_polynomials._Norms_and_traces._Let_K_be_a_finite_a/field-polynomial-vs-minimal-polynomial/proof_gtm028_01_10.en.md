---
role: proof
locale: en
of_concept: field-polynomial-vs-minimal-polynomial
source_book: gtm028
source_chapter: "I"
source_section: "10"
---
Let $g(X)$ be of degree $s$, and let $g_1(X)$ be the field polynomial of $x$ when $x$ is regarded as an element of $k(x)$. Since $[k(x):k] = s$, it follows that $g_1(X)$ is also of degree $s$. Since $x$ is a root of $g_1(X)$ and $g(X)$ is the minimal polynomial of $x$ in $k[X]$, it follows (by §2, Theorem 1) that $g(X) = g_1(X)$, both $g$ and $g_1$ being monic polynomials. We have thus shown that if $x$ is regarded as an element of $k(x)$, then the minimal polynomial of $x$ in $k[X]$ coincides with the field polynomial of $x$ over $k$.

Now apply formula (10) (the tower formula for field polynomials) by replacing $K$ by $k(x)$ and $\Delta$ by $K$. This yields $f(X) = [g_1(X)]^{[K:k(x)]} = [g(X)]^{\nu}$ where $\nu = [K:k(x)]$, proving that $f(X)$ is a power of $g(X)$.

If $K = k(x)$, then $\nu = 1$ and $f(X) = g(X)$. Conversely, if $f(X) = g(X)$, then comparing degrees gives $n = s$, so $[K:k] = [k(x):k]$, which forces $K = k(x)$. Hence $x$ is a primitive element.
