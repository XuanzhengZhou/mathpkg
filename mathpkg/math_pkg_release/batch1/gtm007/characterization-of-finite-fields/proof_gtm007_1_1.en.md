---
role: proof
locale: en
of_concept: characterization-of-finite-fields
source_book: gtm007
source_chapter: "I"
source_section: "1"
---

(i) Since $K$ is finite, the homomorphism $\mathbb{Z} \to K$ given by $n \mapsto n \cdot 1$ cannot be injective, so its kernel is $p\mathbb{Z}$ for some prime $p$. Thus $\operatorname{char}(K) = p$ and $K$ contains $\mathbb{F}_p$. Viewing $K$ as a vector space over $\mathbb{F}_p$, if $f = \dim_{\mathbb{F}_p} K$, then $|K| = p^f$.

(ii) Consider the polynomial $F(X) = X^q - X$ over $\Omega$. Its derivative is $F'(X) = qX^{q-1} - 1 = -1$ (since $q$ is a multiple of $p$, hence $q = 0$ in $\Omega$). Thus $F'(X) = -1 \neq 0$, so $F$ has $q$ distinct roots in $\Omega$. Let $\mathbb{F}_q = \{x \in \Omega : x^q = x\}$. For $x, y \in \mathbb{F}_q$, we have $(x+y)^q = x^q + y^q = x + y$ (Frobenius), $(xy)^q = x^q y^q = xy$, and if $x \neq 0$, $(x^{-1})^q = (x^q)^{-1} = x^{-1}$. Thus $\mathbb{F}_q$ is a subfield of $\Omega$ with $q$ elements.

Conversely, if $K$ is a subfield of $\Omega$ with $q$ elements, then $K^*$ is a group of order $q-1$, so $x^{q-1} = 1$ for all $x \in K^*$, i.e., $x^q = x$ for all $x \in K$. Hence $K \subseteq \mathbb{F}_q$. Comparing cardinalities, $K = \mathbb{F}_q$.

(iii) Any field with $p^f$ elements can be embedded in the algebraic closure $\Omega$ of $\mathbb{F}_p$; by (ii), its image must be $\mathbb{F}_q$, hence it is isomorphic to $\mathbb{F}_q$.
