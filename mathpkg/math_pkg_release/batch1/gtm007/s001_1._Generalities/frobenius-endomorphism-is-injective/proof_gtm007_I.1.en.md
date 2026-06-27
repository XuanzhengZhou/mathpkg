---
role: proof
locale: en
of_concept: frobenius-endomorphism-is-injective
source_book: gtm007
source_chapter: "I. Finite Fields"
source_section: "1. Generalities"
---

We have $\sigma(xy) = \sigma(x)\sigma(y)$. Moreover, the binomial coefficient $\binom{p}{k}$ is congruent to $0 \pmod{p}$ if $0 < k < p$. From this it follows that

$$\sigma(x+y) = (x+y)^p = \sum_{k=0}^{p} \binom{p}{k} x^k y^{p-k} = x^p + y^p = \sigma(x) + \sigma(y);$$

hence $\sigma$ is a homomorphism. Furthermore, $\sigma$ is clearly injective: if $x^p = 0$, then $x = 0$ since a field has no nonzero nilpotent elements. Thus $\sigma$ is an isomorphism of $K$ onto its image $K^p$, which is a subfield of $K$.
