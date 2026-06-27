---
role: proof
locale: en
of_concept: baire-space-fails-omega-omega-wdl
source_book: gtm008
source_chapter: "20"
source_section: "20. Weak Distributive Laws"
---

Let $B = \operatorname{RO}(\omega^\omega)$ be the regular open algebra of the Baire space $\omega^\omega$ with the product topology. For each $n, m < \omega$, define
$$
b_{nm} = \{p \in \omega^\omega \mid p(n) = m\}.
$$
Each $b_{nm}$ is clopen in the product topology, hence regular open, so $b_{nm} \in B$.

For each $n < \omega$, we have $\sum_{m < \omega} b_{nm} = \omega^\omega = 1$, since every $p \in \omega^\omega$ satisfies $p(n) = m$ for exactly one $m$. Therefore,
$$
\prod_{n < \omega} \sum_{m < \omega} b_{nm} = \prod_{n < \omega} 1 = 1.
$$

Now consider the right-hand side of the $(\omega, \omega)$-WDL:
$$
\sum_{f \in \omega^\omega} \prod_{n < \omega} \sum_{m \leq f(n)} b_{nm}.
$$

For each $f \in \omega^\omega$,
$$
\sum_{m \leq f(n)} b_{nm} = \{p \in \omega^\omega \mid p(n) \leq f(n)\},
$$
which is clopen and hence regular open. Therefore,
$$
\prod_{n < \omega} \sum_{m \leq f(n)} b_{nm}
= \prod_{n < \omega} \{p \in \omega^\omega \mid p(n) \leq f(n)\}^{-0}
= \prod_{n < \omega} \{p \in \omega^\omega \mid p(n) \leq f(n)\}.
$$

Suppose, for contradiction, that $\sum_{f} \prod_{n} \sum_{m \leq f(n)} b_{nm} \neq 0$. Then there exists $f \in \omega^\omega$ such that
$$
0 \neq \prod_{n < \omega} \sum_{m \leq f(n)} b_{nm}
= \bigcap_{n < \omega} \{p \in \omega^\omega \mid p(n) \leq f(n)\}.
$$

Since the right-hand side is a nonempty intersection of clopen sets, it contains a nonempty basic open set. Hence there exist $n_1, \ldots, n_i \in \omega$ and $l_1, \ldots, l_i \in \omega$ such that
$$
\{p \in \omega^\omega \mid p(n_1) = l_1 \land \cdots \land p(n_i) = l_i\}
\subseteq \bigcap_{n < \omega} \{p \in \omega^\omega \mid p(n) \leq f(n)\}. \tag{1}
$$

Since the condition $p(n_1) = l_1, \ldots, p(n_i) = l_i$ implies $l_j \leq f(n_j)$ for each $j = 1, \ldots, i$ (by taking $p$ in the basic open set and applying the membership condition with $n = n_j$), we have $l_j \leq f(n_j)$ for all $j$.

Now choose $n_0 \in \omega \setminus \{n_1, \ldots, n_i\}$ and $l_0 \in \omega$ with $l_0 > f(n_0)$. Consider the basic open set
$$
U = \{p \in \omega^\omega \mid p(n_0) = l_0 \land p(n_1) = l_1 \land \cdots \land p(n_i) = l_i\}.
$$
$U$ is nonempty (it specifies values at finitely many coordinates). We claim $U$ is disjoint from $\bigcap_{n < \omega} \{p \in \omega^\omega \mid p(n) \leq f(n)\}$. Indeed, for any $p \in U$, we have $p(n_0) = l_0 > f(n_0)$, so $p \notin \{p \in \omega^\omega \mid p(n_0) \leq f(n_0)\}$, and therefore $p$ cannot belong to the intersection.

But by (1), any $p$ satisfying $p(n_1) = l_1, \ldots, p(n_i) = l_i$ must belong to the intersection. Since $U$ refines this condition (it additionally specifies $p(n_0) = l_0$), it is a subset of the basic open set in (1), hence $U \subseteq \bigcap_{n < \omega} \{p \in \omega^\omega \mid p(n) \leq f(n)\}$.

This contradicts the disjointness established above. Hence
$$
\sum_{f \in \omega^\omega} \prod_{n < \omega} \sum_{m \leq f(n)} b_{nm} = 0,
$$
while $\prod_{n < \omega} \sum_{m < \omega} b_{nm} = 1$. Therefore $B$ does not satisfy the $(\omega, \omega)$-WDL.
