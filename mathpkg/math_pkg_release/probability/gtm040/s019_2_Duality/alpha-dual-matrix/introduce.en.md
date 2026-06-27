---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

The alpha-dual matrix formalizes the duality between row vectors (measures) and column vectors (functions) in the context of Markov chains. Given a positive finite-valued superregular measure $\alpha$, the $\alpha$-dual $\hat{P}$ of a transition matrix $P$ is defined by $\hat{P}_{ij} = \alpha_j P_{ji} / \alpha_i$, which can be expressed concisely as $\hat{P} = D P^T D^{-1}$ where $D$ is the diagonal matrix of $1/\alpha_i$. Duality cannot be defined for all Markov chains, but it exists in two important cases: when $P$ is recurrent (yielding the unique reverse chain) and when $P$ has only transient states.
