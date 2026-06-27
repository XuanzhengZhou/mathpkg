---
role: proof
locale: en
of_concept: "let-be-any-cantor-like-set-then-is-compact"
source_book: gtm025
source_chapter: "Topology"
source_section: "6.63"
---

We use the notation of (6.62). Obviously each $P_n$ is closed, so that $P$ is closed and bounded and hence compact (6.44). Since no $P_n$ contains an interval of length $\geq \frac{1}{2^n}$ and $P \subset P_n$ for each $n \in N$, it follows that $P$ contains no interval. Thus $P^{-\circ} = P^{\circ} = \varnothing$; that is, $P$ is nowhere dense in $R$. Next let $x \in P$. For each $n \in N$ we have $x \in P_n$, so that there exists $k_n$ such that $x \in J_{n,k_n}$. Thus, given $\varepsilon > 0$, there is an $n \in N$ such that $\frac{1}{2^n} < \varepsilon$, and therefore the endpoints of $J_{n,k_n}$ are both in $]x - \varepsilon, x + \varepsilon[$. But these endpoints are in $P$. Hence $x$ is a limit point of $P$. We conclude that $P$ is perfect.
