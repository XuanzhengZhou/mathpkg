---
role: proof
locale: en
of_concept: large-family-of-almost-disjoint-mappings
source_book: gtm043
source_chapter: "12"
source_section: "12.8"
---
By the maximal principle (Zorn's lemma), there exists a maximal subfamily $\mathcal{E}$ of $Y^X$ no two members of which agree on a set of power $\mathfrak{m}$.

Assume $|\mathcal{E}| \leq \mathfrak{m}$. Since $|\mathcal{E}| \leq \mathfrak{m} = |X| = |Y|$, we can enumerate $\mathcal{E} = \{f_\alpha : \alpha < \mathfrak{m}\}$ and well-order $X = \{x_\alpha : \alpha < \mathfrak{m}\}$.

For each $x \in X$, the set $\{f(x) : f \in \mathcal{E}\}$ has cardinality $\leq \mathfrak{m}$. Since $|Y| = \mathfrak{m}$, we can diagonally construct $g \in Y^X$ such that for each $f \in \mathcal{E}$, the set $\{x \in X : g(x) = f(x)\}$ has power $< \mathfrak{m}$. This contradicts maximality of $\mathcal{E}$. Hence $|\mathcal{E}| > \mathfrak{m}$.