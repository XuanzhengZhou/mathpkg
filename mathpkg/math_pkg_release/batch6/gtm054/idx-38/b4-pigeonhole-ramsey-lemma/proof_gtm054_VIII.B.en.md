---
role: proof
locale: en
of_concept: b4-pigeonhole-ramsey-lemma
source_book: gtm054
source_chapter: "VIII"
source_section: "B"
---

For $s=1$, $H$ consists of functions $h: V \to \{1, \ldots, m\}$ (since $\mathcal{P}_1(V)$ can be identified with $V$). The condition $\mathcal{P}_1(S) \subseteq h^{-1}[i]$ for $|S| = q_i$ means there are at least $q_i$ elements all mapped to color $i$. 

Now $|V| < n(q_1, \ldots, q_m : 1)$ if and only if for all such colorings $h$, we have $|h^{-1}[i]| \leq q_i - 1$ for each $i = 1, \ldots, m$. This is equivalent to $|V| \leq \sum_{i=1}^{m} (q_i - 1) = (\sum_{i=1}^{m} q_i) - m$. Therefore the Ramsey number is $(\sum_{i=1}^{m} q_i) - m + 1$.
