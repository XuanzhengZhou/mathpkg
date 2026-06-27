---
role: proof
locale: en
of_concept: classification-of-finite-fields
source_book: gtm007
source_chapter: "I"
source_section: "1"
---

\textit{(i)} Since $K$ is finite, its prime subfield must be $\mathbf{F}_p$ for some prime $p$ (otherwise $K$ would contain $\mathbb{Q}$, which is infinite). Hence $\operatorname{char}(K) = p \neq 0$, and $K$ is a finite extension of $\mathbf{F}_p$. Let $f = [K : \mathbf{F}_p]$. Then $K$ is an $f$-dimensional vector space over $\mathbf{F}_p$, so $\operatorname{Card}(K) = p^f$.

\textit{(ii)} Let $q = p^f$. Consider the polynomial $F(X) = X^q - X$ in $\Omega[X]$. Its derivative is $F'(X) = q X^{q-1} - 1 = -1$ (since $q = p^f$ is divisible by $p$, hence $q \cdot 1 = 0$ in characteristic $p$), and this is not zero. This implies (since $\Omega$ is algebraically closed) that $X^q - X$ has $q$ distinct roots, hence $\operatorname{Card}(\mathbf{F}_q) = q$, where $\mathbf{F}_q$ denotes the set of roots of $X^q - X$ in $\Omega$.

Conversely, if $K$ is a subfield of $\Omega$ with $q$ elements, the multiplicative group $K^*$ of nonzero elements in $K$ has $q-1$ elements. Then $x^{q-1} = 1$ if $x \in K^*$ and $x^q = x$ if $x \in K$. This proves that $K$ is contained in $\mathbf{F}_q$. Since $\operatorname{Card}(K) = \operatorname{Card}(\mathbf{F}_q)$ we have $K = \mathbf{F}_q$, which completes the proof of (ii).

\textit{(iii)} Assertion (iii) follows from (ii) and from the fact that all fields with $p^f$ elements can be embedded in $\Omega$ since $\Omega$ is algebraically closed.
