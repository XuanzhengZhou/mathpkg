---
role: proof
locale: en
of_concept: completeness-of-symmetric-difference-metric-space
source_book: gtm002
source_chapter: "10"
source_section: "10"
---

To show that $(\tilde{S}, \varrho)$ is complete, let $\tilde{E}_n$ be any Cauchy sequence in $(\tilde{S}, \varrho)$. Then for each positive integer $i$ there is an index $n_i$ such that

$$\varrho(E_n, E_m) < \frac{1}{2^i}$$

for all $n, m \geq n_i$, and we may assume that $n_i < n_{i+1}$. Putting $F_i = E_{n_i}$ we have $\varrho(F_i, F_j) < 1/2^i$ for all $j > i$. Define

$$H_i = \bigcap_{j=i}^{\infty} F_j \quad \text{and} \quad E = \bigcup_{i=1}^{\infty} H_i.$$

All of these sets belong to $S$. $E$ is the set of points that belong to all but a finite number of the sets $F_1, F_2, \ldots$. It is easy to verify that both $E \triangle H_i$ and $H_i \triangle F_i$, and therefore $E \triangle F_i$, are contained in the set

$$(F_i \triangle F_{i+1}) \cup (F_{i+1} \triangle F_{i+2}) \cup (F_{i+2} \triangle F_{i+3}) \cup \cdots.$$

Consequently,

$$m(E \triangle F_i) \leq \sum_{j=i}^{\infty} m(F_j \triangle F_{j+1}) < \sum_{j=i}^{\infty} \frac{1}{2^j} = \frac{1}{2^{i-1}}.$$

For any $\varepsilon > 0$, choose $i$ such that $1/2^{i-1} < \varepsilon$. Then for all $n \geq n_i$,

$$\varrho(E, E_n) \leq m(E \triangle F_i) + m(F_i \triangle E_n) < \frac{1}{2^{i-1}} + \frac{1}{2^i} < \varepsilon.$$

Hence $E_n \to E$ in $(\tilde{S}, \varrho)$, establishing completeness. $\square$
