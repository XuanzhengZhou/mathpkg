---
role: proof
locale: en
of_concept: proposition-9-5
source_book: gtm040
source_chapter: "9"
source_section: "1. Potentials"
---

If $\mu$ is a left charge, then $\sum_k |\mu_k| < \infty$ and
$$\nu_j = \lim_n \sum_k \mu_k N_{kj}^{(n)}$$
is finite. Therefore
$$\sum_k \mu_k \left( \frac{N_{kj}^{(n)}}{N_{jj}^{(n)}} \right) \to 0.$$
Since by Lemma 9-3, $N_{kj}^{(n)} / N_{jj}^{(n)} \leq 1$, dominated convergence gives
$$0 = \lim_n \sum_k \mu_k \left( \frac{N_{kj}^{(n)}}{N_{jj}^{(n)}} \right) = \sum_k \mu_k \lim_n \left( \frac{N_{kj}^{(n)}}{N_{jj}^{(n)}} \right) = \sum_k \mu_k H_{kj}.$$
For recurrent states, $H_{kj} = 1$ for communicating $k, j$, giving $\sum_k \mu_k = \mu \mathbf{1} = 0$. The result for functions is dual.
