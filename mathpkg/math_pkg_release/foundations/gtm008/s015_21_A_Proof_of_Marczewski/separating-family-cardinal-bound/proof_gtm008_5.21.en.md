---
role: proof
locale: en
of_concept: separating-family-cardinal-bound
source_book: gtm008
source_chapter: "5"
source_section: "21. A Proof of Marczewski's Theorem"
---

Let $A^{(n)} = \{A_t \mid t \in T \;\wedge\; \bar{A}_t = n\}$ for $n \in \omega$. For each $n$, the subfamily $\{A_t \mid t \in T, \bar{A}_t = n\}$ (together with the corresponding $\{B_t\}$) satisfies the hypotheses of Theorem 21.3 with $\alpha = n$. By Theorem 21.3,

$$\bar{A}^{(n)} \leq \gamma^n = \gamma$$

since $\gamma \geq \aleph_0$ implies $\gamma^n = \gamma$ for all finite $n$.

Now $A = \{A_t \mid t \in T\} = \bigcup_{n < \omega} A^{(n)}$, and the sets $A_t$ for different $t$ may coincide only when the corresponding $B_t$ differ — but the index set $T$ has the same cardinality as the family of ordered pairs $\{(A_t, B_t) \mid t \in T\}$. Thus

$$\bar{T} = \bar{A} \leq \sum_{n < \omega} \bar{A}^{(n)} \leq \aleph_0 \cdot \gamma = \gamma.$$

$\square$
