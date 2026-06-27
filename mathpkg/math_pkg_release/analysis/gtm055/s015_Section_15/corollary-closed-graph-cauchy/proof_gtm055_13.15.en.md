---
role: proof
locale: en
of_concept: corollary-closed-graph-cauchy
source_book: gtm055
source_chapter: "13"
source_section: "15"
---
Consider the graph $\mathcal{G}$ of $T$ as a linear submanifold of $\mathcal{E} \oplus_1 \hat{\mathcal{F}}$, where $\hat{\mathcal{F}}$ denotes the completion of $\mathcal{F}$. If $\{(x_n, Tx_n)\}$ is a sequence in $\mathcal{G}$ converging in $\mathcal{E} \oplus_1 \hat{\mathcal{F}}$ to $(x_0, y_0)$, set $z_n = x_n - x_0$. Then $z_n \to 0$ and $\{Tz_n\}$ is Cauchy, so by hypothesis $Tz_n \to 0$. But $Tz_n = Tx_n - Tx_0 \to y_0 - Tx_0$, so $y_0 = Tx_0$. Thus $\mathcal{G}$ is closed, and $T$ is continuous by the Closed Graph Theorem.
