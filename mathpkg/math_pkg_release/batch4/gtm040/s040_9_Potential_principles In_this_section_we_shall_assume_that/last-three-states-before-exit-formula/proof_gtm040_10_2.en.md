---
role: proof
locale: en
of_concept: last-three-states-before-exit-formula
source_book: gtm040
source_chapter: "10"
source_section: "2"
---

We compute
\begin{align*}
\Pr[x_{v_E-2} = i \land x_{v_E-1} = j \land x_{v_E} = k]
&= \sum_n \Pr[x_n = i \land x_{n+1} = j \land x_{n+2} = k \\
&\qquad \land \{x_n\} \text{ not in } E \text{ after time } n+2] \\
&= \sum_n \nu_i^{(n)} P_{ij} P_{jk} e_k^E = \nu_i P_{ij} P_{jk} e_k^E,
\end{align*}
where $\nu_i^{(n)} = \Pr[x_n = i]$ and $\sum_n \nu_i^{(n)} = \nu_i$.
