---
role: proof
locale: en
of_concept: frobenius-endomorphism
source_book: gtm007
source_chapter: "I"
source_section: "1"
---

We have $\sigma(xy) = \sigma(x)\sigma(y)$. Moreover, the binomial coefficient $\binom{p}{k}$ is congruent to $0 \pmod p$ if $0 < k < p$. From this it follows that

$$\sigma(x+y) = (x+y)^p = \sum_{k=0}^{p} \binom{p}{k} x^{p-k} y^k = x^p + y^p = \sigma(x) + \sigma(y);$$

hence $\sigma$ is a homomorphism. Furthermore, $\sigma$ is clearly injective (since $x^p = 0$ implies $x = 0$ in a field). Thus $\sigma$ is an isomorphism of $K$ onto its image $K^p \subseteq K$, which is a subfield.
