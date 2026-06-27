---
role: proof
locale: en
of_concept: countable-additivity-measurable
source_book: gtm002
source_chapter: "3"
source_section: "3. Lebesgue Measure in r-Space"
---

For any $\varepsilon > 0$, since each $A_i$ is measurable, there exist closed sets $F_i \subset A_i$ such that

$$
m^*(F_i) > m^*(A_i) - \frac{\varepsilon}{2^{i+1}}.
$$

Since the $A_i$ are disjoint and all contained in the interval $I$, the $F_i$ are disjoint bounded closed sets. By Lemma 3.5 (finite additivity for disjoint bounded closed sets),

$$
m^*\left(\bigcup_{i=1}^n F_i\right) = \sum_{i=1}^n m^*(F_i) > \sum_{i=1}^n m^*(A_i) - \frac{\varepsilon}{2}.
$$

Since $\bigcup_{i=1}^n F_i \subset A$, we have $m^*(A) \geq m^*(\bigcup_{i=1}^n F_i)$. Letting $n \to \infty$,

$$
m^*(A) \geq \sum_{i=1}^{\infty} m^*(A_i) - \frac{\varepsilon}{2}.
$$

Since $\varepsilon > 0$ is arbitrary, $m^*(A) \geq \sum_{i=1}^{\infty} m^*(A_i)$. The reverse inequality $m^*(A) \leq \sum m^*(A_i)$ follows from countable subadditivity (Theorem 3.2). Hence

$$
m^*(A) = \sum_{i=1}^{\infty} m^*(A_i).
$$

To show $A$ is measurable, note that $A \subset I$ and $I$ is bounded. For each $n$, the finite union $\bigcup_{i=1}^n A_i$ is measurable (as a finite union of measurable sets), hence there exist closed $F^{(n)} \subset \bigcup_{i=1}^n A_i$ and open $G^{(n)} \supset \bigcup_{i=1}^n A_i$ with $m^*(G^{(n)} - F^{(n)}) < \varepsilon/2^n$. Since $A$ is the countable union and the tails have arbitrarily small total measure (by the equality just proved), the standard approximation argument shows $A$ satisfies the measurability criterion of Lemma 3.11.
