---
role: exercise
locale: en
chapter: "5"
section: "18"
exercise_number: 3
---

Prove that E2 and C6 are equivalent for integral networks.

Often E2 is stated and proved in the case where the capacity function and the feasible flows are defined as functions from $D$ into the nonnegative elements of $\mathbb{Q}$ or $\mathbb{R}$. The proof of C6 takes care of the rational case of E2, but not the real case. The difficulty in the real case is that the iteration process need not increase the value of the flow by a fixed minimum amount and hence may never terminate. If the process does not terminate, suppose $h_0, h_1, \ldots$ is a sequence of feasible flows constructed via this iteration process. Since the sequence is bounded above by $k$, there is a function $h \in \mathbb{R}^D$ such that $\lim_{i \to \infty} h_i(x, y) = h(x, y)$ for all $(x, y) \in D$. While it is not

of equivalence will be completed in the same section. There Menger’s Theorem will in turn be used to give another proof of Theorem C6.

Let $(V, D)$ be a directed graph and let $j: V \rightarrow \mathbb{N}$. The function $j$ is called a vertex capacity for $(V, D)$. By a flow in $(V, D)$ we shall mean a flow $h$ in $F(V)$ such that $\sigma(h) \subseteq D$. The value of the flow $h$ at the vertex $x$ is denoted by $h(x)$ and defined by

$$h(x) = \sum_{y \in V + \{x\}} h(y,x).$$

Since the “inflow” equals the “outflow” at $x$, we have by B2 that
