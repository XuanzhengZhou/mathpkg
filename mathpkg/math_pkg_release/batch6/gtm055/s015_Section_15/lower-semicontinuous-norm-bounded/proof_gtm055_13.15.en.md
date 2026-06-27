---
role: proof
locale: en
of_concept: lower-semicontinuous-norm-bounded
source_book: gtm055
source_chapter: "13"
source_section: "15"
---
The sets $M_n = \{x \in \mathcal{E} : \|Tx\| \leq n\}$ are closed for all $n$ (by the lower semicontinuity hypothesis) and cover $\mathcal{E}$. By the Baire category theorem, at least one $M_{n_0}$ has nonempty interior. Thus there exists $x_0 \in \mathcal{E}$ and a neighborhood $U$ of $0$ such that $x_0 + U \subset M_{n_0}$. For any $u \in U$, we have $\|T(x_0 + u)\| \leq n_0$ and $\|Tx_0\| \leq n_0$, so $\|Tu\| \leq 2n_0$. Hence $T$ is bounded on a neighborhood of $0$, and therefore $T$ is bounded.
