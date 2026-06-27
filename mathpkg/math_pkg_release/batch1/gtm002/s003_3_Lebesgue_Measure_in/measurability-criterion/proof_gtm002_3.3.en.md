---
role: proof
locale: en
of_concept: measurability-criterion
source_book: gtm002
source_chapter: "3"
source_section: "3. Lebesgue Measure in r-Space"
---

For any $\varepsilon > 0$, let $F$ be a closed subset of $A$ such that $m^*(F) > m^*(A) - \varepsilon/2$. Since $m^*(A) < \infty$, there exists a covering sequence of open intervals $I_i$ of diameter less than $1$ such that

$$
\sum |I_i| < m^*(A) + \frac{\varepsilon}{2}.
$$

Let $G$ be the union of those intervals $I_i$ that meet $A$. Then $F \subset A \subset G$, $G$ is bounded, and by Lemma 3.7,

$$
m^*(G - F) = m^*(G) - m^*(F) \leq \sum |I_i| - m^*(F) < m^*(A) + \frac{\varepsilon}{2} - m^*(F) < \varepsilon.
$$

Hence $A$ is measurable. Conversely, if $A$ is measurable, the required closed and open sets exist by definition.
