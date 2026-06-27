---
role: proof
locale: en
of_concept: regular-functions-yield-martingales
source_book: gtm040
source_chapter: "3"
source_section: "3"
---

On the cell of the cross-partition where $x_0 = i, \ldots, x_n = j$ and where $\Pr[x_0 = i \land \ldots \land x_n = j] > 0$, we compute the conditional expectation:

$$\mathbf{M}[h(x_{n+1}) \mid x_0 \land \ldots \land x_n] = \mathbf{M}[h(x_{n+1}) \mid x_0 = i \land \ldots \land x_n = j]$$

$$= \sum_k \Pr[x_{n+1} = k \mid x_0 = i \land \ldots \land x_n = j] \cdot h_k$$

$$= \sum_k P_{jk} h_k \quad \text{by the Markov chain property}$$

$$= h_j \quad \text{since } h \text{ is regular}$$

$$= h(x_n).$$

Thus $\mathbf{M}[h(x_{n+1}) \mid \mathcal{R}_n] = h(x_n)$, which together with the finite absolute expectation condition $\mathbf{M}[|h(x_n)|] < \infty$ establishes that $(h(x_n), \mathcal{R}_n)$ is a martingale.
