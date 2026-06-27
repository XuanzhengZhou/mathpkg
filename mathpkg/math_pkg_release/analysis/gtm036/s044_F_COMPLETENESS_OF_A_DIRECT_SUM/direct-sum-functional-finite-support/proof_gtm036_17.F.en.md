---
role: proof
locale: en
of_concept: direct-sum-functional-finite-support
source_book: gtm036
source_chapter: "17"
source_section: "F"
---

Suppose the conclusion is false. Then there exist infinitely many distinct indices $t_n \in A$ and elements $f_{t_n} \in E_{t_n}^*$ such that $(\phi \circ I_{t_n})(f_{t_n}) = C_n \neq 0$ for $n = 1, 2, \dots$.

Consider the set $S = \{n I_{t_n}(f_{t_n}) / C_n : n = 1, 2, \dots\}$. Each element $n I_{t_n}(f_{t_n}) / C_n$ lies in the factor $E_{t_n}^*$ of the product $\bigwedge \{E_t^* : t \in A\}$. Since the coordinates are supported on distinct indices, the set $S$ is bounded in the product topology and therefore equicontinuous in $E^*$.

Now $\phi$ evaluated on the $n$-th element of $S$ gives:
$$\phi(n I_{t_n}(f_{t_n}) / C_n) = n (\phi \circ I_{t_n})(f_{t_n}) / C_n = n.$$

Thus $\phi$ is unbounded on the equicontinuous set $S$, contradicting the hypothesis that $\phi$ is weak* continuous on every equicontinuous set. Hence the finite subset $B$ must exist.
