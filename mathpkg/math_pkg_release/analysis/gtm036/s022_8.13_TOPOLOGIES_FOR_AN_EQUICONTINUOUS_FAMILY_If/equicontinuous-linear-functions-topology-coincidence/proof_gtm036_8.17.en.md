---
role: proof
locale: en
of_concept: equicontinuous-linear-functions-topology-coincidence
source_book: gtm036
source_chapter: "8"
source_section: "8.17"
---
It is clear that the pointwise topology is weaker than the topology of uniform convergence on totally bounded sets. In order to prove the reverse, it is necessary to prove that, if a net $\{T_\gamma, \gamma \in \Gamma\}$ in $M$ converges pointwise to $T_0$ in $M$, then $\{T_\gamma, \gamma \in \Gamma\}$ converges uniformly to $T_0$ on totally bounded sets.

Let $U$ be a neighborhood of $0$ in $F$; let $V$ be a circled neighborhood of $0$ in $F$ such that $V + V + V \subset U$; and let $W$ be a neighborhood of $0$ in $E$ such that $T$ in $M$ and $x$ in $W$ imply that $T(x) \in V$. If $B$ is a totally bounded subset of $E$, then choose $x_1, x_2, \cdots, x_n$ such that

$$B \subset \bigcup \{x_i + W: i = 1, 2, \cdots, n\}.$$

Next, choose an $\alpha$ such that $T_\gamma(x_i) - T_0(x_i) \in V$ for all $i = 1, 2, \cdots, n$, and for all $\gamma \geq \alpha$. Then any $x$ in $B$ belongs to some $x_i + W$, and

$$T_\gamma(x) - T_0(x) = T_\gamma(x) - T_\gamma(x_i) + T_\gamma(x_i) - T_0(x_i) + T_0(x_i) - T_0(x) \in V + V + V \subset U.$$

It follows that $T$ converges uniformly to $T_0$ on $B$, and the proof is complete.
