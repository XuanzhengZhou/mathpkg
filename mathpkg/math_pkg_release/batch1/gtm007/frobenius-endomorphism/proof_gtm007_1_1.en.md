---
role: proof
locale: en
of_concept: frobenius-endomorphism
source_book: gtm007
source_chapter: "I"
source_section: "1"
---

We have $\sigma(xy) = (xy)^p = x^p y^p = \sigma(x)\sigma(y)$. For addition, by the binomial theorem,
\[
\sigma(x+y) = (x+y)^p = \sum_{k=0}^{p} \binom{p}{k} x^{p-k} y^k.
\]
For $0 < k < p$, the binomial coefficient $\binom{p}{k} = \frac{p(p-1)\cdots(p-k+1)}{k!}$ is divisible by $p$ since the numerator contains $p$ and the denominator does not. Thus $\binom{p}{k} \equiv 0 \pmod{p}$, and in characteristic $p$, all intermediate terms vanish, giving
\[
\sigma(x+y) = x^p + y^p = \sigma(x) + \sigma(y).
\]
Hence $\sigma$ is a homomorphism. If $\sigma(x) = x^p = 0$, then $x = 0$, so $\sigma$ is injective. Therefore $\sigma$ is an isomorphism onto $K^p$.
