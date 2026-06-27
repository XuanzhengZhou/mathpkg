---
role: proof
locale: en
of_concept: borel-cantelli-lemma
source_book: gtm017
source_chapter: "IX"
source_section: "a"
---
If $\sum P(A_i) < \infty$: $P(A_i \text{ i.o.}) \leq P(\bigcup_{i=n}^\infty A_i) \leq \sum_{i=n}^\infty P(A_i) \to 0$ as $n \to \infty$.

If $\sum P(A_i) = \infty$: By independence,
$$P(\bigcap_{i=n}^\infty \bar{A}_i) = \prod_{i=n}^\infty (1 - P(A_i)) \leq \exp(-\sum_{i=n}^\infty P(A_i)) = 0.$$
Thus $P(A_i \text{ f.o.}) = P(\bigcup_{n=1}^\infty \bigcap_{i=n}^\infty \bar{A}_i) = 0$, so $P(A_i \text{ i.o.}) = 1$.
