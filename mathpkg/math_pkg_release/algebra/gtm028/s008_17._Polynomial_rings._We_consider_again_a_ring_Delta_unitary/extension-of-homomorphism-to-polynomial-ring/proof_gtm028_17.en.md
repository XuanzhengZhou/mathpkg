---
role: proof
locale: en
of_concept: extension-of-homomorphism-to-polynomial-ring
source_book: gtm028
source_chapter: "I"
source_section: "17"
---

**Proof.** We observe that if $T$ exists at all, then we have

$$\left( \sum a_i x^i \right) T = \sum \left( a_i T \right) \left( x T \right)^i = \sum \left( a_i T_0 \right) y^i, \quad a_i \in R,$$

so that $T$ is uniquely determined. We make use of this formula to define $T$. Since $x$ is transcendental over $R$, every element of $S'$ can be uniquely expressed in the form $\sum a_i x^i$ with $a_i \in R$; thus $T$ is single-valued. It is surely a mapping of $S'$ onto $\bar{R}[y]$, since $T_0$ is a mapping onto $\bar{R}$. Obviously $aT = aT_0$ for $a \in R$, and $xT = y$. That $T$ is a homomorphism follows from (5) and (6) of §16, applied to elements of $R[x]$ and $\bar{R}[y]$.

Suppose $T_0$ is an isomorphism and $y$ is transcendental over $\bar{R}$. If $(\sum a_i x^i) T = 0$, then $\sum \left( a_i T_0 \right) y^i = 0$. Since $y$ is transcendental over $\bar{R}$, each $a_i T_0$ is $0$; since $T_0$ is an isomorphism, $a_i = 0$. Thus $T$ is an isomorphism. The converse is similarly proved.
