---
role: proof
locale: en
of_concept: total-probability-via-alternatives
source_book: gtm040
source_chapter: "2"
source_section: "6"
---

\begin{proof}
Let $f$ be the characteristic function of the set $P$. Then $M[f] = \Pr[p]$ and $M[f \mid q_i] = \Pr[p \mid q_i]$. Applying Proposition 2-11, which states $M[f] = \sum_i \Pr[q_i] \cdot M[f \mid q_i]$, we obtain
$$\Pr[p] = \sum_i \Pr[q_i] \cdot \Pr[p \mid q_i].$$
The equality $\Pr[q_i] \cdot \Pr[p \mid q_i] = \Pr[p \wedge q_i]$ follows from the definition of conditional probability.
\end{proof}
