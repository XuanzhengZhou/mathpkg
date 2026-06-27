---
role: proof
locale: en
of_concept: minimality-criterion-sufficient-sigma-fields
source_book: gtm046
source_chapter: "VIII"
source_section: "27.4"
---

**Proof.** According to Chapter II, Complements and Details 23, there exists a probability measure $\mu_0$ (or equivalently a random variable $Z_0$) such that

$$\mu_0 A = 0 \iff \text{every } \mu_t A = 0,$$

or, equivalently, up to $P$-null subsets,

$$Z_0 = 0 \text{ on } A \iff \text{every } Z_t = 0 \text{ on } A.$$

Condition (i') guarantees that $Z_0$ vanishes on exactly those sets where all $Z_t$ vanish. Therefore, for any sub-$\sigma$-field $\mathfrak{B}$, the conditional expectation $E_{Z_0}^\mathfrak{B}X$ belongs to all the equivalence classes $E_{Z_t}^\mathfrak{B}X$.

Consequently, if a sub-$\sigma$-field $\mathfrak{B}$ is sufficient with respect to some $Z$, it is also sufficient with respect to $Z_0$. Hence the least fine sufficient $\sigma$-field computed with $Z_0$ is the minimal sufficient $\sigma$-field for the whole family $\{Z_t\}$.

The corresponding factorization takes the form $Z_t = g_t Z_0$ a.s., where $Z_0 = 0$ a.s. implies every $Z_t = 0$ a.s. (but the converse need not hold in general—this is precisely what distinguishes $Z_0$ from other dominating measures). The minimality criterion is thus established.
