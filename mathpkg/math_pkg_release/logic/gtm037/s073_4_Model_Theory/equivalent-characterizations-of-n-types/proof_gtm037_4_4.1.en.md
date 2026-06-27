---
role: proof
locale: en
of_concept: equivalent-characterizations-of-n-types
source_book: gtm037
source_chapter: "4"
source_section: "4.1"
---

Obviously $(iii) \Rightarrow (i)$ and $(i) \Rightarrow (ii)$.

$(ii) \Rightarrow (iii)$. Assume $\Delta$ is maximal consistent over $\Gamma$. Expand the language $\mathcal{L}$ to $\mathcal{L}'$ by adjoining new individual constants $c_0, \ldots, c_{n-1}$. Let

$$\Delta' = \{ \varphi(c_0, \ldots, c_{n-1}) : \varphi \in \Delta \}.$$

Since $\Delta$ is consistent over $\Gamma$, every finite subset of $\Delta' \cup \Gamma$ has a model. By the compactness theorem, $\Delta' \cup \Gamma$ has a model $\mathfrak{A}'$. Let $\mathfrak{A}$ be the $\mathcal{L}$-reduct of $\mathfrak{A}'$ and let $a = \langle c_0^{\mathfrak{A}'}, \ldots, c_{n-1}^{\mathfrak{A}'} \rangle$. By the downward Lowenheim--Skolem theorem, we may assume $|A| \leq |\mathrm{Fmla}^n_{\mathcal{L}}|$. Since $\Delta$ is maximal consistent over $\Gamma$, $\Delta$ is exactly the $n$-type of $a$ in $\mathfrak{A}$.
