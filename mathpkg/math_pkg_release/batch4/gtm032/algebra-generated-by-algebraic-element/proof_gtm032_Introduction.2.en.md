---
role: proof
locale: en
of_concept: algebra-generated-by-algebraic-element
source_book: gtm032
source_chapter: "Introduction"
source_section: "2"
---

Let $n = \deg f(x)$. We claim $\{1, t, t^2, \ldots, t^{n-1}\}$ is a basis for $\mathfrak{A}/\Phi$. Let $a \in \mathfrak{A} = \Phi[t]$. Then $a = g(t)$ for some $g(x) \in \Phi[x]$. By the division algorithm in $\Phi[x]$, write $g(x) = f(x)q(x) + r(x)$ where $\deg r(x) < \deg f(x) = n$. Applying the homomorphism sending $x \mapsto t$ yields $a = g(t) = f(t)q(t) + r(t) = 0 \cdot q(t) + r(t) = r(t)$, since $f(t) = 0$. Thus $a$ is a linear combination of $1, t, \ldots, t^{n-1}$.

For linear independence, if $\sum_{i=0}^{n-1} \alpha_i t^i = 0$ with not all $\alpha_i = 0$, then $h(x) = \sum \alpha_i x^i$ is a non-zero polynomial of degree $< n$ with $h(t) = 0$, contradicting the minimality of $\deg f(x) = n$. Hence $[\mathfrak{A}:\Phi] = n = \deg f(x)$.
