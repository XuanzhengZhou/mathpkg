---
role: proof
locale: en
of_concept: recurrence-criterion-via-current
source_book: gtm040
source_chapter: "9"
source_section: "10"
---

If $0$ is transient, then there is a positive probability $1 - \bar{H}_{00}$ that the chain never returns to $0$. Hence ${}_0 \bar{H}_{0\bar{F}} \geq 1 - \bar{H}_{00} > 0$ for every finite set $F$.

Conversely, let $0$ be recurrent. Choose $N$ sufficiently large that $\bar{H}_{00}^{(N)} > 1 - \epsilon$. Choose $\delta$ close enough to $1$ so that $1 - \epsilon < \delta^N < 1$. Construct an increasing sequence of finite sets $A_0, \ldots, A_N$ such that $A_0 = \{0\}$ and the probability of stepping from any state of $A_k$ to a state of $A_{k+1}$ is greater than $\delta$. Let $F$ be any finite set containing $A_N$. Then ${}_0 \bar{H}_{0\bar{F}} < 2\epsilon$ for all $F$ containing $A_N$.
