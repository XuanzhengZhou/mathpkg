---
role: proof
locale: en
of_concept: classification-of-finite-fields
source_book: gtm007
source_chapter: "I"
source_section: "1.1"
---

If $K$ is finite, its characteristic $p$ is a prime number. $K$ is then a finite-dimensional vector space over $F_p$, of dimension $f = [K:F_p]$, hence $\mathrm{Card}(K) = p^f$.

Now let $\Omega$ be algebraically closed of characteristic $p$ and let $q = p^f$. The derivative of $X^q - X$ is $qX^{q-1} - 1 = -1$ since $\mathrm{char}(\Omega) = p$. This derivative is never zero. Hence $X^q - X$ has $q$ distinct roots in $\Omega$. Let $F_q$ be the set of these roots. If $x, y \in F_q$, then $(x+y)^q = x^q + y^q = x+y$ and $(xy)^q = x^q y^q = xy$, so $F_q$ is a subfield of $\Omega$ with $q$ elements.

Conversely, if $K$ is a subfield of $\Omega$ with $q$ elements, the multiplicative group $K^*$ has $q-1$ elements. Then $x^{q-1} = 1$ for $x \in K^*$ and $x^q = x$ for all $x \in K$. Thus $K \subset F_q$. Since $\mathrm{Card}(K) = \mathrm{Card}(F_q)$, we have $K = F_q$.

Assertion iii) follows from ii) and from the fact that all fields with $p^f$ elements can be embedded in $\Omega$ since $\Omega$ is algebraically closed.
