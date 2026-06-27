---
role: proof
locale: en
of_concept: interval-countable-subadditivity
source_book: gtm018
source_chapter: "II"
source_section: "8"
---

Write $E_i = [a_i, b_i)$, $i = 0, 1, 2, \cdots$. For a fixed $\epsilon > 0$ choose a positive number $\delta$ and write $F_0 = [a_0, b_0 - \epsilon]$, and for each $i = 1, 2, \cdots$ choose an open interval $U_i = (a_i, b_i + \delta/2^i)$. Then $F_0$ is contained in the union of the open intervals $\{U_i\}$. Since $F_0$ is compact, there exists a positive integer $n$ such that $F_0 \subset \bigcup_{i=1}^{n} U_i$. From Theorem B we obtain

$$\mu(E_0) - \epsilon = (b_0 - a_0) - \epsilon < \sum_{i=1}^{n} \left(b_i - a_i + \frac{\delta}{2^i}\right) \leq \sum_{i=1}^{\infty} \mu(E_i) + \delta.$$

Since $\epsilon$ and $\delta$ are arbitrary, the conclusion of the theorem follows.
