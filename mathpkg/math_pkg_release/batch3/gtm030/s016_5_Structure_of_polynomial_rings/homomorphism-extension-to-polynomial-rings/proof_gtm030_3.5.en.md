---
role: proof
locale: en
of_concept: homomorphism-extension-to-polynomial-rings
source_book: gtm030
source_chapter: "3"
source_section: "5"
---

Since $x$ is transcendental, an element of $\mathfrak{A}_1[x]$ can be written in one and only one way in the form

$$a_0 + a_1x + \cdots + a_nx^n, \quad a_i \text{ in } \mathfrak{A}_1.$$

Denote this element as $f(x)$ and define

$$f^\sigma(u) = a_0^\sigma + a_1^\sigma u + \cdots + a_n^\sigma u^n, \quad a_i^\sigma \text{ in } \mathfrak{A}_2.$$

The rule $f(x) \to f^\sigma(u)$ defines a single-valued mapping of $\mathfrak{A}_1[x]$ onto $\mathfrak{A}_2[u]$. If $g(x) = \sum b_i x^i$, then $f(x) + g(x) = \sum (a_i + b_i) x^i$ maps to

$$\sum (a_i + b_i)^\sigma u^i = \sum (a_i^\sigma + b_i^\sigma) u^i = \sum a_i^\sigma u^i + \sum b_i^\sigma u^i,$$

so the mapping preserves addition. Similarly, for multiplication one verifies that $(f(x)g(x))^\sigma = f^\sigma(u) g^\sigma(u)$ using the definition of polynomial multiplication and the fact that $\sigma$ is a homomorphism. Hence the mapping is a homomorphism, which we denote by $\Sigma$. Since $x^\sigma = u$ by definition, $\Sigma$ sends $x$ to $u$.

For uniqueness, suppose there is another homomorphism $\Sigma'$ extending $\sigma$ and sending $x$ to $u$. Then for any $f(x) = \sum a_i x^i$, we have $\Sigma'(f(x)) = \sum \Sigma'(a_i) \Sigma'(x)^i = \sum a_i^\sigma u^i = f^\sigma(u) = \Sigma(f(x))$. Hence $\Sigma' = \Sigma$, proving uniqueness.
