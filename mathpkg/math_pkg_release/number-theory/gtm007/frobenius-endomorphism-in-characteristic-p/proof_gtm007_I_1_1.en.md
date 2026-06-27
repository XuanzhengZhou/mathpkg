---
role: proof
locale: en
of_concept: "frobenius-endomorphism-in-characteristic-p"
source_book: gtm007
source_chapter: "I"
source_section: "1.1"
---
We have $\sigma(xy) = (xy)^p = x^p y^p = \sigma(x)\sigma(y)$. Moreover, the binomial coefficient $\binom{p}{k}$ is congruent to $0 \pmod{p}$ if $0 < k < p$. From this it follows that
$$\sigma(x+y) = (x+y)^p = x^p + \sum_{k=1}^{p-1} \binom{p}{k} x^k y^{p-k} + y^p = x^p + y^p = \sigma(x) + \sigma(y).$$
Hence $\sigma$ is a homomorphism. Furthermore, $\sigma$ is clearly injective since $x^p = 0$ implies $x = 0$.
