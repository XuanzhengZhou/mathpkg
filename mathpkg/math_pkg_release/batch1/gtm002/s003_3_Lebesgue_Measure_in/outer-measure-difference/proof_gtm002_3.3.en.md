---
role: proof
locale: en
of_concept: outer-measure-difference
source_book: gtm002
source_chapter: "3"
source_section: "3. Lebesgue Measure in r-Space"
---

By Lemma 3.6, for any $\varepsilon > 0$ there is a closed subset $F_1$ of the open set $G - F$ such that $m^*(F_1) > m^*(G - F) - \varepsilon$. By Lemma 3.4 and Theorem 3.1,

$$
m^*(F) + m^*(G - F) < m^*(F) + m^*(F_1) + \varepsilon = m^*(F \cup F_1) + \varepsilon \leq m^*(G) + \varepsilon.
$$

Hence $m^*(F) + m^*(G - F) \leq m^*(G)$. The opposite inequality $m^*(G) \leq m^*(F) + m^*(G - F)$ follows from countable subadditivity. Therefore $m^*(G - F) = m^*(G) - m^*(F)$.
