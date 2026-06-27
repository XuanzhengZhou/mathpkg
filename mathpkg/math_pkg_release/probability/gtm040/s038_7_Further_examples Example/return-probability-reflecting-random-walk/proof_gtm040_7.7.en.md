---
role: proof
locale: en
of_concept: return-probability-reflecting-random-walk
source_book: gtm040
source_chapter: "7"
source_section: "7. Further examples"
---

From state $0$, the chain can return in one step by taking a left step (which reflects back to $0$). This occurs with probability $q = \Pr_0[X_1 = 0]$.

For a return in $2n$ steps ($n \geq 1$), the path must start at $0$, take a right step to $1$, then take $n-1$ additional right steps and $n$ left steps without ever hitting $0$ before the final step. Such a path has exactly $n$ right steps and $n$ left steps, each with probability $p$ and $q$ respectively, giving a factor of $(pq)^n$ per such path.

From Feller [1957], p. 71, the number of paths from $1$ to $1$ of length $2n-2$ that never go below $1$ (i.e., never hit $0$ before step $2n$) is $\binom{2n-2}{n-1} \frac{1}{n}$. This is the $(n-1)$-st Catalan number. Multiplying by the probability $(pq)^n$ of any specific such path gives the stated formula.
