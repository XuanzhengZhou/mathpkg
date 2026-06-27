---
role: proof
locale: en
of_concept: "structure-of-finite-fields"
source_book: gtm007
source_chapter: "I"
source_section: "1.1"
---
The derivative of $X^q - X$ is $qX^{q-1} - 1 = -1$ in characteristic $p$, so $X^q - X$ has $q$ distinct roots in $\Omega$, thus $\operatorname{Card}(\mathbb{F}_q) = q$. Conversely, if $K$ is a subfield of $\Omega$ with $q$ elements, the multiplicative group $K^*$ has $q-1$ elements. Then $x^{q-1} = 1$ for $x \in K^*$ and $x^q = x$ for all $x \in K$. This proves $K \subseteq \mathbb{F}_q$. Since $\operatorname{Card}(K) = \operatorname{Card}(\mathbb{F}_q)$, we have $K = \mathbb{F}_q$. Assertion (iii) follows from (ii) since all fields with $p^f$ elements embed into $\Omega$.
