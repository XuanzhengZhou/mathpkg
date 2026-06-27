---
role: proof
locale: en
of_concept: bounded-universal-quantifier
source_book: gtm037
source_chapter: "2"
source_section: "Elementary and Primitive Recursive Functions"
---

Let $S$ be as in Proposition 2.14, with $R$ replaced by $m\omega \sim R$. That is,
$$S = \{ \langle x_0, \ldots, x_{m-1} \rangle : \text{there is a } y < x_{m-1} \text{ such that } \langle x_0, \ldots, x_{m-2}, y \rangle \notin R \}.$$
Then $S$ is an $A$-relation by Proposition 2.14, since the complement $m\omega \sim R$ is an $A$-relation. The set $T$ can be expressed as the complement of $S$:
$$T = m\omega \sim S.$$
Since $A$ is closed under complementation, $T$ is an $A$-relation.
