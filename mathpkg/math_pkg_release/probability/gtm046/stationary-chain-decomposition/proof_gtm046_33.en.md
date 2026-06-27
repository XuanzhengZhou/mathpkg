---
role: proof
locale: en
of_concept: stationary-chain-decomposition
source_book: gtm046
source_chapter: "X"
source_section: "33"
---
Given a stationary chain with transition probability $P(x, S)$, the ergodic theorem for stationary sequences yields the Cesàro limit
$$\frac{1}{n} \sum_{k=1}^n P^k(x, S) \to \bar{P}(x, S)$$
for almost every $x$. The limit $\bar{P}(x, S)$ is a conditional probability given the invariant $\sigma$-field.

By the decomposition theorem for $\sigma$-fields (26.2A), the invariant $\sigma$-field can be partitioned into invariant atoms $S_t$. On each atom, $\bar{P}(x, S)$ takes a constant value $\bar{P}_t S$, giving the decomposition
$$\bar{P} S = \int_T \bar{P}_t S \, \mu(dt).$$
Each component probability $\bar{P}_t$ is invariant under $P(x, S)$:
$$\bar{P}_t S = \int \bar{P}_t(dx) P(x, S),$$
and the corresponding component chain is stationary and indecomposable. The corollary follows directly from the invariance of each $\bar{P}_t$.
