---
role: proof
locale: en
of_concept: fixed-point-of-semi-normal-functions
source_book: gtm008
source_chapter: "7"
source_section: "7"
---
We define an $\omega$-sequence $\langle \alpha_m \mid m \in \omega \rangle$ by:
\begin{align*}
\alpha_0 &= \alpha, \\
\alpha_{m+1} &= \max\{F_1(\alpha_m), \ldots, F_n(\alpha_m)\} + 1.
\end{align*}
Let $\beta = \bigcup_{m \in \omega} \alpha_m$. For each $i = 1, \ldots, n$, since each $F_i$ is semi-normal (hence continuous at limits):
$$F_i(\beta) = \bigcup_{m \in \omega} F_i(\alpha_m) \leq \bigcup_{m \in \omega} \alpha_{m+1} = \beta.$$
On the other hand, $\beta \leq F_i(\beta)$ since $F_i$ is inflationary. Therefore $F_i(\beta) = \beta$ for all $i$.
