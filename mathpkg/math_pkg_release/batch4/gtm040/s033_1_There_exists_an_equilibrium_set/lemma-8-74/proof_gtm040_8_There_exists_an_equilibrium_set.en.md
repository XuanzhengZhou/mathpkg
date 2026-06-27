---
role: proof
locale: en
of_concept: lemma-8-74
source_book: gtm040
source_chapter: "8"
source_section: "There exists an equilibrium set"
---

We proceed by induction on $k$. If $k = 0$, the result is trivial. Suppose that both quantities exist for some $k$ and that they correspond. Then
$$(P^{k+1} f)_i = \sum_j P_{ij} (P^k f)_j$$
or in space-time coordinates,
$$(P^{k+1} f)_{\langle U, n \rangle} = \sum_{\substack{V \subset U \\ V \in \mathcal{R}_{n+1}}} \frac{\mu(V)}{\mu(U)} (P^k f)_{\langle V, n+1 \rangle}.$$
By the inductive hypothesis, $(\mathbf{M}[f_{n+k} \mid \mathcal{R}_n], \mathcal{R}_n) \sim P^k f$. Hence, by definition of the correspondence,
$$(P^{k+1} f)_{\langle U, n \rangle} = \frac{1}{\mu(U)} \int_U \mathbf{M}[f_{n+k} \mid \mathcal{R}_n] \,d\mu.$$
By the tower property of conditional expectation,
$$\mathbf{M}[f_{n+k+1} \mid \mathcal{R}_n] = \mathbf{M}[\mathbf{M}[f_{n+k+1} \mid \mathcal{R}_{n+1}] \mid \mathcal{R}_n].$$
Thus $P^{k+1} f$ exists if and only if $\mathbf{M}[f_{n+k+1} \mid \mathcal{R}_n]$ does, and if they exist, they correspond.
