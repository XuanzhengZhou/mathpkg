---
role: proof
locale: en
of_concept: leibniz-formula-for-derivations
source_book: gtm023
source_chapter: "5"
source_section: "§1. Basic properties"
---

For $n=1$, the formula coincides with the definition of a derivation. Suppose now by induction that the formula holds for some $n$. Then

$$
\theta^{n+1}(xy) = \theta \theta^n(xy) = \theta\left(\sum_{r=0}^{n} \binom{n}{r} \theta^r x \cdot \theta^{n-r} y\right).
$$

Applying the derivation property to each term and using linearity,

$$
= \sum_{r=0}^{n} \binom{n}{r} \theta^{r+1} x \cdot \theta^{n-r} y + \sum_{r=0}^{n} \binom{n}{r} \theta^r x \cdot \theta^{n-r+1} y.
$$

Reindexing the second sum with $s = r+1$ and combining with the first sum using the binomial identity $\binom{n}{r-1} + \binom{n}{r} = \binom{n+1}{r}$ yields

$$
\theta^{n+1}(xy) = \sum_{r=0}^{n+1} \binom{n+1}{r} \theta^r x \cdot \theta^{n+1-r} y,
$$

completing the induction.
