---
role: proof
locale: en
of_concept: proposition-8-75
source_book: gtm040
source_chapter: "8"
source_section: "There exists an equilibrium set"
---

If $h$ is superregular, then $P h \leq h$. Hence, by Lemma 8-74, $\mathbf{M}[h_{n+1} \mid \mathcal{R}_n] \leq h_n$ a.e. for all $n$. If $P^k h$ is finite-valued, then
$$(P^k h)_0 = \sum_{U \in \mathcal{R}_k} \mu(U) h_k(U) = \mathbf{M}[h_k]$$
is finite. Since $h_n$ is constant on cells of $\mathcal{R}_n$, Definition 3-5 is satisfied.

Conversely, if $(h_n, \mathcal{R}_n)$ is a supermartingale, then $\mathbf{M}[h_{n+1} \mid \mathcal{R}_n] \leq h_n$, and hence $P h \leq h$ by Lemma 8-74. Moreover, $\mathbf{M}[h_{k+n}] = (P^{k+n} h)_0$ is finite. If $i = \langle U, n \rangle$, then $P_{0i}^{(n)} = \mu(U) > 0$. From
$$(P^{k+n} h)_0 = \sum_j P_{0j}^{(n)} (P^k h)_j,$$
we see that $(P^k h)_i$ must be finite (since all terms in the sum are nonnegative and the total is finite). The proof for martingales replaces $P h \leq h$ by $P h = h$.
