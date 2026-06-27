---
role: proof
locale: en
of_concept: inner-approximation-measurability
source_book: gtm002
source_chapter: "3"
source_section: "3. Lebesgue Measure in r-Space"
---

**(i) $\Rightarrow$ (ii).** Suppose $A$ is measurable. The inequality $\sup \{ m(F) : F \subset A,\ F \text{ bounded closed} \} \leq m^*(A)$ is obvious since each $F$ is a subset of $A$.

For the reverse inequality, let $\alpha$ be any real number with $\alpha < m(A)$. Define $A_i = A \cap (-i, i)^r$ for $i = 1, 2, \ldots$. By Theorem 3.17 (continuity of measure), $m(A) = \lim_{i \to \infty} m(A_i)$. Hence we can choose $i$ sufficiently large so that $m(A_i) > \alpha$.

Since $A_i$ is measurable and bounded, there exists a closed set $F \subset A_i$ with $m(F) > \alpha$ (by the definition of measurability, Lemma 3.11, or by Lemma 3.7). Then $F$ is a bounded closed subset of $A$ with $m(F) > \alpha$. Since $\alpha < m(A)$ was arbitrary, we obtain

$$
m^*(A) \leq \sup \{ m(F) : A \supset F,\ F \text{ bounded and closed} \}.
$$

**(ii) $\Rightarrow$ (i).** Suppose $m^*(A) < \infty$ and $m^*(A) = \sup \{ m(F) : A \supset F,\ F \text{ bounded and closed} \}$. Given $\varepsilon > 0$, choose a bounded closed set $F \subset A$ such that

$$
m(F) > m^*(A) - \frac{\varepsilon}{2}.
$$

Since $m^*(A) < \infty$, there exists an open set $G \supset A$ such that

$$
m(G) < m^*(A) + \frac{\varepsilon}{2}.
$$

Then $F \subset A \subset G$ and

$$
m(G - F) = m(G) - m(F) < \left(m^*(A) + \frac{\varepsilon}{2}\right) - \left(m^*(A) - \frac{\varepsilon}{2}\right) = \varepsilon.
$$

By Lemma 3.11 (the measurability criterion), $A$ is measurable.
