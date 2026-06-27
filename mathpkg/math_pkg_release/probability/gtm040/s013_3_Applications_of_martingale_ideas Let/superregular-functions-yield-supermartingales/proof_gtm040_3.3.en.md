---
role: proof
locale: en
of_concept: superregular-functions-yield-supermartingales
source_book: gtm040
source_chapter: "3"
source_section: "3"
---

The proof follows the same computation as for the martingale case. On the cell of the cross-partition where $x_0 = i, \ldots, x_n = j$ and where $\Pr[x_0 = i \land \ldots \land x_n = j] > 0$:

$$\mathbf{M}[h(x_{n+1}) \mid x_0 \land \ldots \land x_n] = \sum_k \Pr[x_{n+1} = k \mid x_0 = i \land \ldots \land x_n = j] \cdot h_k$$

$$= \sum_k P_{jk} h_k \quad \text{by the Markov chain property}$$

$$\geq h_j \quad \text{since } h \text{ is superregular}$$

$$= h(x_n).$$

Thus $\mathbf{M}[h(x_{n+1}) \mid \mathcal{R}_n] \geq h(x_n)$, establishing the supermartingale property. For subregular functions, the inequality $\leq$ replaces $\geq$ in the penultimate step, yielding the submartingale property $\mathbf{M}[h(x_{n+1}) \mid \mathcal{R}_n] \leq h(x_n)$.
