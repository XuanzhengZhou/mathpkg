---
role: proof
locale: en
of_concept: stationary-chain-decomposition
source_book: gtm046
source_chapter: "X"
source_section: "35"
---

From the decomposition theorem, the state space partitions into invariant atoms $S_t$ of the invariant $\sigma$-field. On each atom $S_t$, the transition probability restricts to $P_t(x, S) = P(x, S)$ for $x \in S_t$.

Stationarity follows because, for each fixed Borel set $S$, the invariance relation $\overline{P}(x, S) = \int \overline{P}(x, dy) P(y, S)$ restricted to $S_t$ yields $\overline{P}_t S = \int_{S_t} \overline{P}_t(dx) P(x, S)$, hence each $\overline{P}_t$ is invariant under the transition probability.

Indecomposability follows because the $\sigma$-field of invariant events restricted to $S_t$ is trivial (contains only events of probability 0 or 1). If the chain on $S_t$ were decomposable, there would exist a nontrivial invariant subset of $S_t$, contradicting the fact that $S_t$ is an atom of the invariant $\sigma$-field. Thus each component chain $\{P_t, P(x, S)\}$ is stationary and indecomposable.
