---
role: proof
locale: en
of_concept: closed-approximation-open-set
source_book: gtm002
source_chapter: "3"
source_section: "3. Lebesgue Measure in r-Space"
---

The bounded open set $G$ can be represented as the union of a sequence of non-overlapping intervals $I_i$. By definition, $m^*(G) \leq \sum |I_i|$. Determine $n$ so that

$$
\sum_{i=1}^n |I_i| > m^*(G) - \frac{\varepsilon}{2},
$$

and let $J_i$ be a closed interval contained in the interior of $I_i$ such that

$$
|J_i| > |I_i| - \frac{\varepsilon}{2n} \quad (i = 1, 2, \ldots, n).
$$

Then $F = \bigcup_{i=1}^n J_i$ is a closed subset of $G$, and by Theorem 3.3 and Lemma 3.5,

$$
m^*(F) = \sum_{i=1}^n |J_i| > \sum_{i=1}^n |I_i| - \frac{\varepsilon}{2} > m^*(G) - \varepsilon.
$$
