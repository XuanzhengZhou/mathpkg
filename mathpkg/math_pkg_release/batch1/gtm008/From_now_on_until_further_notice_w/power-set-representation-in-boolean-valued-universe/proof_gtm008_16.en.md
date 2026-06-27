---
role: proof
locale: en
of_concept: power-set-representation-in-boolean-valued-universe
source_book: gtm008
source_chapter: "16"
source_section: "The Maximum Principle"
---

Let $b = \sum_{v' \in A} \llbracket v = v' \rrbracket$. From Theorem 16.24, for any $v$ with $\llbracket v \subseteq u \rrbracket = b_0$, there exists $v' \in A$ such that $b_0 \leq \llbracket v = v' \rrbracket$. Taking the supremum over all such $b_0$ gives
$$\llbracket v \subseteq u \rrbracket \leq b.$$

Conversely,
$$b \leq \sum_{v' \in A} \llbracket v' \subseteq u \rrbracket \cdot \llbracket v' = v \rrbracket \leq \llbracket v \subseteq u \rrbracket,$$
since each $v' \in A$ satisfies $\llbracket v' \subseteq u \rrbracket = 1$, and $\llbracket v' = v \rrbracket \cdot \llbracket v' \subseteq u \rrbracket \leq \llbracket v \subseteq u \rrbracket$.

Thus $b = \llbracket v \subseteq u \rrbracket$.
