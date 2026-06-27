---
role: proof
locale: en
of_concept: proposition-8-78
source_book: gtm040
source_chapter: "8"
source_section: "There exists an equilibrium set"
---

Existence and uniqueness of the representation follows immediately from Theorem 5-10 (Riesz decomposition for superregular functions) and Propositions 8-75 and 8-77 (the correspondence between supermartingales and superregular functions, and between potentials and stochastic process potentials). Then $r_n = \lim_k \mathbf{M}[h_{n+k} \mid \mathcal{R}_n]$ by Lemma 8-74.

For the last part, let $(f_n, \mathcal{R}_n)$ be the charge of $(g_n, \mathcal{R}_n)$. Set
$$s_n = f_0 + \cdots + f_{n-1}$$
and
$$s = \lim_n s_n.$$
Then $s_n$ increases monotonically to $s$, and
$$\mathbf{M}[s] \leq \sum_n \mathbf{M}[|f_n|] < \infty$$
by monotone convergence. Since $f_n \geq 0$,
$$g_n = \sum_k \mathbf{M}[f_{n+k} \mid \mathcal{R}_n] = \mathbf{M}\left[\sum_k f_{n+k} \;\middle|\; \mathcal{R}_n\right]$$
$$= \mathbf{M}[s \mid \mathcal{R}_n] - \mathbf{M}[s_n \mid \mathcal{R}_n].$$
Here $\mathbf{M}[s \mid \mathcal{R}_n]$ is a martingale and $\mathbf{M}[s_n \mid \mathcal{R}_n]$ is an increasing process, so $g_n$ is the difference of a martingale and an increasing process.
