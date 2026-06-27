---
role: proof
locale: en
of_concept: regular-open-algebra-fails-weak-distributive-law
source_book: gtm008
source_chapter: "20"
source_section: "20"
---

Define $b_{nm} = \{p \in \omega^\omega \mid p(n) = m\}$ for $n, m < \omega$. Then each $b_{nm}$ is clopen in the product topology on $\omega^\omega$ (where $\omega$ has the discrete topology) and therefore regular open.

Clearly,
$$\prod_{n < \omega} \sum_{m < \omega} b_{nm} = 1,$$
since for each $n$, $\bigcup_{m < \omega} b_{nm} = \omega^\omega$, and taking the regular open closure preserves the whole space.

However,
$$\sum_{f \in \omega^\omega} \prod_{n < \omega} \sum_{m \leq f(n)} b_{nm} = 0.$$
Suppose not. Then there exists $f \in \omega^\omega$ such that
$$0 \neq \prod_{n < \omega} \sum_{m \leq f(n)} b_{nm} = \prod_{n < \omega} \{p \in \omega^\omega \mid p(n) \leq f(n)\}^{-0} = \prod_{n < \omega} \{p \in \omega^\omega \mid p(n) \leq f(n)\}.$$
Thus there exist $n_1, \ldots, n_i, l_1, \ldots, l_i$ such that
$$\{p \in \omega^\omega \mid p(n_1) = l_1 \wedge \cdots \wedge p(n_i) = l_i\} \subseteq \bigcap_{n < \omega} \{p \in \omega^\omega \mid p(n) \leq f(n)\}.$$
Choose $n_0 \notin \{n_1, \ldots, n_i\}$ and $l_0 > f(n_0)$. Then
$$\{p \in \omega^\omega \mid p(n_0) = l_0 \wedge p(n_1) = l_1 \wedge \cdots \wedge p(n_i) = l_i\}$$
is nonempty but is contained in the basic open set while violating $p(n_0) \leq f(n_0)$, a contradiction.

Therefore the Boolean algebra of regular open sets of $\omega^\omega$ does not satisfy the $(\omega, \omega)$-WDL.
