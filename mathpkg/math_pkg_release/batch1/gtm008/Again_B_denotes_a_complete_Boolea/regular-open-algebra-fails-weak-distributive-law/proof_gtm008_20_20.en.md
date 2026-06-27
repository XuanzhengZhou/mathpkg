---
role: proof
locale: en
of_concept: regular-open-algebra-fails-weak-distributive-law
source_book: gtm008
source_chapter: "20"
source_section: "Weak Distributive Laws"
---

Define $b_{nm} = \{p \in \omega^\omega \mid p(n) = m\}$ for $n, m < \omega$. Then each $b_{nm}$ is clopen and therefore regular open. Obviously,

$$\prod_{n < \omega} \sum_{m < \omega} b_{nm} = 1,$$

since for each $n$, $\sum_{m < \omega} b_{nm} = \omega^\omega$. However,

$$\sum_{f \in \omega^\omega} \prod_{n < \omega} \sum_{m \leq f(n)} b_{nm} = 0.$$

Suppose not. Then there exists some $f \in \omega^\omega$ such that

$$0 \neq \prod_{n < \omega} \sum_{m \leq f(n)} b_{nm} = \prod_{n < \omega} \{p \in \omega^\omega \mid p(n) \leq f(n)\}^{-0} = \prod_{n < \omega} \{p \in \omega^\omega \mid p(n) \leq f(n)\}.$$

Then there exist $n_1, \ldots, n_i, l_1, \ldots, l_i$ such that

$$\{p \in \omega^\omega \mid p(n_1) = l_1 \wedge \cdots \wedge p(n_i) = l_i\} \subseteq \bigcap_{n < \omega} \{p \in \omega^\omega \mid p(n) \leq f(n)\}.$$

Choose some $n_0 \notin \{n_1, \ldots, n_i\}$ and $l_0 > f(n_0)$. Then the intersection of the basic open set $\{p \mid p(n_0) = l_0 \wedge \cdots \wedge p(n_i) = l_i\}$ with $\bigcap_{n < \omega} \{p \mid p(n) \leq f(n)\}$ must be nonempty by the inclusion above. But this is impossible because $l_0 > f(n_0)$ contradicts $p(n_0) \leq f(n_0)$. Hence the sum is empty and equals $0$.
