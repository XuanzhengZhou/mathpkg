---
role: proof
locale: en
of_concept: conditional-mean-expansion
source_book: gtm040
source_chapter: "2"
source_section: "6"
---

\begin{proof}
Since the integral is a completely additive set function, we have for every random variable $f$ whose mean exists:
$$M[f] = \sum_i \int_{Q_i} f \, d\mu.$$
For each $i$ with $\Pr[q_i] \neq 0$, the conditional mean is $M[f \mid q_i] = \frac{1}{\Pr[q_i]} \int_{Q_i} f \, d\mu$, so $\int_{Q_i} f \, d\mu = \Pr[q_i] \cdot M[f \mid q_i]$. For $i$ with $\Pr[q_i] = 0$, the integral over $Q_i$ is zero, and the term in the sum is interpreted as $0$. Therefore,
$$M[f] = \sum_i \Pr[q_i] \cdot M[f \mid q_i].$$
\end{proof}
