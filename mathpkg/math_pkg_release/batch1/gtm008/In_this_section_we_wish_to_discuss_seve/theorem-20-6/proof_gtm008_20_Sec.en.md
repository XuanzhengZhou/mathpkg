---
role: proof
locale: en
of_concept: theorem-20-6
source_book: gtm008
source_chapter: "20"
source_section: "20 Weak Distributive Laws

Again B denotes a complete Boolean a"
---
Let $\{b_{n,k} \mid n, k < \omega\} \subseteq B$. Then for every real $\varepsilon > 0$

$$(\forall n < \omega) (\exists l \in \omega) \left[ m \left( \sum_{k < \omega} b_{nk} - \sum_{k \leq l}

Proof. Define $b_{nm} = \{p \in \omega^\omega \mid p(n) = m\}$ for $n, m < \omega$. Then $b_{nm}$ is clopen and therefore it is regular open. Obviously,

$$\prod_{n < \omega} \sum_{m < \omega} b_{nm} = 1,$$

but

$$\sum_{f \in \omega^\omega} \prod_{n < \omega} \sum_{m \leq f(n)} b_{mn} = 0.$$

for otherwise there exists some $f \in \omega^\omega$ such that

$$0 \neq \prod_{n < \omega} \sum_{m \leq f(n)} b_{nm} = \prod_{n < \omega} \{p \in \omega^\omega \mid p(n) \leq f(n)\}^{-0}$$

$$= \prod_{n < \omega} \{p \in \omega^\omega \mid p(n) \leq f(n)\}.$$

Then there exist $n_1, \ldots, n_i, l_1, \ldots, l_i$ such that

i) $\{p \in \omega^\omega \mid p(n_1) = l_1 \wedge \cdots \wedge p(n_i) = l_i\}$

$$\subseteq \left( \bigcap_{n < \omega} \{p \in \omega^\omega \mid p(n) \leq f(n)\} \right).$$

Choose some $n_0 \notin \{n_1, \ldots, n_i\}$ and $l_0 > f(n_0)$. Then by i),

$$\{p \in \omega^\omega \mid p(n_0) = l_0 \wedge \cdots \wedge p(n_i) = l_i\} \cap \bigcap_{n < \omega} \{p \in \omega^\omega \mid p(n) \leq f(n)\} \neq 0,$$

Since this intersection is empty we have a contradiction.
