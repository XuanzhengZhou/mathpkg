---
role: proof
locale: en
of_concept: inner-product-approximation-lemma
source_book: gtm040
source_chapter: "8"
source_section: "5"
---

We have $(g, \bar{g}) = \frac{1}{2}(\mu \bar{g} + \bar{\mu} g)$, and by symmetry it is enough to show that $\bar{\mu}^{(n)}g^{(n)}$ converges to $\bar{\mu} g$. By monotone convergence, we have $\lim g^{(n)} = g$, since $0 \leq f^{(1)} \leq f^{(2)} \leq \cdots$. Let

$$h_i^{(n)} = \begin{cases} g_i^{(n)} & \text{if } i \in E_n \\ 0 & \text{otherwise.} \end{cases}$$

Then

$$\bar{\mu}^{(n)}g^{(n)} = \bar{\mu}h^{(n)}$$

and

$$\lim h^{(n)} = \lim g^{(n)} = g.$$

The functions $h^{(n)}$ are non-negative and increasing; also $\bar{\mu}$ is non-negative. Thus by monotone convergence,

$$\lim \bar{\mu}^{(n)}g^{(n)} = \lim \bar{\mu}h^{(n)} = \bar{\mu} \lim h^{(n)} = \bar{\mu}g.$$
