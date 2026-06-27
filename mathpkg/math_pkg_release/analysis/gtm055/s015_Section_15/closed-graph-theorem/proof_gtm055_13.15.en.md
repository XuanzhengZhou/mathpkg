---
role: proof
locale: en
of_concept: closed-graph-theorem
source_book: gtm055
source_chapter: "13"
source_section: "15"
---
The sufficiency of the condition is easily established. To see this, let $T$ be continuous, and let $(x_0, y_0)$ be a vector in $\mathcal{E} \oplus_1 \mathcal{F}$ that does not belong to $\mathcal{G}$, so that $y_0 \neq Tx_0$. Then there exist disjoint open sets $W_1$ and $W_2$ in $\mathcal{F}$ such that $y_0 \in W_1$ and $Tx_0 \in W_2$. Moreover, since $T$ is continuous, there exists a neighborhood $V$ of $x_0$ in $\mathcal{E}$ such that $T(V) \subset W_2$, and it is readily seen that $V \times W_1$ is a neighborhood of $(x_0, y_0)$ in $\mathcal{E} \oplus_1 \mathcal{F}$ that is disjoint from $\mathcal{G}$. Hence $\mathcal{G}$ is closed.

To prove necessity, if $\mathcal{G}$ is closed in $\mathcal{E} \oplus_1 \mathcal{F}$, then $\mathcal{G}$ is itself an $F$-space. The projection $S: \mathcal{G} \rightarrow \mathcal{E}$ defined by $S(x, Tx) = x$ is a continuous linear bijection. By the Open Mapping Theorem, $S^{-1}$ is continuous, so $T = \pi_2 \circ S^{-1}$ is continuous.
