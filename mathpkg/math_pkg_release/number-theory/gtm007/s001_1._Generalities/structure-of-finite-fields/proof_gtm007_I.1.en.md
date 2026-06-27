---
role: proof
locale: en
of_concept: structure-of-finite-fields
source_book: gtm007
source_chapter: "I. Finite Fields"
source_section: "1. Generalities"
---

**i)** If $K$ is a finite field, its characteristic must be a prime $p \neq 0$ (characteristic zero would give an infinite subfield isomorphic to $\mathbb{Q}$). The subfield $\mathbb{F}_p \subseteq K$ is the prime field, so $K$ is a finite extension of $\mathbb{F}_p$. Let $f = [K:\mathbb{F}_p]$; then $|K| = p^f = q$.

**ii)** Let $\Omega$ be an algebraically closed field of characteristic $p$, and let $q = p^f$ with $f \geq 1$. Consider the polynomial $X^q - X \in \Omega[X]$. Its derivative is $q X^{q-1} - 1 = -1$ (since $q = p^f$ is divisible by $p$, hence $q \cdot 1_\Omega = 0$), which is never zero. Therefore $X^q - X$ has no multiple roots in $\Omega$, so it has exactly $q$ distinct roots. Let $\mathbf{F}_q$ be the set of these roots. For $x, y \in \mathbf{F}_q$, we have $(x+y)^q = x^q + y^q = x + y$ (by the Frobenius endomorphism property in characteristic $p$) and $(xy)^q = x^q y^q = xy$, so $\mathbf{F}_q$ is a subfield of $\Omega$ with $q$ elements. This proves existence.

For uniqueness: if $K \subseteq \Omega$ is any subfield with $q$ elements, then $K^* = K \setminus \{0\}$ has order $q-1$. Every $x \in K^*$ satisfies $x^{q-1} = 1$, hence $x^q = x$ for all $x \in K$. Thus $K \subseteq \mathbf{F}_q$. Since $|K| = |\mathbf{F}_q| = q$, we have $K = \mathbf{F}_q$.

**iii)** Any field with $q = p^f$ elements can be embedded into $\Omega$ (since $\Omega$ is algebraically closed), and its image must coincide with $\mathbf{F}_q$ by the uniqueness proved in (ii). Hence all such fields are isomorphic to $\mathbf{F}_q$.
