---
role: proof
locale: en
of_concept: pq-random-walk-exit-boundary
source_book: gtm040
source_chapter: "10"
source_section: "13"
---

A calculation like that in Section 5-8 yields

$$H_{ij} = \begin{cases} 1 & \text{if } i \leq j \\ (q/p)^{i-j} & \text{if } i \geq j \end{cases}$$

and consequently

$$N_{ij} = \begin{cases} (p - q)^{-1} & \text{if } i \leq j \\ (q/p)^{i-j}(p-q)^{-1} & \text{if } i \geq j. \end{cases}$$

Both functions $1$ and $(q/p)^i$ are regular and minimal, and thus the exit boundary contains two points, both extreme. No point of $S$ is a limit point. Since the process goes to $+\infty$ with probability one, we have $\mu(\{+\infty\}) = 1$.

The entrance boundary is obtained by reversing the process with respect to the regular measure $\alpha = 1^T$. Then the reversed process is of the same type but with the roles of $p$ and $q$ interchanged. Consequently

$$J(-\infty, j) = 1, \qquad J(+\infty, j) = (p/q)^j,$$

and $\mu^\alpha(\{-\infty\}) = \hat{\mu}(\{-\infty\}) = 1$.
