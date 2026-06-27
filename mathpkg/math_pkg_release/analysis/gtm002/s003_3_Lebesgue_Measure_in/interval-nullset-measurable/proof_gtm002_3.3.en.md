---
role: proof
locale: en
of_concept: interval-nullset-measurable
source_book: gtm002
source_chapter: "3"
source_section: "3. Lebesgue Measure in r-Space"
---

The first statement follows at once from Lemma 3.11 and Theorem 3.3: for an interval $I$, $m^*(I) = |I| < \infty$, and one can take $F = \bar{I}$ (a closed interval with the same volume) and $G$ an open interval slightly larger than $I$, making $m^*(G - F)$ arbitrarily small.

If $m^*(A) = 0$, then for each $\varepsilon > 0$ there is a covering sequence of open intervals $I_i$ such that $\sum |I_i| < \varepsilon$. Take $G = \bigcup I_i$ and $F = \emptyset$. Then $F$ is closed, $G$ is open, $F \subset A \subset G$, and $m^*(G - F) \leq \sum |I_i| < \varepsilon$. Hence $A$ is measurable.
