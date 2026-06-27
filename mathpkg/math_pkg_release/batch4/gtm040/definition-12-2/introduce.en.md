---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Given a random field $\{x_t\}$, and finite (non-empty) sets $A$ and $\Lambda$ such that $A \subset \Lambda$, the $(A, \Lambda)$-characteristic is the real-valued function on $\Omega$ given by

$$\mu_A^\Lambda(\iota) = \Pr[x_t = i_t \text{ for all } t \in A \mid x_t = i_t \text{ for all } t \in \Lambda - A]$$

when evaluated at the configuration $\iota = \{i_t; t \in T\}$. For $a \in T$, we abbreviate $\mu_a^\Lambda = \mu_{a^\Lambda}^\Lambda$; the collection $\{\mu_{a^\Lambda}^\Lambda; a \in \Lambda \subset T\}$ is called the local characteristics of the random field.

Throughout this chapter $A$ and $\Lambda$ will always be finite subsets of $T$, even when not explicitly identified as such.

Our immediate objective is to formulate the notion of a Markov field. As motivation, we return briefly to the setting of Chapter 4.
