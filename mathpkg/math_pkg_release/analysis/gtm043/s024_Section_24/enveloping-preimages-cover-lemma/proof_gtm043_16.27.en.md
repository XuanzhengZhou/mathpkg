---
role: proof
locale: en
of_concept: enveloping-preimages-cover-lemma
source_book: gtm043
source_chapter: "16"
source_section: "27"
---
(a) There exists a cover $\mathcal{W}$ of $g[X]$ such that for each $W \in \mathcal{W}$, the family $\{U \in \mathcal{U}: U \cap g^\leftarrow(W) \neq \emptyset\}$ refines $\mathcal{U}$.

(b) The compact subset $g[X]$ of $\mathbf{R}^n$ is of dimension $\leq n$ (Theorem 16.22). By Corollary 16.8, it has a cover $\mathcal{T}$ of order $\leq n$ whose closures refine $\mathcal{W}$. Then $\mathcal{U}$ envelops the compact set $g^\leftarrow[\operatorname{cl} T_i]$, for each $T_i \in \mathcal{T}$. By Lemma 16.26, the subset $E_i = g^\leftarrow[T_i]$ has a partition $\{E_{i,j}\}_j$ that refines $\mathcal{U}$. Since all $E_i$, and hence all $E_{i,j}$, are open in $X$, the collection $\mathcal{E} = \{E_{i,j}\}_{i,j}$ is a cover—and it refines $\mathcal{U}$. Clearly, the order of $\mathcal{E}$ is that of $\{E_i\}_i$, which is that of $\mathcal{T}$; thus, $\mathcal{E}$ is a refinement of $\mathcal{U}$ of order $\leq n$.

More generally, the lemma holds when $g$ is a continuous mapping from $X$ onto any space of dimension $\leq n$.
