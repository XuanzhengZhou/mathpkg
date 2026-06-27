---
role: proof
locale: en
of_concept: simple-functions-dense-in-vector-lp
source_book: gtm055
source_chapter: "17"
source_section: "18"
---

That the collection $\mathcal{S}$ of integrable simple $\mathcal{E}$-valued mappings constitutes a linear submanifold of $\mathcal{L}_p(X; \mathcal{E})$ for all values of $p$ is obvious. If $\Phi$ belongs to $\mathcal{L}_p(X; \mathcal{E})$ then the function $N_\Phi$ vanishes outside some set having $\sigma$-finite measure, and so therefore does $\Phi$. If $\{\Sigma_n\}$ is a sequence of elements of $\mathcal{S}$ tending to $\Phi$ as in the preceding lemma, then the sequence of functions $h_n(x) = \|\Phi(x) - \Sigma_n(x)\|$ tends to zero a.e. $[\mu]$ and is dominated by the function $3\|\Phi(x)\|$. Hence $\lim_n \int_X h_n^p d\mu = \lim_n \|\Phi - \Sigma_n\|_p^p = 0$ by the dominated convergence theorem. Thus $\mathcal{S}$ is dense in $\mathcal{L}_p(X; \mathcal{E})$.

If $\mathcal{C}_0$ is any countable collection of measurable sets of finite measure whose corresponding equivalence classes form a dense subset of the measure ring of $(X, \mathbf{S}, \mu)$ and $V$ is a countable dense subset of $\mathcal{E}$, then the simple mappings of the form $\sum_{i=1}^N \chi_{E_i} v_i$, where the sets $E_i$ are selected from $\mathcal{C}_0$ and the vectors $v_i$ from $V$, constitute a countable dense set in the linear manifold $\mathcal{S}$ and therefore a dense subset of $\mathcal{L}_p(X; \mathcal{E})$, $1 \leq p < +\infty$, by what has already been shown.
