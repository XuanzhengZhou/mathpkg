---
role: proof
locale: en
of_concept: metrization-theorem
source_book: gtm036
source_chapter: "6"
source_section: "6.7"
---

It is clear that the topology of a pseudo-metrizable space has a countable local base. Conversely, assume that $\{U_n\}$ is a countable local base for the topology of $E$. One constructs a function $g$ on $E$ as follows. Let $g(x) = \inf\{2^{-n} : x \in U_n\}$, and then define a pseudo-metric $d$ by
$$d(x,y) = \inf\left\{\sum_{i=0}^{n} g(x_i - x_{i+1}) : x_0 = x,\; x_{n+1} = y,\; x_i \in E \text{ for } i = 0, \cdots, n\right\}.$$
It is not difficult to see that $d$ is an invariant pseudo-metric, and that each sphere about $0$ is circled. To prove that the pseudo-metric topology is the topology of $E$, it is sufficient to show, in view of the definition of $g$, that $d(x,y) \leq g(x-y) \leq 2d(x,y)$, for all $x$ and $y$ in $E$. The first of these inequalities is clear, and the second will be proved by induction on the number $n$ of links in the chain. For each $n$ it must be shown that
$$g(x_0 - x_{n+1}) \leq 2 \sum_{i=0}^{n} g(x_i - x_{i+1}).$$
For convenience, call the number $\sum_{i=r}^{s} g(x_i - x_{i+1})$ the length of the chain from $r$ to $s+1$. Let $a$ be the length of the chain from $0$ to $n+1$; one can suppose that $a < 2^{-2}$ (otherwise the assertion is trivial). Assume that the required inequality is proved for integers smaller than $n$. Clearly one may suppose $n \geq 1$. Break the chain $0, 1, \cdots, n+1$ into three parts, from $0$ to $k$, $k$ to $k+1$, and $k+1$ to $n+1$ (here $k$ may be equal to $0$ or to $n$), in such a way that the lengths of the first and third parts are at most $a/2$ each. By the induction hypothesis, $g(x_0 - x_k)$ is at most $2(a/2) = a$, and $g(x_{k+1} - x_{n+1})$ is at most $a$. If $m$ is the integer $\geq 2$ such that $2^{-m} \leq a < 2^{-m+1}$, then $x_0 - x_k$, $x_k - x_{k+1}$, and $x_{k+1} - x_{n+1}$ all belong to $U_m$, and hence their sum $x_0 - x_{n+1}$ belongs to $U_{m-1} + U_{m-1} + U_{m-1}$. Using the properties of the chosen local base, one concludes $g(x_0 - x_{n+1}) \leq 2^{-(m-1)} = 2 \cdot 2^{-m} \leq 2a$. This establishes $g(x-y) \leq 2d(x,y)$, completing the proof that the pseudo-metric topology coincides with the original topology.
