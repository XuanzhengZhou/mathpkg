---
role: proof
locale: en
of_concept: induced-class-function-vanishing-mod-p
source_book: gtm042
source_chapter: "11"
source_section: "11.3"
---

Let $S(x)$ be the set of conjugates of $x$. Then

$$\psi'(x) = \frac{\operatorname{Card} Z(x)}{\operatorname{Card} H} \sum_{y \in S(x) \cap H} \psi(y).$$

Let $(Y_i)_{i \in I}$ be the distinct $H$-conjugacy classes contained in $S(x) \cap H$, and choose an element $y_i$ in each $Y_i$. The number of conjugates of $y_i$ in $H$ is equal to $\operatorname{Card} Y_i$, and also equal to $(H : H \cap Z(y_i))$. Therefore

$$\psi'(x) = \frac{\operatorname{Card} Z(x)}{\operatorname{Card} H} \sum_{i \in I} \operatorname{Card} Y_i \cdot \psi(y_i),$$

$$= \sum_{i \in I} n_i \, \psi(y_i), \quad \text{with} \quad n_i = \frac{\operatorname{Card} Z(x)}{\operatorname{Card}(H \cap Z(y_i))}.$$

Suppose we have $n_i \not\equiv 0 \pmod{p}$ for some $i \in I$. Then $H$ contains a conjugate of $C \times P$, contradicting the hypothesis. Hence all $n_i$ are divisible by $p$, and consequently $\psi'(x) \equiv 0 \pmod{p}$.
