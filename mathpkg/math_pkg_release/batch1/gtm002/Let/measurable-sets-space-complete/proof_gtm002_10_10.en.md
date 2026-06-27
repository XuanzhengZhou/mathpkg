---
role: proof
locale: en
of_concept: measurable-sets-space-complete
source_book: gtm002
source_chapter: "10"
source_section: "10"
---

Let $\tilde{E}_n$ be any Cauchy sequence in $(\tilde{S}, \varrho)$. Then for each positive integer $i$ there is an index $n_i$ such that $\varrho(E_n, E_m) < 1/2^i$ for all $n, m \geq n_i$, and we may assume that $n_i < n_{i+1}$. Putting $F_i = E_{n_i}$ we have $\varrho(F_i, F_j) < 1/2^i$ for all $j > i$. Define

$$H_i = \bigcap_{j=i}^{\infty} F_j \quad \text{and} \quad E = \bigcup_{i=1}^{\infty} H_i.$$

All of these sets belong to $S$. $E$ is the set of points that belong to all but a finite number of the sets $F_1, F_2, \ldots$. It is easy to verify that both $E \triangle H_i$ and $H_i \triangle F_i$, and therefore $E \triangle F_i$, are contained in the set

$$(F_i \triangle F_{i+1}) \cup (F_{i+1} \triangle F_{i+2}) \cup (F_{i+2} \triangle F_{i+3}) \cup \cdots.$$

Consequently,

$$m(E \triangle F_i) \leq \sum_{j=i}^{\infty} m(F_j \triangle F_{j+1}) < \sum_{j=i}^{\infty} 1/2^j = 1/2^{i-1}.$$

Hence $\varrho(E, F_i) \to 0$ as $i \to \infty$, showing that the Cauchy sequence converges to $E$.
